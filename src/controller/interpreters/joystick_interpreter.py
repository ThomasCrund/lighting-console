
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

    self._pan_position = 0
    self._tilt_position = 0

  def update_from_artnet(self, artnet: ArtnetManager):
    self._pan_position = self.get_channels()[0].get_input_value(artnet) + self.get_channels()[1].get_input_value(artnet) / 255
    self._tilt_position = self.get_channels()[2].get_input_value(artnet) + self.get_channels()[3].get_input_value(artnet) / 255
    pass

  def enable(self, artnet: ArtnetManager):
    self.update_from_artnet(artnet)

  def update_artnet(self, artnet: ArtnetManager):
    self.get_channels()[0].set_output_value(artnet, math.floor(self._pan_position))
    self.get_channels()[1].set_output_value(artnet, math.floor((self._pan_position % 1) * 255))
    self.get_channels()[2].set_output_value(artnet, math.floor(self._tilt_position))
    self.get_channels()[3].set_output_value(artnet, math.floor((self._tilt_position % 1) * 255))

  def set_position(self, artnet: ArtnetManager, new_pan_position, new_tilt_position):
    self._pan_position = new_pan_position
    self._tilt_position = new_tilt_position
    self.update_artnet(artnet)

  def interpret_hal(self, hal_data: dict, artnet: ArtnetManager):
    if ((self._pan_input_id() in hal_data and hal_data[self.self._pan_input_id()].type == "joystick_axis") and
        (self._tilt_input_id() in hal_data and hal_data[self.self._tilt_input_id()].type == "joystick_axis")):
      if (hal_data[self.self._pan_input_id()].value <= 0.005 and hal_data[self.self._pan_input_id()].changed 
          and hal_data[self.self._tilt_input_id()].value <= 0.005 and hal_data[self.self._tilt_input_id()].changed):
        self.update_from_artnet(artnet)

      pan_adjust = self._input_mapping(hal_data[self.self._pan_input_id()].value) * self._change_rate
      tilt_adjust = self._input_mapping(hal_data[self.self._tilt_input_id()].value) * self._change_rate

      new_pan_position = self._pan_position + pan_adjust
      new_tilt_position = self._tilt_position + tilt_adjust

      if (new_pan_position < 0): new_pan_position = 0
      if (new_pan_position >= 256): new_pan_position = 255.999
      if (new_tilt_position < 0): new_tilt_position = 0
      if (new_tilt_position >= 256): new_tilt_position = 255.999

      self.set_position(artnet, new_pan_position, new_tilt_position)


