import asyncio
import pytest
from src.artnet import ArtnetManager, ArtnetReceiver, ArtnetSender, ArtnetChannel
from src.util.ip import calculate_broadcast_address

class TestManager:
  
  def test_create_manager(self):
    receiver = ArtnetReceiver(5)
    sender = ArtnetSender(5, calculate_broadcast_address("255.255.255.0"))
    manager = ArtnetManager(receiver, sender)
    assert manager.get_receiver() == receiver
    assert manager.get_sender() == sender

class TestChannel:
  
  def test_create_channel(self):
    channel = ArtnetChannel(1, "channel1")
    assert channel.__class__.__name__ == "ArtnetChannel"
    assert channel.get_channel_id() == "channel1"
    assert channel.get_channel_num() == 1

class TestSendAndReceive:
  
  @pytest.mark.asyncio
  async def test_basic(self):
    loop = asyncio.get_event_loop()

    receiver = ArtnetReceiver(5)
    sender = ArtnetSender(5, "127.255.255.255")

    task = loop.create_task(sender.run())
    sender.set_channel_value(1, 100)

    await asyncio.sleep(0.1)

    assert receiver.get_channel_value(1) == 100
    
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)
    print("end")

  @pytest.mark.asyncio
  async def test_multiple(self):
    loop = asyncio.get_event_loop()

    receiver = ArtnetReceiver(2)
    sender = ArtnetSender(2, "127.255.255.255")

    task = loop.create_task(sender.run())

    sender.set_channel_value(1, 100)
    sender.set_channel_value(2, 200)

    await asyncio.sleep(0.1)
    assert receiver.get_channel_value(1) == 100
    assert receiver.get_channel_value(2) == 200
    
    sender.set_channel_value(1, 50)

    await asyncio.sleep(0.1)
    assert receiver.get_channel_value(1) == 50
    
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)
    print("end")