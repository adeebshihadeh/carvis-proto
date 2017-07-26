import os
from sys import platform as _platform

def handleCmd(cmd):
  if "roll-up" in cmd:
    if _platform == "linux" or _platform == "linux2":
      os.system("qdbus org.mpris.MediaPlayer2.spotify / org.freedesktop.MediaPlayer2.OpenUri https://open.spotify.com/track/7kClqlbpmpZmGMimROkvh6")
    elif _platform == "darwin":
      os.system("spotify play uri https://open.spotify.com/track/7kClqlbpmpZmGMimROkvh6")
    
    print "roll up!"