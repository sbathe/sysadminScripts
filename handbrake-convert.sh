#!/bin/bash
set -x
audio=0
outdir=`pwd`
# preset="HQ 2160p60 4K HEVC Surround"
preset="Fast 2160p60 4K HEVC"

while getopts ":n:o:a" opt; do
  case $opt in
    n)
      name="${OPTARG}"
      ;;
    o)
      outdir="${OPTARG}"
      ;;
    a)
       audio=1
       ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

# Create output directory
mkdir -p "${outdir}/${name}"
#read handbrake's stderr into variable
HandBrakeCLI -i /dev/sr0 -t 0 2>&1 | tee /tmp/hb-out

#parse the output to get titles and chapters
titles="$(grep -a 'scan: title' /tmp/hb-out | grep -v angle | wc -l)"
size=

#loop through titles
for i in $(seq $titles); do
  # get chapters in this title
	chapters="$(grep -a 'scan: title' /tmp/hb-out | grep -v angle | head -$i | tail -1 | gawk '{print $(NF-1)}')"
	for j in $(seq $chapters); do
	  #echo "HandBrakeCLI --input /dev/sr0 --title $i --chapter $j --min-duration 60 --previews 10:1 --preset "Chromecast 1080p30 Surround" -o "${outdir}/${name}_${i}_${j}.mp4" --format av_mp4 --optimize"
    echo "Writing Title ${i} Chapter ${j} at ${outdir}/${name}/${i}_${j}.mp4..."
	  HandBrakeCLI --input /dev/sr0 --title $i --chapter $j --min-duration 60 --previews 10:1 --preset "$preset" -E copy:ac3 -o "${outdir}/${name}/${i}_${j}.mp4" --format av_mp4 --optimize
	done
done

# Now, convert all vidoes to audio if we have set that
# We assume that stream 1 is the stereo stream and that is what we will copy
if [ "$audio" -eq "1" ]; then
  mkdir -p "${HOME}/Music/${name}"
  for f in $(find ${outdir}/${name} -name '*.mp4'); do
     fn="$(basename $f)"
     nn="$(echo $fn | sed 's/mp4/ogg/g')"     
    ffmpeg -i "${f}" -map 0:1 -c:a:1 copy "${HOME}/Music/${name}/${nn}"
  done
fi
