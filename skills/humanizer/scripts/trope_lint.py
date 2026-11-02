#!/usr/bin/env python3
"""
trope-lint.py - check email drafts against the AI-writing-tropes list.

Usage:
    python3 trope-lint.py FILE.md [FILE.md ...]
    python3 trope-lint.py DIR/
    python3 trope-lint.py DIR/ --quiet      # only failures
    python3 trope-lint.py DIR/ --json

Exit 1 if any ERROR fires or any CAP is exceeded.

Severity:
  ERROR  never acceptable in Bryan's copy
  CAP:n  allowed up to n times per email (a device that works once and grates at ten)
  INFO   reported, judgement call, never fails the build

Bryan's verified voice is exempted on purpose. His corpus has 100 fragment paragraphs opening
with Because/And/But/So across 15 emails, and the "X isn't the hard part, Y is" contrast is a
documented signature. Those are capped, not banned. Sanding them out would remove the voice.
"""
import re, sys, json, os

# (name, regex, severity, cap)
RULES = [
 # --- word choice
 ("magic adverb",            r"(?i)\b(quietly|deeply|fundamentally|remarkably|arguably)\b", "ERROR", 0),
 ("delve family",            r"(?i)\b(delve|delving|utili[sz]e|streamline|harness(?:ing)?|robust|plethora|myriad|paramount|certainly)\b", "ERROR", 0),
 ("leverage as verb",        r"(?i)\bleverag(?:e|es|ed|ing)\b", "ERROR", 0),
 ("grandiose noun",          r"(?i)\b(tapestry|landscape|paradigm|synergy|ecosystem|framework)\b", "ERROR", 0),
 ("serves-as dodge",         r"(?i)\b(serves as|stands as|represents a|marks a)\b", "ERROR", 0),
 # --- sentence structure
 ("negative parallelism",    r"(?i)(\b(?:is|are|was|were|it'?s|that'?s)\s+not\s+[^.!?]{2,70}[.,]\s*(?:it'?s|that'?s|the)\b"
                             r"|\bnot because\b[^.!?]{2,60}\bbut because\b"
                             r"|(?<=[.!?]\s)The \w+ isn'?t [^.!?]{2,60}\. The \w+ is\b)", "CAP", 1),
 ("Not X. Not Y. Just Z.",   r"(?<=[.!?]\s)Not [^.!?]{2,45}\.\s*Not [^.!?]{2,45}\.", "ERROR", 0),
 ("question-then-answer",    r"(?i)\b(the (?:result|worst part|scary part|problem|catch|best part|kicker))\?\s", "ERROR", 0),
 ("worth-noting filler",     r"(?i)\b(it'?s worth noting|it bears mentioning|importantly,|interestingly,|notably,)", "ERROR", 0),
 ("superficial -ing tail",   r"(?i),\s+(highlighting|underscoring|reflecting|demonstrating|showcasing|contributing to|cementing|solidifying)\b", "ERROR", 0),
 ("false range",             r"(?i)\bfrom\s+[\w'-]+\s+to\s+[\w'-]+\b", "INFO", 0),
 # --- tone
 ("here's-the-kicker",       r"(?i)\bhere'?s (?:the (?:thing|kicker|deal|catch)|where it gets|what most people)", "ERROR", 0),
 ("here's/here is",          r"(?i)\bhere(?:'s| is| are)\b", "CAP", 1),
 ("think-of-it-as",          r"(?i)\b(think of it (?:as|like)|imagine a world|it'?s like a)\b", "ERROR", 0),
 ("false vulnerability",     r"(?i)\b(and yes,|i'?ll be honest with you|this is not a rant|let'?s be honest,)", "ERROR", 0),
 ("truth-is-simple",         r"(?i)\b(the (?:truth|reality) is[,:]?\s|history is (?:clear|unambiguous)|the real story is)", "ERROR", 0),
 ("stakes inflation",        r"(?i)\b(fundamentally reshape|define the next era|change everything about|something entirely new)\b", "ERROR", 0),
 ("pedagogical voice",       r"(?i)\blet'?s (?:break (?:this|it) down|unpack|explore|dive in|dig in)\b", "ERROR", 0),
 ("vague attribution",       r"(?i)\b(experts (?:say|argue|agree)|industry reports|observers have|studies show|research shows|many creators find)\b", "ERROR", 0),
 ("invented concept label",  r"(?i)\b[a-z]+\s+(paradox|trap|creep|divide|vacuum|inversion)\b", "ERROR", 0),
 # --- formatting
 ("em dash",                 r"\u2014|\u2013", "ERROR", 0),
 ("en dash in prose",        r"(?<=\w)–(?=\w)", "ERROR", 0),
 ("smart quote",             r"[‘’“”]", "ERROR", 0),
 ("unicode arrow",           r"[→←⇒⇐]", "ERROR", 0),
 ("bold-first bullet",       r"(?m)^\s*[-*]\s*\*\*", "ERROR", 0),
 # --- Bryan-specific
 ("uncontracted form",       r"\b(do not|does not|did not|is not|are not|was not|were not|cannot|will not|would not|have not|has not)\b", "CAP", 1),
 ("corporate connector",     r"(?i)\b(furthermore|moreover|in addition|therefore|thus|consequently|nevertheless)\b", "ERROR", 0),
]

# applied with re.S so multi-line YAML notes are actually removed
FRONTMATTER = r"\A---\n.*?\n---\n"

STRIP = [
 (r"(?m)^>.*$", ""),                       # note blockquotes
 (r"«[^»]*»", ""),                         # BRYAN placeholders
 (r"(?m)^#{1,6} .*$", ""),                 # headers
 (r"(?m)^\*\*(?:Subject|Preview|Subject options).*$", ""),
 (r"(?m)^(?:Subject options:|Preview:).*$", ""),
 (r"(?m)^\d+\.\s.*$", ""),                 # numbered subject options
 (r"(?ms)^## (?:Self-Scorecard|Risks|Why This Should Work|Strategy Brief|Notes?).*?(?=^## |\Z)", ""),
 (r"(?ms)^## Generic swap.*\Z", ""),
 (r"(?m)^\|.*$", ""),                      # tables
 (r"\{\{[^}]*\}\}", "MERGEFIELD"),         # merge fields are not prose
 (r"https?://\S+", "URL"),
 (r"(?m)^(?:Bryan|Co-founder, Subscribr|Hope this helps,|Hope this inspires,|Talk soon,|See you inside,)\s*$", ""),
]

def extract(text):
    text = re.sub(FRONTMATTER, "", text, flags=re.S)
    for rx, rep in STRIP:
        text = re.sub(rx, rep, text, flags=re.S if "(?ms)" in rx or "(?s" in rx else 0)
    return text

def anaphora(body):
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    starts = [p.split()[0].strip(",.:;").lower() for p in paras if p.split()]
    worst, run, word = 1, 1, ""
    for i in range(1, len(starts)):
        if starts[i] == starts[i-1]:
            run += 1
            if run > worst: worst, word = run, starts[i]
        else:
            run = 1
    return worst, word

def drone(body):
    """Short paragraphs are Bryan's voice. UNIFORM length is the actual failure.
    Flags a run of 5+ consecutive sentences whose word counts sit within 3 of each other."""
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body.replace("\n", " ")) if s.strip()]
    lens = [len(s.split()) for s in sents]
    worst, run = 0, 1
    for i in range(1, len(lens)):
        if abs(lens[i] - lens[i-1]) <= 3:
            run += 1; worst = max(worst, run)
        else:
            run = 1
    return worst

def trenchcoat(body):
    hits = re.findall(r"(?im)^(?:First|Second|Third|Fourth|The first|The second|The third)\b[,.]?\s", body)
    return len(hits)

def dead_metaphor(body):
    words = re.findall(r"\b[a-z]{6,}\b", body.lower())
    stop = {"because","channel","subscribr","already","people","actually","something","thumbnail",
            "видео","without","another","everything","nothing","yourself"}
    from collections import Counter
    c = Counter(w for w in words if w not in stop)
    return [(w,n) for w,n in c.most_common(3) if n >= 6]

def lint_email(name, body):
    findings = []
    for rname, rx, sev, cap in RULES:
        ms = [m.group(0) for m in re.finditer(rx, body)]
        if not ms: continue
        if sev == "ERROR":
            findings.append((sev, rname, len(ms), ms[:3]))
        elif sev == "CAP" and len(ms) > cap:
            findings.append((f"CAP>{cap}", rname, len(ms), ms[:3]))
        elif sev == "INFO":
            findings.append(("INFO", rname, len(ms), ms[:3]))
    a, word = anaphora(body)
    if a >= 3: findings.append(("ERROR", f"anaphora ('{word}' x{a} paras)", a, []))
    dr = drone(body)
    if dr >= 6: findings.append(("ERROR", f"uniform sentence length ({dr} in a row)", dr, []))
    tc = trenchcoat(body)
    if tc >= 3: findings.append(("ERROR", f"listicle in a trench coat ({tc} markers)", tc, []))
    for w, n in dead_metaphor(body):
        findings.append(("INFO", f"repeated word '{w}'", n, []))
    return findings

def split_emails(path, text):
    """Return [(label, body)]. Handles the three draft shapes in this repo."""
    if re.search(r"(?m)^## (?:Email|Day) ", text):
        parts = re.split(r"(?m)^## ([^\n]*)$", text)
        out = []
        for i in range(1, len(parts), 2):
            title = parts[i].strip()
            if not re.match(r"(?:Email|Day) ", title):
                continue                      # build specs, appendices, question lists
            out.append((title, extract(parts[i+1])))
        return out
    return [(os.path.basename(path), extract(text))]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    files = []
    for a in args:
        if os.path.isdir(a):
            files += sorted(os.path.join(a, f) for f in os.listdir(a)
                            if f.endswith(".md") and not f.startswith(("judge-", "SEQ-E07-activation-PLAN")))
        else:
            files.append(a)
    total_fail = 0; report = []
    for f in files:
        text = open(f).read()
        for label, body in split_emails(f, text):
            if len(body.split()) < 40: continue
            fs = lint_email(label, body)
            fails = [x for x in fs if x[0] != "INFO"]
            total_fail += len(fails)
            report.append(dict(file=os.path.basename(f), email=label,
                               words=len(body.split()), findings=fs))
    if "--json" in flags:
        print(json.dumps(report, indent=1)); sys.exit(1 if total_fail else 0)
    print(f"trope-lint: {len(report)} emails checked\n")
    for r in report:
        fails = [x for x in r["findings"] if x[0] != "INFO"]
        if "--quiet" in flags and not fails: continue
        status = f"{len(fails)} FAIL" if fails else "clean"
        print(f"  {r['email'][:44]:46} {r['words']:4}w  {status}")
        for sev, rname, n, ex in r["findings"]:
            if "--quiet" in flags and sev == "INFO": continue
            exs = ("  " + " | ".join(repr(e) for e in ex)) if ex else ""
            print(f"        [{sev}] {rname} x{n}{exs}")
    print(f"\n{'FAILURES: ' + str(total_fail) if total_fail else 'ALL CLEAN'}")
    sys.exit(1 if total_fail else 0)

if __name__ == "__main__":
    main()
