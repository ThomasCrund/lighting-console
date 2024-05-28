import asyncio
from pyartnet import ArtNetNode

class ArtnetSender:
  
  def __init__(self, universe_num: int, send_address) -> None:
    self._universe_num = universe_num
    self._send_address = send_address
    self._channels = {}
    self._node = None
    self._universe = None
    self._set_requests = []
    self._stop = False

  def set_channel_value(self, channel_num, value):
    self._set_requests.append({"channel_num": channel_num, "value": value})

  async def update_channel_data(self):
    print("Update Channel Data:", len(self._set_requests))
    while len(self._set_requests) != 0:
      channel_num = self._set_requests[0]["channel_num"]
      value = self._set_requests[0]["value"]
      if not str(channel_num) in self._channels:
        self._channels[str(channel_num)] = self._universe.add_channel(channel_num, 1, str(channel_num))
      print(self._universe._channels, str(channel_num), "set", [value])
      self._channels[str(channel_num)].set_fade([value], 0)
      await self._channels[str(channel_num)]
      self._set_requests.pop(0)

  async def run(self):
    self._node = ArtNetNode(self._send_address, 6454)
    print(self._send_address)
    self._universe = self._node.add_universe(self._universe_num)
    while True:
      await self.update_channel_data()
      await asyncio.sleep(0.05)

  def start(self):
    print("start")
    asyncio.run(self.method())
