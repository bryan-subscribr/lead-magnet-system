"""Retire AUDIT + BANGER (Bryan, 2026-10-05). Only SCRIPT, SCOTT, THUMBNAILS, MILLION, EDIT remain.
Rules: CTA_MIGRATION.md. migrate_text() is used by build_planner.py and to rewrite source files in place.
"""
import re

PROMISE = {
    'SCRIPT': "Comment \"SCRIPT\" and I'll send you my scriptwriting guide (the one behind Jordan Welch's 923,571-view video) plus my free full course 🤝",
    'SCOTT': "Comment \"SCOTT\" and I'll send you the full Scott Taylor case study: how he tracks about $40,000 a month back to YouTube 🤝",
    'THUMBNAILS': "Comment \"THUMBNAILS\" and I'll send you the 6-part thumbnail formula that gets RP Profits 4.4x the views 🤝",
    'MILLION': "Comment \"MILLION\" and I'll send you how we got Inayah McMillan 1,185,797 views on one video 🤝",
    'EDIT': "Comment \"EDIT\" and I'll send you the editing checklist we use on Chamath Palihapitiya's channel 🤝",
    'ALGORITHM': "Comment \"ALGORITHM\" and I'll send you the new rules of the YouTube algorithm (for 2027) 🤝",
    'IDEAS': "Comment \"IDEAS\" and I'll send you how we come up with video ideas that build your brand and get you sales 🤝",
    'SETUP': "Comment \"SETUP\" and I'll send you the only setup guide you need for recording YouTube videos 🤝",
    'CLAUDE': "Comment \"CLAUDE\" and I'll send you my full guide to editing YouTube videos with Claude, with every prompt I use 🤝",
}
MAGNET = {'SCRIPT': 'LM5: Jordan Welch scriptwriting guide + free course', 'SCOTT': 'LM1: Scott Taylor case study',
          'THUMBNAILS': 'LM3: RP Profits thumbnail formula', 'MILLION': 'LM4: Inayah McMillan positioning guide',
          'EDIT': 'LM2: Chamath editing checklist', 'ALGORITHM': 'LM6: The new rules of the YouTube algorithm (2027)',
          'IDEAS': 'LM8: BANGER video ideas guide', 'SETUP': 'LM7: Recording setup guide', 'CLAUDE': 'LM9: How to edit YouTube videos using Claude'}
KEEP = list(PROMISE)
_Q = r'["“\\]*'  # straight, curly or JSON-escaped quotes


def topic_keyword(text):
    """Keyword already used in the piece, else the topic fit, else SCOTT (offers / audits / work-with-me)."""
    t = text or ''
    hits = [(m.start(), k) for k in KEEP for m in [re.search(rf'[Cc]omment {_Q}{k}\b|{_Q}{k}{_Q}', t)] if m]
    if hits: return min(hits)[1]
    low = t.lower()
    if re.search(r'\bclaude\b|ai (video )?edit', low): return 'CLAUDE'
    if re.search(r'algorithm|recommend(ed|ation)|engaged views|got pushed', low): return 'ALGORITHM'
    if re.search(r'\bcamera\b|\bmic(rophone)?\b|lighting|\bgear\b|recording setup|\bsetup\b', low): return 'SETUP'
    if re.search(r'video ideas?|what to make next|ideation|topic ideas', low): return 'IDEAS'
    if re.search(r'thumbnail|packaging', low): return 'THUMBNAILS'
    if re.search(r'\bedit(ing|or)?\b|capcut|music', low): return 'EDIT'
    if re.search(r'positioning|outlier|your story|niche angle', low): return 'MILLION'
    if re.search(r'script|hook|course', low): return 'SCRIPT'
    return 'SCOTT'


def migrate_text(text, kw=None):
    if not text or not re.search(r'\bAUDIT\b|\bBANGER\b|audit your channel|free channel audit', text): return text
    t = text
    k = kw or topic_keyword(t)
    nl = r'(?:\\n|\n)'
    # 1. secondary lines after a primary CTA: delete
    t = re.sub(rf'{nl}{{1,2}}Want us to look at your channel too\? Comment {_Q}AUDIT{_Q}', '', t)
    t = re.sub(r' If you want, my team will audit your channel too ?🤝', ' 🤝', t)
    t = re.sub(r'(?:\\n|\n)*If you want, my team will audit your channel too\.?', '', t)
    t = re.sub(rf'{nl}*P\.S\. If yours has gone quiet and you want it back, my team does a free channel audit\. Link in the comments\.', '', t)
    # 2. AUDIT/BANGER as the only CTA: replace with the topic keyword's promise
    t = re.sub(rf'(?:Follow me & )?[Cc]omment {_Q}AUDIT{_Q} and my team will audit your channel(?: and your top competitors)? for free within 24 hours ?🤝?', PROMISE[k], t)
    t = re.sub(rf'[Cc]omment {_Q}BANGER{_Q} and I\'ll message you personally ?🤝?', PROMISE[k], t)
    # 3. keyword lists and labels
    t = t.replace('YOUTUBE / AUDIT / BANGER', 'SCOTT / EDIT / THUMBNAILS / MILLION / SCRIPT')
    t = t.replace('SCOTT / EDIT / THUMBNAILS / MILLION / SCRIPT / AUDIT / BANGER', 'SCOTT / EDIT / THUMBNAILS / MILLION / SCRIPT')
    t = re.sub(r'CTA keyword: (AUDIT|BANGER)\b', f'CTA keyword: {k}', t)
    return t


def migrate_kw(kw, text=''):
    return topic_keyword(text) if kw in ('AUDIT', 'BANGER') else kw
