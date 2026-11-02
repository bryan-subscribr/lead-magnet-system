#!/bin/bash
cd /Users/bryanng/lead_magnets/TIKTOK/work/vids
for id in julmRjiSasM RU6yYP1RjDI s4UkCaf_scs -or5CLiuR3c GHrhzZv_MwQ xLLVn0-k5Wg Izmx3UVjNIc _GPSfzoVvC4 eCtRi8C8cuk ozRs8z25puM Y64FHeLz8QE CSSUx4TuGug; do
  [ -f "v_$id.mp4" ] || yt-dlp -q --no-warnings -f "bv*[height<=720][ext=mp4]/bv*[height<=720]" -o "v_$id.%(ext)s" -- "https://www.youtube.com/watch?v=$id" || echo "FAIL $id"
done
yt-dlp -q --no-warnings -f "bv*/b" -o "v_tiktok_nav.%(ext)s" "https://www.tiktok.com/@simonsquibb/video/7669456900089531670" || echo "FAIL tiktok"
ls -la
