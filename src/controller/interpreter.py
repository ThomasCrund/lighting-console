from abc import ABC, abstractmethod
from src.artnet import ArtnetChannel, ArtnetManager
from typing import List

# A object which links physical inputs with output channels
class Interpreter(ABC):
  
  def __init__(self, channels: List[ArtnetChannel]) -> None:
    self._channels = channels

  @abstractmethod
  def interpret_hal(self, hal_data: dict, artnet: ArtnetManager):
    pass

  def get_channels(self):
    return self._channels
  
  @abstractmethod
  def enable(self):
    pass

  @abstractmethod
  def deactivate(self):
    pass