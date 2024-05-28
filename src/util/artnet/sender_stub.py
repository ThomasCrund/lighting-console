
class SenderStub:
  
  def __init__(self) -> None:
    self._last_packet = None
    self.values = [0] * 512

  def get_channel_value(self, channel_num):
    return self.values[channel_num]
  
  def set_channel_value(self, channel_num, value):
    self.values[channel_num] = value
  
    

