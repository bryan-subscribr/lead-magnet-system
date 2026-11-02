#!/bin/bash
cd /Users/bryanng/lead_magnets/TIKTOK/img
IM=~/.claude/skills/lead-magnet-doc/scripts/images.py
python3 $IM row nav_pair.jpg 700 nav_short_pasta_src.jpg nav_long_thumb.jpg
python3 $IM row codie_vending_pair.jpg 700 codie_short_hook.jpg codie_vending_long_thumb.jpg
python3 $IM row codie_6biz_pair.jpg 700 codie_6biz_long_thumb.jpg codie_6biz_short.jpg
python3 $IM row simon_quit_pair.jpg 700 simon_quit_short.jpg simon_quit_long_thumb.jpg
python3 $IM row nav_short_beats.jpg 900 nav_short_open.jpg nav_short_part2.jpg nav_short_end.jpg
python3 $IM row nav_countdown.jpg 400 nav_long_3days.jpg nav_long_2days.jpg nav_long_clock24.jpg nav_long_50k.jpg --cols 2
python3 $IM row codie_short_beats.jpg 900 codie_short_hook.jpg codie_short_2100.jpg codie_short_cta.jpg
python3 $IM row hero.jpg 600 nav_short_pasta_src.jpg nav_long_thumb.jpg codie_short_hook.jpg codie_vending_long_thumb.jpg --cols 2
