from typing import List
from src.controller.interpreter import Interpreter
from src.artnet import ArtnetChannel

class Fixture:
  
  def __init__(self) -> None:
    self._channels: List[ArtnetChannel] = []
    self._interpreters: List[Interpreter] = []

  def add_channel(self, channel: ArtnetChannel):
    if not channel in self._channels:
      self._channels.append(channel)

  def add_interpreter(self, interpreter: Interpreter):
    if interpreter in self._interpreters:
      raise Exception("Adding an interpreter which already exists")
    for channel in self._interpreters.get_channels():
      if not channel in self._channels:
        raise Exception("Adding an interpreter to fixture for which the channel does not exist")
    self._interpreters.append(interpreter)

  def remove_interpreter(self, interpreter: Interpreter):
    if interpreter in self._interpreters:
      self._interpreters.remove(interpreter)

  def get_channels(self):
    return self._channels
  
  def get_interpreters(self):
    return self._interpreters