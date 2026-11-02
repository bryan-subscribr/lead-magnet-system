# OptIn.tsx patch: Kit GDPR consent redirect
Recovered verbatim from raw session cfe87574 at 14:51:27 (Bash). Source: /Users/bryanng/.claude/projects/-Users-bryanng/cfe87574*.jsonl. Original punctuation kept.

--- command ---
cd /tmp/vb && python3 - <<'PY'
p='/tmp/vb/OptIn.tsx'; s=open(p).read()
a='''            if (data?.consent?.enabled && data?.consent?.url) {'''
b='''            if (data?.status === "quarantined" && data?.url) {
                // Kit's bot check: the visitor proves they're human on Kit's page, then Kit finishes the sign-up.
                window.location.href = data.url
                return
            }
            if (data?.consent?.enabled && data?.consent?.url) {'''
assert s.count(a)==1; s=s.replace(a,b)
open(p,'w').write(s)
PY
cd ~ && npx -y @framer/agent@latest exec -s 1 <<'FRAMER_EXEC' 2>&1 | grep -v "npm notice"
const fs = require("fs");
const f = (await framer.getCodeFiles()).find(f => f.name === "OptIn.tsx");
const u = await f.setFileContent(fs.readFileSync("/tmp/vb/OptIn.tsx","utf8"));
console.log("errors:", JSON.stringify((await u.typecheck()).filter(e => !/implicitly has an 'any'/.test(e.message)).map(e => e.span.start.line + ": " + e.message)));
const p = await framer.agent.publish({ action: "preview" });
console.log(JSON.stringify({ status: p.status, errors: p.errors, warnings: p.warnings, changes: p.changes?.map(c => c.name + ":" + c.status) }));
if (p.status === "ready" && !(p.errors||[]).length) {
  const r = await framer.agent.publish({ action: "confirm_publish", confirmationHash: p.confirmationHash });
  console.log(JSON.stringify({ status: r.status, message: r.message }));
}
FRAMER_EXEC
--- description ---
Add bot-check handling and publish the site
--- timeout ---
300000
