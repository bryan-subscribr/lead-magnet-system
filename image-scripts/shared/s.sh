for q in "Inayah McMillan" "Ethan Garland trading" "Scott Taylor webinar youtube" "Fiction Profits Academy how to start a KDP business" "Chamath Palihapitiya" "Clover Trading"; do
yt-dlp --flat-playlist --print "%(id)s | %(title)s | %(channel)s | %(view_count)s" "ytsearch4:$q" 2>/dev/null; echo "--"; done
