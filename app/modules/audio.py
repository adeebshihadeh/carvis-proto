import subprocess
from subprocess import call

class Audio:
  playing = False
  sp_cmd = "sp"

  def get_state(self):
    state = {
      "paused": True,
      "song": {}
    }
    song = subprocess.check_output([self.sp_cmd, 'metadata'])
    if "trackid" in song:
      song = song.splitlines()
      for line in song:
        state["song"][line.split('|', 1)[0]] = line.split('|', 1)[1]

    return state

  def handle_input(self, input):
    if "play" in input:
      call([self.sp_cmd, 'play'])
    elif "pause" in input:
      call([self.sp_cmd, 'pause'])
    elif "previous" in input:
      call([self.sp_cmd, 'prev'])
    elif "next" in input:
      call([self.sp_cmd, 'next'])

  def __init__(self):
    return None
