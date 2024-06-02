
from typing import List
from artnet import ArtnetChannel, ArtnetManager
from src.controller.interpreter import Interpreter

class SliderInterpreter(Interpreter):
  
  def __init__(self, input_id: str, channels: List[ArtnetChannel]) -> None:
    super().__init__(channels)
    self._input_id = input_id

  def interpret_hal(self, hal_data: dict, artnet: ArtnetManager):
    if self._input_id in hal_data and hal_data[self._input_id].type == "slider" and hal_data[self._input_id].changed == True:
      for channel in self.get_channels():
        channel.set_output_value(artnet, hal_data[self._input_id].value)