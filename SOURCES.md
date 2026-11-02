# Where every image and data point comes from

This is the full list of places the lead magnet system pulls images, screenshots and numbers from, and the exact commands used. The scripts that do it are in `image-scripts/` (one folder per guide) and `skills/lead-magnet-doc/scripts/images.py`.

## 1. Frames from YouTube videos (the main source)

Used for: screen-share tutorials (the CLAUDE editing guide), YouTube Studio tabs, analytics screens, your own videos, case-study videos.

```bash
# download video only (no audio needed, never play sound)
yt-dlp -f "bv*[height<=1080][ext=mp4]" -o work/video.mp4 "https://www.youtube.com/watch?v=<ID>"
# or just a window around the moment you need
yt-dlp -f "bv*[height<=1080][ext=mp4]" --download-sections "*12:30-13:30" -o work/clip.mp4 "<URL>"

# contact sheets to find moments: 1 frame every 4 seconds with a timestamp burned in
ffmpeg -i work/video.mp4 -vf "fps=1/4,scale=480:-1,drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.7" -q:v 4 frames/f_%04d.jpg

# full-res frame at a chosen second (from fps-filter sheets, the real moment is ~2s after the label)
ffmpeg -ss 712 -i work/video.mp4 -frames:v 1 -q:v 2 full/t0712.jpg
```

Then crop the useful part with PIL (e.g. the screen area right of a webcam bubble) and combine with `images.py row`.

## 2. YouTube thumbnails

```bash
curl -s -o thumb.jpg "https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg"   # falls back to hqdefault.jpg
```
Find a channel's top videos (for proof grids):
```bash
yt-dlp --flat-playlist --print "%(view_count)s | %(id)s | %(title)s" "https://www.youtube.com/channel/<CHANNEL_ID>/videos" | sort -t'|' -k1 -nr | head
yt-dlp --flat-playlist --print "%(id)s | %(title)s | %(channel)s | %(view_count)s" "ytsearch4:<query>"
```

## 3. Client channel logos (avatars)

`image-scripts/shared/client_logos.sh`: video id to channel id with `yt-dlp --print channel_id`, then the `avatar_uncropped` thumbnail from the channel's playlist JSON, cropped to a circle with PIL. Nexlev `youtube_channel_about` also returns avatar URLs and exact subscriber counts.

## 4. MCP research tools

| Tool | What it gives |
|---|---|
| Subscribr admin **Strategy_Search** | Expert creator advice with source video ids (20+ queries per guide, cited by creator name) |
| **Nexlev** MCP | `youtube_search`, `youtube_video_details`, `get_video_transcript`, `youtube_channel_about`, niche finder (RPM by niche, outlier scores), `get_video_rpm`, `faceless_outliers_videos`, `watch_tiktok_video_and_ask` |
| **vidIQ** MCP | keyword volume and competition, `vidiq_instagram_tiktok_outlier_search`, `vidiq_watch_shortform_content`, earnings calculator |
| **Claude in Chrome** | Google Drive upload, Docs conversion, contents page, reading private Google Docs |

Every number quoted in a guide is saved with its source and date in that guide's `work/RESEARCH.md`.

## 5. Other image sources

- **Case study PDFs / Gamma**: `images.py extract-pdf SRC.pdf OUT/`
- **Course decks (PPTX)**: `images.py extract-pptx SRC.pptx OUT/`, and Keynote slide renders with `images.py slides-keynote` for diagram slides
- **Cleared proof screenshots**: your own proof folder (only items marked public in its index)
- **Amazon listing galleries**: product-in-use shots for the gear guide
- **Charts**: matplotlib from Nexlev / vidIQ data (white background, readable on a phone)
- **Diagrams**: `flow()` in `builders/docbuilder_v3.py` draws black-line step boxes with arrows

## 6. Image rules

- No text labels or captions on images. The images speak for themselves.
- No accent colours, cyan lines or coloured boxes. Tables and diagrams use hard black lines.
- Compress to max 1600 px wide JPEG. A Google Drive upload through the Chrome file input must be under 10 MB.
- Read every image (contact sheet) before using it, to confirm it shows what the copy says.
