#!/bin/bash
# Render a .docx to PDF with Pages and make contact sheets for a visual QA pass.
# Usage: render_check.sh IN.docx OUTDIR
# Pages swaps Lora for a default font. That's fine: Google Docs shows Lora.
set -e
IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; OUT="$2"; mkdir -p "$OUT"
osascript -e 'tell application "Pages" to activate' >/dev/null; sleep 4
osascript <<EOF
set src to POSIX file "$IN"
set outF to POSIX file "$OUT/render.pdf"
tell application "Pages"
  set d to open src
  delay 6
  export d to outF as PDF
  close d saving no
end tell
EOF
pdfinfo "$OUT/render.pdf" | grep Pages
rm -f "$OUT"/p-*.png
pdftoppm -r 40 -png "$OUT/render.pdf" "$OUT/p"
python3 - "$OUT" <<'PY'
import sys,glob
from PIL import Image
o=sys.argv[1]; fs=sorted(glob.glob(o+'/p-*.png')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size
for k in range(0,len(ims),12):
    c=Image.new('RGB',(w*6,h*2),'white')
    for j,im in enumerate(ims[k:k+12]): c.paste(im,((j%6)*w,(j//6)*h))
    c.save(f'{o}/contact{k//12}.png')
print('contact sheets:', sorted(glob.glob(o+'/contact*.png')))
PY
