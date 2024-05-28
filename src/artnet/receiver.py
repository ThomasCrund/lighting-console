import python_artnet as Artnet

class ArtnetReceiver:
  
  def __init__(self, universe_num) -> None:
    self._artNet = Artnet.Artnet()
    self._last_packet = None
    self._universe_num = universe_num

  def get_channel_value(self, channel_num):
    artnet_packet = self._artNet.readBuffer()[self._universe_num]
    if artnet_packet == None: return 0
    print(artnet_packet.data, channel_num)
    if artnet_packet.data == None: return 0
    if artnet_packet.data[channel_num - 1] == None: return 0
    self._last_packet = artnet_packet
    return artnet_packet.data[channel_num - 1]

