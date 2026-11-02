#!/bin/bash
set -e
I=~/.claude/skills/lead-magnet-doc/scripts/images.py
T=/Users/bryanng/lead_magnets/NICHE/work/thumbs
O=/Users/bryanng/lead_magnets/NICHE/img
cd $T
python3 $I row $O/hero.jpg 360 T9tnDlEvlQg.jpg UvR1iyfzq4g.jpg gQkHA9DZuxk.jpg aHk7i-B6N-g.jpg 7JDgHvgWsZo.jpg _r9xxRWe2nQ.jpg --cols 3
python3 $I row $O/thumbs_business_rpm.jpg 360 T9tnDlEvlQg.jpg UvR1iyfzq4g.jpg _r9xxRWe2nQ.jpg RJ-ZfgbDa4U.jpg qN95TmywOko.jpg 2TxKwffQdfo.jpg --cols 3
python3 $I row $O/thumbs_entertainment_rpm.jpg 360 Hztf3WSRRck.jpg e7-Y7Hs7Dqw.jpg 6YdXp7Dr0RI.jpg lXF_squiTr4.jpg mFpDyPcWw2Q.jpg 4alYTXo3Iro.jpg --cols 3
python3 $I row $O/thumbs_money_property_rpm.jpg 360 fKkyLwNiQ1Q.jpg DWgUYdqZxe8.jpg gQkHA9DZuxk.jpg K3dzok7_ZbI.jpg iVQhkDZS_Tk.jpg aE1rh-U6zsM.jpg --cols 3
python3 $I row $O/thumbs_service_outliers.jpg 360 yN8fZcWu5fM.jpg aHk7i-B6N-g.jpg 7JDgHvgWsZo.jpg 1a0lVireAKg.jpg K3dzok7_ZbI.jpg uXftiLYEBW8.jpg --cols 3
python3 $I row $O/check2_top_results.jpg 360 y2-fP6LiIa8.jpg WWb7rT8lFtw.jpg 2ZfPY0oZDKE.jpg
python3 $I row $O/check3_hubspot_outlier.jpg 420 T9tnDlEvlQg.jpg RJ-ZfgbDa4U.jpg
python3 $I row $O/bryan_course_thumb.jpg 500 qdE8FKQC_Vg.jpg
python3 $I row $O/thumbs_lawyer_doctor.jpg 400 aHk7i-B6N-g.jpg 7JDgHvgWsZo.jpg PBzmMvmG5Oo.jpg
for f in $O/*.jpg; do python3 $I compress "$f" "$f" 1600; done
ls -la $O
