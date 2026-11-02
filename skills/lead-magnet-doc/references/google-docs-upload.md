# Getting the .docx into Google Docs (Claude in Chrome)

The Drive MCP connector is probably a different Google account from Bryan's Chrome, and passing a 3MB+ file as base64 isn't practical. So the upload goes through his Chrome. Load these tools in one ToolSearch call: `tabs_context_mcp, navigate, computer, find, file_upload, javascript_tool, browser_batch, tabs_close_mcp`.

The file has to sit somewhere the browser tool can read, for example the lead magnet folder in `~/budgetdog-analysis/...`. Not the scratchpad.

## 1. Upload (intercept Drive's file picker)
Synthetic drag-and-drop is ignored by Drive, and the native picker can't be driven. Patch `click` so Drive's own hidden input gets captured instead:
1. `tabs_context_mcp {createIfEmpty:true}`, then navigate to `https://drive.google.com/drive/my-drive`.
2. Run this in javascript_tool:
   ```js
   const oc=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'&&!this.webkitdirectory){this.setAttribute('aria-label','drive captured upload');if(!this.isConnected)document.body.appendChild(this);this.style.cssText='display:block;position:fixed;top:60px;left:0;z-index:99999;';window.__cap=this;return;}return oc.apply(this,arguments)};'patched'
   ```
3. Click **New**, take a screenshot, and click **File upload**. The menu toggles, so click it once and check the screenshot.
4. Run `find "drive captured upload file input"`, then call `file_upload` with that ref and the docx path.
5. Wait about 8s. Then on `drive.google.com/drive/recent`, grab the id: `[...new Set([...document.querySelectorAll('[data-id]')].map(e=>e.getAttribute('data-id')+' :: '+e.textContent.slice(0,50)))]`.

## 2. Convert to a native Google Doc
Build the upload copy with `docbuilder.py ... --docs` (blank lines under the TOC heading, no static TOC). Open `docs.google.com/document/d/<docx id>/edit?rtpof=true&sd=true` (the plain /edit URL can hang forever on "Opening the file") and click **File**. The menubar File item sits at about (73,45) in the 1512-wide frame, and (38,43) is the Docs home logo, so don't click there. Then click **Save as Google Docs**. A new tab opens with the converted doc, and `tabs_context_mcp` shows its id and URL.

## 3. Insert the real TOC
1. Scroll to page 2. The "Table Of Contents" heading is followed by two empty lines.
2. Click at the end of the heading, then press End, then Down Down.
3. **Never use cmd+f + type.** The keystrokes can land in the doc. If that happens, undo with cmd+z and check the title.
4. Insert → Page elements → Table of contents → 2nd thumbnail (dotted leaders + page numbers). Click through: Insert (205,45) → Page elements (265,513) → TOC (593,346) → style 2 (855,382), checking a screenshot at each step.
5. Docs includes H2s by default. For an H1-only TOC: click the TOC, the ⋮ menu → Table of contents options → Heading levels → untick Heading 2, close the panel, then click the TOC refresh icon so page numbers update.
6. Take a screenshot to confirm the entries and page numbers.

## Gotchas
- Pasting from one doc into another with synthetic cmd+c/cmd+v **does not work**. Every rebuild becomes a new doc with a new link, so tell Bryan the new link and offer to trash the old ones. Only trash files when he says yes.
- Close the extra .docx tabs you opened, and leave the final doc tab open for Bryan.
