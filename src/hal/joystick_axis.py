
from src.hal.Input import Input

class JoystickAxis(Input):
  
  def __init__(self, inputId, initial_value) -> None:
    super().__init__(inputId, "joystick_axis")
    self.value = initial_value
    self.changed = False
    self.mid_value = 1024 / 2

  def set_value(self, value):
    self.value = value - self.mid_value
    self.changed = True
  
  def get_value(self):
    self.changed = False
    return self.value
  
  def get_changed(self):
    return self.changed
  
  def get_value_silent(self):
    return self.value
  
  def get_id(self):
    return self.id
  
  def check_update(self):
    pass
  
