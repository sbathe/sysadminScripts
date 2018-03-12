#!/usr/bin/python3
import subprocess
import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("-v", action="store_true", default=False, dest='verbose',
                    help="increase output verbosity")
parser.add_argument("-f", action="store", default="out", dest="pattern",
                    help="file name pattern")
args = parser.parse_args()

filename = args.pattern + '.ogg'
os.mkdir(args.pattern)
os.chdir(args.pattern)

def run_ffmpeg_command(cmd):
    run = subprocess.run(cmd, stderr=subprocess.PIPE ,stdout = subprocess.PIPE)
    s = run.stderr + run.stdout
    if run.returncode:
        return(False, s)
    else:
        return(True, s)

def validate_cmd(t):
    if t[0]:
        print("Success")
    else:
        print("Something is a miss. The command output is:\n{0}".format(t[1].decode("utf-8")))
        exit(1)

def get_chapter_lengths(filename='/dev/sr0'):
  ff = "ffprobe -f libcdio -i {0}".format(filename).split()
  k = run_ffmpeg_command(ff)
  validate_cmd(k)
  chaps = []
  str_out = k[1].decode("utf-8")
  for l in str_out.splitlines():
    if l.strip().startswith("Chapter"):
      chaps.append((l.strip().split()[3], l.strip().split()[5]))
  return chaps

def dump_audiocd(infile='/dev/sr0',outfile='out.ogg'):
  dumpcd = "ffmpeg -y -f libcdio -ss 0 -i {0} -codec:a libvorbis -qscale:a 10 {1}".format(infile,outfile).split()
  k = run_ffmpeg_command(dumpcd)
  return validate_cmd(k)

def split_file(chaps, infile='out.ogg', outpat='out-t'):
  c=1
  print(chaps)
  for e in chaps:
    start, end = e
    splitcmd = "ffmpeg -y -i {0} -acodec copy -ss {1} -to {2} {3}{4}.ogg".format(infile,start.strip(','),end,outpat,c).split()
    print("running {0}".format(splitcmd))
    k = run_ffmpeg_command(splitcmd)
    c+=1
  os.remove(infile)
  return print("All Done")

chaps = get_chapter_lengths()
dump_audiocd('/dev/sr0',filename)
file_pattern = args.pattern + '-t'
split_file(chaps,filename,file_pattern)
