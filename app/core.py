# 


from modules import audio


class Core:
  modules = []
  update_function = None

  def get_state(self):
    for module in self.modules:
      print module.get_state()

  def set_update_function(self, func):
    self.update_function = func
    func("")

  def register_module(self, module):
    self.modules.append(module)
    module.__init__()

  def broadcast_input(self, input):
    for module in self.modules:
      module.handle_input(input)

  def handle_msg(self, msg):
    self.broadcast_input(msg)

  def __init__(self):
    return None

core = Core()
core.register_module(audio.Audio())