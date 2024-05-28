
from typing import List
from artnet import ArtnetChannel, ArtnetManager
from src.controller.interpreter import Interpreter
import math

class JoystickInterpreter(Interpreter):
  
  def __init__(self, pan_input_id: str, tilt_input_id: str, 
               pan_channel, pan_fine_channel, tilt_channel, tilt_fine_channel, 
               input_mapping = lambda x: math.pow(x, 2), change_rate = 1) -> None:
    super().__init__([pan_channel, pan_fine_channel, tilt_channel, tilt_fine_channel])
    self._pan_input_id = pan_input_id
    self._tilt_input_id = tilt_input_id
    self._input_mapping = input_mapping
    self._change_rate = change_rate

  def interpret_hal(self, hal_data: dict, artnet: ArtnetManager):
    if self.get_input_id() in hal_data and hal_data[self.get_input_id()].type == self.get_input_type():
      for channel in self.get_channels():
        channel.set_output_value(artnet, hal_data[self.get_input_id()].value)