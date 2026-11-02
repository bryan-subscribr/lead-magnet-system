for pair in chamath:RWqB9eAKMx0 jordan:9SWaq5Eoak0 inayah:U81bsDC8oP0 ethan:1wohm6V3LMk fpa:7Uz7e9Cbyo0 clover:u4OAg30NbhA; do
n=${pair%%:*}; v=${pair#*:}
cid=$(yt-dlp --print channel_id "https://www.youtube.com/watch?v=$v" 2>/dev/null)
url=$(yt-dlp --flat-playlist --playlist-items 0 -J "https://www.youtube.com/channel/$cid" 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);t=[x for x in d.get('thumbnails',[]) if x.get('id')=='avatar_uncropped'];print(t[0]['url'] if t else '')")
echo "$n $cid $url"; [ -n "$url" ] && curl -s -o $n.jpg "$url"
done
