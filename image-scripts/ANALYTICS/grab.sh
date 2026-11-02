#!/bin/bash
# usage: grab.sh video.mp4 outprefix t1 t2 ...
v=$1; p=$2; shift 2
for t in "$@"; do ffmpeg -loglevel error -y -ss $t -i $v -frames:v 1 -q:v 2 ${p}_$t.jpg; done
