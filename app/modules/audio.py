import subprocess
from subprocess import call

class Audio:
  playing = False
  sp_cmd = "echo"

  def get_state(self):
    state = {
      "paused": False,
      "song": {}
    }
    return state

  def handle_input(self, input):
    if "play" in input:
      call([self.sp_cmd, 'play'])
    elif "pause" in input:
      call([self.sp_cmd, 'pause'])
    elif "previous" in input:
      call([self.sp_cmd, 'previous'])
    elif "next" in input:
      call([self.sp_cmd, 'next'])

  def __init__(self):
    return None