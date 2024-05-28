
from src.artnet.manager import ArtnetManager

class ArtnetChannel:
  
  def __init__(self, channel_num, channel_id) -> None:
    self._fixture = None
    self._channel_num = channel_num
    self._channel_id = channel_id
    self.output_value = 0
  
  def get_channel_num(self):
    return self._channel_num
  
  def get_channel_id(self):
    return self._channel_id
  
  def set_output_value(self, artnet: ArtnetManager, value):
    assert value >= 0
    assert value <= 255
    artnet.get_sender().set_channel_value(self.get_channel_num(), value)
    self.output_value = value

  def get_output_value(self):
    return self.output_value

  def get_input_value(self, artnet: ArtnetManager):
    return artnet.get_receiver().get_channel_value(self.get_channel_num())
  