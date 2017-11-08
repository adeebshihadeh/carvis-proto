


class Bluetooth:

  profiles = []
  known_devices = []

  def discover(self):
    return None

  def get_state(self):
    return "bluetooth ok"

  def handle_input(self, input):
    return ""

  def __init__(self):
    return None


class BluetoothConnection:

  profiles = []
  addr = ""

  def connect(self):
    return 0

  def disconnect():
    return 0

  def handle_input(self, input):
    return ""

  def __init__(self, addr, type):
    return None