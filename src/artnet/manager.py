
from src.artnet.receiver import ArtnetReceiver
from src.artnet.sender import ArtnetSender

class ArtnetManager:
  
  def __init__(self, receiver: ArtnetReceiver, sender: ArtnetSender) -> None:
    self.receiver = receiver
    self.sender = sender

  def get_receiver(self):
    return self.receiver
  
  def get_sender(self):
    return self.sender
  
