import socket
import time

class Connectivity:

  last_check = 0
  state = {}

  def get_state(self):
    if time.time() - self.last_check > 30: # only check every 30s
      self.last_check = time.time()
      self.state["internet_connected"] = self.internet_connected()
    return self.state

  def internet_connected(self):
    try:
      host = socket.gethostbyname("www.google.com")
      s = socket.create_connection((host, 80), 2)
      return True
    except:
       pass
    return False

  def __init__(self):
    return None