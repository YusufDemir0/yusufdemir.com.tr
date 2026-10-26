#!/usr/bin/env bash
# Omni klibini siteye hazırlar: yeşil perdeyi siler, gerçek panel görüntüsünün (panel.png) üstüne bindirir,
# A4 sahne alanına kırpar, son yarım saniyede kalan külü siler ve hafif bir MP4 + poster üretir.
#   bash _build/video/isle.sh _build/video/klipler/yanma-a.mp4
set -euo pipefail
cd "$(dirname "$0")"
IN="$(realpath "$1")"
OUT=../../assets/video
mkdir -p "$OUT"

# Sahne A4 (210x297); kare 9:16 ve kâğıt dikeyde ortalı
CROP='crop=iw:trunc(iw*297/210/2)*2:0:(ih-iw*297/210)/2'
# Plaka (panel.png) sahnenin masaüstü genişliğinde: 440 css px x2
W=880
H=1244

ffmpeg -y -loglevel error \
  -loop 1 -i panel.png -i "$IN" \
  -filter_complex "\
    [0:v]scale=${W}:${H},format=rgba[bg];\
    [1:v]${CROP},scale=${W}:${H},chromakey=0x00b140:0.16:0.06,despill=type=green,format=rgba,fade=t=out:st=4.2:d=0.55:alpha=1[fg];\
    [bg][fg]overlay=shortest=1,format=yuv420p[v]" \
  -map "[v]" -an -c:v libx264 -preset slow -crf 26 -movflags +faststart "$OUT/yanma.mp4"

ffmpeg -y -loglevel error -i "$OUT/yanma.mp4" -frames:v 1 -q:v 3 "$OUT/yanma-poster.jpg"
ls -la "$OUT"
