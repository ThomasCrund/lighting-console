
from src.artnet import ArtnetManager, ArtnetReceiver, ArtnetSender, ArtnetChannel

class TestManager:
  
  def test_create_manager(self):
    receiver = ArtnetReceiver()
    sender = ArtnetSender()
    manager = ArtnetManager(receiver, sender)
    assert manager.get_receiver() == receiver
    assert manager.get_sender() == sender

class TestChannel:
  
  def test_create_channel(self):
    channel = ArtnetChannel(1, "channel1")
    assert channel.__class__.__name__ == "ArtnetChannel"
    assert channel.get_channel_id() == "channel1"
    assert channel.get_channel_num() == 1