
from src.control.Input import Input

class Button(Input):
  
  def __init__(self, buttonId) -> None:
    super().__init__(buttonId, "button")
    self.update = False
    self.pressed = False


  def set_value(self, value):
    if value == True and self.pressed == False:
      self.update = True
    self.pressed = value
  
  def get_value(self):
    if self.update:
      self.update = False;
      return True
    return False
  
  def get_value_silent(self):
    return self.pressed
  
  def check_update(self):
    pass