---
name: lead-magnet-optin-pipeline
description: How a lead magnet, newsletter or training library gets from a Google Doc to a subscriber who has the guide in their inbox, on viralbangers.com. Framer opt-in page (OptIn.tsx, Trainings.tsx) posts to a Kit form, which tags the subscriber and starts a one-email delivery sequence ("[REPLY REQUIRED]" framework) through a visual automation Bryan's MCP cannot create, so it is clicked together in Kit. Includes the 9 guide opt-ins, /newsletter, /trainings, every Kit id, the confirmation-email-off setting, EU consent redirect, quarantine handling, the test protocol and the Framer publish gotchas. Use when Bryan says "create an opt-in page for ...", "add a new lead magnet to the site", "make viralbangers.com/<slug>", "the opt-in isn't delivering", "test the opt-in", or changes a guide link. Not for writing the guide itself (lead-magnet-doc), not for the landing page sections (vb-landing-page), not for ManyChat keyword flows (automation-audit-and-fix).
---

# Lead magnet opt-in pipeline

## 1. What this does and when

One reusable pattern, used 11 times on 2026-10-06 to 2026-10-09: a Framer page holding one code component, a Kit "landing page" used only as a form, a tag, a one-email delivery sequence, and a visual automation that joins the form to the sequence. Pages today: /script /scott /thumbnails /million /algorithm /ideas /setup /edit /claude (guide opt-ins, name + email + phone), /newsletter (redirects to /newsletter-confirmed), /trainings (email only, redirects to /trainings-confirmed, a 9-row library). Use this skill to add a magnet, change a guide link, repair delivery, or test.

## 2. Load first

1. `docs/rules/GLOBAL_RULES.md` (Kit drafts-only rule, never solve CAPTCHAs, never work around a permission block).
2. `docs/access/KIT.md`, `docs/access/FRAMER.md` (runbooks written in this lane), then `docs/access/ACCESS_REGISTRY.md`.
3. Skills `framer` (run `npx @framer/agent@latest setup` first, it is a mandatory precondition) and `framer-code-components`; `bryan-voice` for any email copy; `humanizer`.
4. `skills/lead-magnet-doc/references/LEAD_MAGNET_GUIDES.md` (guide names, doc links, promise lines).
5. Memory copies in `references/memory/`.

## 3. Fixed rules

- **Delivery email framework** (Bryan's own, from his funnel course; 2026-10-06): subject starts "[REPLY REQUIRED] Your Free <guide>", preview "Here's the link, as promised.", body opens "Hey {{ subscriber.first_name }}," then "It's Bryan Ng from Viral Bangers. You signed up for this on my website.", one benefit line, the Google Doc link, "Please reply YES to let me know you've received this. If you don't, I'll email you again to confirm.", sign-off "Thanks, Bryan Ng". Use plain `{{ subscriber.first_name }}`; the Liquid `default: "there"` form got HTML-escaped in testing. Template 3378821 "Viral Bangers Logo template", sender bryan@viralbangers.com. Why: opt-in then instant delivery then reply YES helps deliverability. The promised day-2 resend email does not exist yet.
- **Confirmation email OFF** on every opt-in form (landing page settings gear, Confirmation email tab, "Send confirmation email" off), so the delivery email goes out at once. All 9 guide forms, newsletter and trainings are off.
- **Kit landing pages are only forms.** They stay unpublished. Kit forms cannot email a guide; sequences do.
- **Kit MCP cannot create automations or change form settings.** Build them by clicking in app.kit.com with Claude in Chrome (Bryan's logged-in session).
- **Delivery emails are drafts-only in spirit, but sequences are live**: a sequence email with `published: true` sends to everyone who enters. Create with care; Bryan approved the 9 guides, newsletter and trainings sequences in-session.
- **Never solve a CAPTCHA or bot check.** Kit tripped one on 2026-10-06 after repeated scripted sign-ups (the form returns status "quarantined" with a url); stop testing and tell Bryan.
- **Real sign-up tests create real subscribers**: use `bryan+<tag>@viralbangers.com`, tell Bryan which to delete (Bryan 2026-10-08 "yes yest and submit from me" approved a test as himself).
- **Ask before each of**: publish (publishing ships every unpublished edit on the site), a Kit automation, a test sign-up that submits a real form (observed gate 2026-10-09). Bryan gave "publish it yeah do it in the kit app thats fine" on 2026-10-09 for trainings.
- **Count in the headline is automatic**: /trainings says "Get My {n} Free YouTube Trainings" from the length of the TRAININGS array. Bryan 2026-10-09: "9 trainings is what i have, change it to 9".
- **Thumbnails are images pulled from inside each Google Doc** (Bryan's instruction, 2026-10-09): export docx, take a cover image, upload to Framer. Branded PIL thumbnails (`make_thumbs.py`) were the first attempt and were replaced.
- **noindex**: the 9 guide opt-ins and /trainings-confirmed are noindex; /newsletter and /newsletter-confirmed were not set to noindex (assistant offered, no answer). Keep this convention for confirmation pages.
- **Rating line and "For Coaches Already Doing YouTube" pill** appear on the 9 guide pages; Bryan (2026-10-08 "remove this") had them removed from /newsletter only, by leaving the "Rating line" and "Who it's for" controls empty. The rating is not invented: the template asked for "X.X rated by over X+ clients" and the real rating is unknown.
- **Opt-in copy style**: black ViralBangers bar on top, headline in the guide's own words, subhead, name/email/phone, button "Download Your Free <thing>". Pull the structure from the Lead Generation Academy Webflow reference page Bryan pasted (private course).
- Cleared proof only (`docs/proof/CLAIMS_LEDGER.md`); the newsletter welcome email states Chamath as editing only.
- Number and AI-tells rules apply to every line, including page copy and email copy.

## 4. Workflow (adding or changing a magnet)

Order matters: tag and form first, sequence and email second, Framer third, automation fourth, test last.

1. **Doc ready**: the Google Doc is shared "anyone with the link can view" and its link is in `LEAD_MAGNET_GUIDES.md`.
2. **Kit tag**: `create_tag` (Kit MCP 6ca9b8d9). Existing: lm1_scott through lm10_claude and the three below. Tag ids per guide are in the table in section 9 and in the `MAGNETS` table of `assets/scripts/OptIn.tsx`.
3. **Kit form**: `create_landing_page` named "LM Opt-in: <KEYWORD> (Framer /<slug>)", content_tree with a heading and short text (copy of the one in `references/prompts/2026-10-06_kit-create-landing-page-script.md`). Record the returned form id (the landing page id doubles as the form id used in the POST URL).
4. **Kit sequence**: `create_sequence` "LM Delivery: <KEYWORD> (...)", sender bryan@viralbangers.com, then `create_sequence_email` day 0, delay 0, `email_template_id` 3378821, `published: true`, using the framework above (copy `references/prompts/2026-10-06_kit-delivery-email-script.md` and change subject, benefit line and link).
5. **Framer code component**: `OptIn.tsx` (in `assets/scripts/`) holds a `MAGNETS` record: form id, tag id, doc link, h1, mark (the highlighted words), sub, button, optional `redirect` and `fine`. Add an entry; push the file with `framer.getCodeFiles()` then `setFileContent` and typecheck (ignore "implicitly has an 'any'" errors). The component posts to `https://app.kit.com/forms/{form}/subscriptions` with `first_name`, `last_name`, `fields[phone_number]`, `tags[]`, handles Kit's GDPR consent response (sends the visitor to Kit's consent url and back with `?sent=1`, stripping `response_format`) and the quarantined bot check (redirects to Kit's url so the human proves themselves there). On success it shows the guide link, or navigates to `redirect`.
6. **Framer page**: copy an existing opt-in page (the original was made by duplicating `/book` page shell C57sgcEOv; node ids differ after every copy, so look them up). The component property control is `$control__magnet`; `applyChanges` can set it (`SET <instanceId> $control__magnet="script";`) but not object controls (use the plugin API, see FRAMER.md). Set the page path and `metadata.title` ("Free <guide> | Viral Bangers"), mark noindex for the page.
7. **Kit automation** (clicks, see 4a). Name it "LM Delivery: <KEYWORD> opt-in", turn Active on.
8. **Turn the confirmation email off** on the form (4b).
9. **Publish** (4c), then verify live with curl.
10. **Test** (4d).
11. **Registry**: add form, tag, sequence, automation ids to `docs/access/ACCESS_REGISTRY.md`; update the memory file; if the guide link changed, change both the `MAGNETS` table and the sequence email (the Kit email holds its own copy of the link).

### 4a. Building the Kit automation by clicking (claude-in-chrome, 1512 px wide window, Bryan's Chrome)

Load tools in one ToolSearch call: `tabs_context_mcp, navigate, computer, find, javascript_tool, browser_batch, read_page, get_page_text, form_input`. The Kit editor blocks request introspection, so it is clicked, not scripted.

1. Navigate `https://app.kit.com/automations?tab=rules`; click New automation (1392,112); choose start from scratch (422,402); click Start building (879,286).
2. Choose "Joins a form" (678,352). The form picker is a `select`: list its options with JS (`[...document.querySelectorAll('select')].map(...)` filtered on /LM Opt-in/) to see the exact option values. Typing the name into the picker is flaky: on 2026-10-06 typing "LM Opt-in: SCRIPT" landed on ALGORITHM, so the first automation became ALGORITHM. Set the value by ref click or Enter, then screenshot and check the form name before adding the event (641,444).
3. Click the "+" under the entry (779,438), choose "Email sequence" under "Add the subscriber to", search "LM Delivery: <KEYWORD>", click the result, click Add Action.
4. Scroll up, click the name field (331,42), cmd+a, type "LM Delivery: <KEYWORD> opt-in", turn Active on.
5. Verify: the SCOTT automation's trigger once saved as "Any form" and had to be fixed. Open each saved automation and read the trigger.
6. For nine automations expect per-automation scripts because the picker is flaky. The 9 are all active; SCRIPT's id is 2088337, the other 8 ids are not recorded in any session (read them at https://app.kit.com/automations).

For the newsletter automation (id 2090786): trigger "Joins a form" = Newsletter Opt-in (Framer /newsletter); steps in order: Email sequence "Newsletter Welcome" (2922645), Delay 1 day, Email sequence "VB Welcome Flow" 2918681 (Instagram leads, 30 emails). The delay stops two emails landing at once because VB Welcome Flow email 1 is an agency pitch. Trainings automation (id 2091128): form 10022732 to sequence 2923182, active.

### 4b. Confirmation email off

Open `https://app.kit.com/landing-pages/<formId>/pages/<pageId>/edit` (example newsletter: 10020943 / 10603837; trainings 10022732 / 10605844), landing page settings (gear), Confirmation email tab, toggle "Send confirmation email" off, save.

### 4c. Publish (Framer)

`framer.agent.publish({action:"preview"})` then `confirm_publish` with the `confirmationHash`; check the change list shows only your pages. On 2026-10-09 the agent publish failed with "You do not have permission to publish this site" (the permission classifier also blocks production pushes). Do not work around it. Publish from the Framer editor in Chrome: https://framer.com/projects/Iwi42wjN93nFtnfHZGAW, Publish, Update, confirm the change count is 2. A page that Framer did not register as changed (/thank-youorganic on 2026-10-04) is forced into the publish by renaming one of its layers. Canvas screenshots of VB components are blank (scroll-reveal animations); verify on the live URL with `curl -sL "https://www.viralbangers.com/<slug>?nc=$(date +%s)"` and grep for a key string, or in the Browser pane.

### 4d. Test protocol

1. Back-end first: `scripts/kit_test.sh FORM_ID TAG_ID bryan+<name>@viralbangers.com` (posts, follows the consent link if any). Kit returned the consent link from an EU IP; the component now handles it.
2. Real browser on the live page (Browser pane or Chrome): fill name, email, phone, submit. Kit's EU consent step appears; tick only email consent and leave ad personalisation unticked. Expect to land on the success state or the confirmed page. A browser extension (probably a password manager) can steal typing into the email field: use `form_input` on the field then click submit (2026-10-09).
3. Verify with Kit MCP after 45 seconds: `list_subscribers` (email), `list_subscribers_for_form`, `list_subscribers_for_sequence`, tag present. The tag can lag the consent step by up to a minute.
4. Check the inbox (Claude cannot; Gmail MCP was unreachable on 2026-10-06). Ask Bryan to open the email and reply YES.
5. Back-end contacts created with `create_subscriber` + `bulk_add_subscribers_to_forms` joined the sequences but Kit sent 0 emails (marked Completed); cause never found. Do not rely on that method as proof of delivery; a real browser sign-up is the proof (ALGORITHM and THUMBNAILS passed in a real browser on 2026-10-06 with email 1 sent and opened).
6. Delete or list test subscribers: bryan+lmtest1 to 7, bryan+lmscript, bryan+lmscott, bryan+kitscript, kitscott, kitmillion, kitideas, kitsetup, kitedit, kitclaude, bryan+newsletter (id 4332052353), bryan+trainings (id 4332655648), all @viralbangers.com. Bryan's old [your-email] subscriber signed up on /claude and was tagged "To Delete" and "30-Day-Inactive".

## 5. Variants

- **Newsletter (/newsletter)**: `MAGNETS.newsletter` has `redirect: "/newsletter-confirmed"` and `fine`. Confirmation page is one `VBPage_1` instance, part "all", home controls copied plus a hero override (pill "You're subscribed. Your first email is on its way to your inbox.", h1 "Watch This Video To Double Your Clients From YouTube"), bringing the VSL c2fsj0njer, survey/booking, testimonials and footer. Welcome email 10410684 (sequence 2922645): what you'll get, who I am, three anti-spam steps (reply, move to Primary, add bryan@viralbangers.com to contacts). Recovered verbatim in `references/prompts/2026-10-08_newsletter-welcome-email.md`. Flags: "one email a day" cadence was the agent's wording, Bryan's 7-a-week decision is open.
- **Trainings (/trainings, /trainings-confirmed)**: `Trainings.tsx` (Framer codeFile EYMPI8H) with control "Page" = Opt-in / Library. Email only, tag 24449232, form 10022732. Library page = alternating thumbnail left/right rows with keyword, headline and "Open the training" to each doc. Thumbnails: docx export per guide to `docimgs/`, crop to `thumbs/`, upload; `framer.uploadImage` only accepted a data: URL string, not bytes. The delivery email (sequence 2923182, email 10412552, subject "[REPLY REQUIRED] Your 9 Free YouTube Trainings", preview "All 9 inside. Click any thumbnail to open it.") is generated HTML with the same alternating layout; recovered in `references/prompts/2026-10-09_trainings-delivery-email.md`. Adding a training = one TRAININGS entry plus a new row in the email.
- **Article page (/lead-magnet)**: Inayah case study as an article modelled on Jeremy Haynes' cold-ads page; belongs to `vb-landing-page`.

## 6. QA checklist

- [ ] Doc link opens in a private window.
- [ ] Kit form has confirmation email off; tag exists; sequence email published; link in the email equals link in `MAGNETS`.
- [ ] Automation trigger names the right form (read it), sequence is the right one, Active.
- [ ] Framer page path, title, noindex (confirmation pages), `$control__magnet` correct; no K/M, no AI tells in page copy.
- [ ] Published by Bryan or with his OK; change count matched; live curl shows the new strings.
- [ ] A real browser sign-up reached the success state; Kit shows subscriber, tag, form, sequence.
- [ ] Test subscribers listed for deletion; Bryan told which.
- [ ] Registry, memory file and `LEAD_MAGNET_GUIDES.md` updated.

## 7. Outputs and where they go

Pages on viralbangers.com; Kit objects; local copies of the code components `~/budgetdog-analysis/bryan-system/newsletter/OptIn.tsx` (current, with the skip-empty-rating-line change) and `~/budgetdog-analysis/bryan-system/trainings/Trainings.tsx`; memory `project_lm_optin_pages.md`, `project_newsletter_optin.md`, `project_trainings_library.md`; registry rows.

## 8. Open questions

- «BRYAN: delivery email promises a day-2 resend if no reply; it does not exist. Build it or reword?»
- «BRYAN: 7 of the 9 guide forms were never tested through a real browser; test each once.»
- «BRYAN: why did back-end test contacts get 0 emails (Kit "Completed")? Unresolved.»
- «BRYAN: newsletter cadence "one email a day" vs 7-a-week plan; newsletter pages are not noindex.»
- «BRYAN: EU visitors see Kit's GDPR consent screen; accept or remove?»
- «BRYAN: no dedicated Step 2 confirmation page for the 9 guide opt-ins (on-page success message stands in).»
- «BRYAN: real rating number for the "X.X rated by over X+ clients" line.»
- «BRYAN: /lead-magnet CTA copy and sign-off ("Go make the video only you can make.") were assistant-written.»

## 9. Files

| File | What it is |
|---|---|
| `assets/scripts/OptIn.tsx` | Framer code component, MAGNETS table for 9 guides + newsletter (current version from newsletter/) |
| `assets/scripts/Trainings.tsx` | Framer component for /trainings and /trainings-confirmed |
| `assets/scripts/make_thumbs.py` | PIL branded thumbnails (first attempt, superseded by doc images) |
| `scripts/kit_test.sh` | back-end form test, recovered from the raw session |
| `references/prompts/` | Bryan's briefs (9 opt-ins, /lead-magnet, newsletter), Kit create_landing_page and create_sequence_email inputs, welcome and trainings emails, consent and quarantine patches |
| `references/memory/` | memory copies for opt-in pages, newsletter, trainings |
| private, not copied | Lead Generation Academy (Skool) Step 1 and Step 2 opt-in pages that Bryan pasted (raw session 41f318fa at 2026-10-08T21:58); the Webflow preview reference |

Kit ids (all in account "Viral Bangers"):

| Magnet | Form id | Tag id | Delivery sequence | Doc id |
|---|---|---|---|---|
| SCRIPT | 10010068 | 24299541 | 2918565 | 1OnxBRiIg-9a8PKmah0Ani9zUF0RS0fGpLmVhh5A1xsk |
| SCOTT | 10010079 | 24299537 | 2918569 | 14JHrz6mIf3rHIYbzqLa_GdaU-cp0jq-zLl1NWMcUI1I |
| THUMBNAILS | 10010080 | 24299539 | 2918570 | 1gz4VoJxQW9mt_qVE0l27R_-AwdxTiEZDQ7w_4YUsf3A |
| MILLION | 10010081 | 24299540 | 2918571 | 1G6gyDiWEyE6oTNBS56qdIFeZ8Fh6ox_41vsOz2TeuN8 |
| ALGORITHM | 10010082 | 24332416 | 2918572 | 1uKia2GXBI592Nrk6-4wS_m_49b0uG7ifWi3uqPEW5R8 |
| IDEAS | 10010083 | 24332417 | 2918573 | 1zzV1Vz8aGbl24ftDvYGTMoSuV8sTb4INJ5hE9U-Lak8 |
| SETUP | 10010084 | 24332418 | 2918574 | 1-gyDLFbtP6LnwG2-gsfRMVzYnaAg5UWPiS-0txBdTfU |
| EDIT | 10010085 | 24299538 | 2918575 | 1-qo8fvNmqzGHifdI28FOddSi3QM-QtveNpd82FLQ-BQ |
| CLAUDE | 10010086 | 24333917 | 2918576 | 1VxLy8Jy2nu7GVoJXXI3lvYyA62j5LmixJq82Dq6FwyA |
| Newsletter | 10020943 (page 10603837) | 24419564 | 2922645 (email 10410684) | none, redirect to /newsletter-confirmed |
| Trainings | 10022732 (page 10605844) | 24449232 | 2923182 (email 10412552) | none, redirect to /trainings-confirmed |

Sequence email ids seen: SCRIPT 10397901, ALGORITHM 10397916. SCRIPT form page 10591623, ALGORITHM page 10591638. Automations: SCRIPT 2088337, newsletter 2090786, trainings 2091128. Framer ids: project Iwi42wjN93nFtnfHZGAW; OptIn code file `codeFile/h7vTq5B:default`; opt-in page node ids scott dbbkj_ioa, thumbnails cJOtmHNTc, million l8gUYtPUY, algorithm xlJNvWr9V, ideas olOUEXwWw, setup IitoYGgU0, edit KXiwmTY3I, claude f1156P2zL (page nodes, checked 2026-10-06); /newsletter page sFS4XMbRR, /newsletter-confirmed JEGYdsLNh, /trainings JjUFRGrqb (instance mNs4zRhR9), /trainings-confirmed tg9htG_5D (instance S6dSsV_hM). Published versions: newsletter 366802017, newsletter badge removal 2a83a498b.

Items not recovered: the other 8 automation ids; each guide's per-page Framer ids beyond the list above; the day-2 resend email (never built); Bryan's verbal instruction on thumbnails from doc images (referenced "as you asked", not visible in the card or raw at the window checked).

## 10. Session provenance

`_mining/cards/`: 2026-10-02_cfe87574 (9 opt-ins, section C), 2026-10-08_41f318fa (newsletter), 2026-10-09_5b5e4774 (trainings, blog audit in `blog-framer`); memory `project_lm_optin_pages.md`, `project_newsletter_optin.md`, `project_trainings_library.md`.
