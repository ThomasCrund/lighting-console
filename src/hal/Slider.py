
from src.hal.Input import Input

class Slider(Input):
  
  def __init__(self, inputId, initial_value) -> None:
    super().__init__(inputId, "slider")
    self.value = initial_value
    self.changed = False

  def set_value(self, value):
    self.value = value
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
  
