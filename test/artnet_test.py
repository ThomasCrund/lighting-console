import asyncio
import pytest
from src.artnet import ArtnetManager, ArtnetReceiver, ArtnetSender, ArtnetChannel
from src.util.ip import calculate_broadcast_address
from src.util.artnet.receiver_stub import ReceiverStub
from src.util.artnet.sender_stub import SenderStub
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

  @pytest.mark.asyncio
  async def test_basic(self):
    loop = asyncio.get_event_loop()

    receiver = ArtnetReceiver(5)
    sender = ArtnetSender(5, "127.255.255.255")
    manager = ArtnetManager(receiver, sender)
    channel = ArtnetChannel(5, "channel5")

    task = loop.create_task(sender.run())
  
    assert channel.get_input_value(manager) == 0
    channel.set_output_value(manager, 45)

    await asyncio.sleep(0.1)

    assert channel.get_input_value(manager) == 45
    
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)
    print("end")

  def test_channel_with_stubs(self):
    channel = ArtnetChannel(1, "channel1")
    receiver = ReceiverStub()
    sender = SenderStub()
    manager = ArtnetManager(receiver, sender)
    
    assert channel.get_input_value(manager) == 0
    channel.set_output_value(manager, 45)
    assert channel.get_input_value(manager) == 0
    assert sender.get_channel_value(1) == 45

    receiver.set_channel_value(1, 72)
    assert channel.get_input_value(manager) == 72
    assert channel.get_output_value() == 45

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