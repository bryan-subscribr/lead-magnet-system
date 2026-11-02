#!/bin/bash
# Back-end test of a Kit opt-in form without a browser.
# usage: kit_test.sh FORM_ID TAG_ID EMAIL
# Recovered from the Bash call in session cfe87574 at 2026-10-06T14:35:54 (was /tmp/vb/kit_test.sh, lost with /tmp).
# Posts to the form, follows Kit's GDPR consent link if one is returned, accepts it.
# Never solve a CAPTCHA or bot check that Kit shows: if the response status is "quarantined", stop.
# Creates a REAL subscriber: use bryan+<tag>@viralbangers.com addresses and delete them in Kit afterwards.
WORK="${KIT_TEST_WORK:-/tmp/kit_test}"; mkdir -p "$WORK"
R=$(curl -s -X POST "https://app.kit.com/forms/$1/subscriptions" -H "Accept: application/json" --data-urlencode "email_address=$3" --data-urlencode "first_name=Bryan" --data-urlencode "last_name=Test" --data-urlencode "fields[phone_number]=+15555550199" --data-urlencode "tags[]=$2")
echo "$R" | head -c 160; echo
U=$(echo "$R" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('consent',{}).get('url','').split('?')[0])")
if [ -n "$U" ]; then
  curl -s -c "$WORK/cj_$1.txt" "$U?redirect=x" -o "$WORK/c_$1.html"
  TOK=$(python3 -c "import re;print(re.search(r'name=\"authenticity_token\" value=\"([^\"]+)\"',open('$WORK/c_$1.html').read()).group(1))")
  curl -s -b "$WORK/cj_$1.txt" -X POST "$U" --data-urlencode "_method=put" --data-urlencode "authenticity_token=$TOK" --data-urlencode "redirect=https://www.viralbangers.com/?sent=1" --data-urlencode "consent_services=1" -o /dev/null -w "consent %{http_code}\n"
fi
