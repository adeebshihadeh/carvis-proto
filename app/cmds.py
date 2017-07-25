import os

def handleCmd(cmd):
  if "roll-up" in cmd:
    # os.system("spotify play uri https://open.spotify.com/track/7kClqlbpmpZmGMimROkvh6")
    os.system("qdbus org.mpris.MediaPlayer2.spotify / org.freedesktop.MediaPlayer2.OpenUri https://open.spotify.com/track/7kClqlbpmpZmGMimROkvh6")
    
    print "roll up!"