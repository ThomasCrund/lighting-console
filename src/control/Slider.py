
from src.control.Input import Input

class Slider(Input):
  
  def __init__(self, inputId, initial_value) -> None:
    super().__init__(inputId, "slider")
    self.value = initial_value

  def set_value(self, value):
    self.value = value
  
  def get_value(self):
    return self.get_value
  
  def get_value_silent(self):
    return self.get_value
  
  def get_id(self):
    return self.id
  
  def check_update(self):
    pass
  
