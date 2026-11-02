#!/bin/bash
cd /Users/bryanng/lead_magnets/NICHE/work
yt-dlp -q -f "bv*[height<=1080][ext=mp4]" --download-sections "*1:50-16:00" -o v_bryan.mp4 "https://www.youtube.com/watch?v=qdE8FKQC_Vg"
yt-dlp -q -f "bv*[height<=1080][ext=mp4]" -o v_howtoai.mp4 "https://www.youtube.com/watch?v=dsHpzIx_VQ0"
yt-dlp -q -f "bv*[height<=1080][ext=mp4]" -o v_noah.mp4 "https://www.youtube.com/watch?v=E5IzG1q0M14"
ls -la
