// De-AI pass on the 9 live lead-magnet Google Docs (2026-10-09).
// DATA = {name: {id, pairs: [[old, new], ...], unbold: [text, ...]}} is prepended by the loader.
// Edits text in place: keeps the doc ID, images, links, TOC and the formatting of each replaced run.
// A pair is applied only when the old text is found exactly once outside the table of contents.

function esc_(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

function inToc_(el) {
  var p = el;
  while (p) {
    if (p.getType && p.getType() == DocumentApp.ElementType.TABLE_OF_CONTENTS) return true;
    p = p.getParent ? p.getParent() : null;
  }
  return false;
}

function findOnce_(body, text) {
  var pat = esc_(text), r = body.findText(pat), hits = [];
  while (r) {
    if (!inToc_(r.getElement())) hits.push(r);
    if (hits.length > 1) break;
    r = body.findText(pat, r);
  }
  return hits;
}

function applyDoc_(name) {
  var d = DATA[name], doc = DocumentApp.openById(d.id), body = doc.getBody();
  var done = 0, skipped = [];
  d.pairs.forEach(function (p) {
    var o = p[0].trim(), n = p[1].trim();
    if (!o || o.indexOf('\n') >= 0) { skipped.push('nl:' + o.slice(0, 50)); return; }
    var hits = findOnce_(body, o);
    if (hits.length != 1) { skipped.push(hits.length + ':' + o.slice(0, 60)); return; }
    var h = hits[0], el = h.getElement().asText(), s = h.getStartOffset(), e = h.getEndOffsetInclusive();
    var attrs = el.getAttributes(s);
    el.deleteText(s, e);
    if (n) {
      el.insertText(s, n);
      el.setAttributes(s, s + n.length - 1, attrs);
    }
    done++;
  });
  var unbolded = 0;
  (d.unbold || []).forEach(function (t) {
    t = t.trim();
    if (!t || t.length < 4) return;
    var hits = findOnce_(body, t);
    if (hits.length != 1) return;
    var h = hits[0];
    h.getElement().asText().setBold(h.getStartOffset(), h.getEndOffsetInclusive(), false);
    unbolded++;
  });
  doc.saveAndClose();
  return name + ': replaced ' + done + '/' + d.pairs.length + ', unbolded ' + unbolded + (skipped.length ? ' | skipped: ' + JSON.stringify(skipped) : '');
}

function scan_(name) {
  var t = DocumentApp.openById(DATA[name].id).getBody().getText();
  var pats = {emdash: /—/g, endash: /–/g, arrow: /→|->/g, heres: /\bhere'?’?s (the|what|how|why)\b/gi, slowly: /read this one slowly/gi,
              adverb: /\b(quietly|deeply|fundamentally|remarkably|arguably|leverage|robust|streamline|harness|delve|unlock|seamless|tapestry|game.?changer)\b/gi};
  var out = {};
  for (var k in pats) { var m = t.match(pats[k]); if (m) out[k] = m.length; }
  return name + ' scan: ' + JSON.stringify(out);
}

function runAll() {
  var log = [];
  Object.keys(DATA).forEach(function (n) { log.push(applyDoc_(n)); });
  Object.keys(DATA).forEach(function (n) { log.push(scan_(n)); });
  Logger.log(log.join('\n'));
  return log;
}

function scanAll() {
  var log = Object.keys(DATA).map(scan_);
  Logger.log(log.join('\n'));
}
