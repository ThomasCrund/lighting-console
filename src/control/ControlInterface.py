from typing import List
from src.control.Input import Input

class ControlInterface:
  
  def __init__(self) -> None:
    self.inputs: List[Input] = []
  
  def get_updates(self) -> dict:
    result = {}
    for inputItem in self.inputs:
      result[inputItem.get_id()] = inputItem.to_object()
    return result
  
  def get_updates_silent(self) -> dict:
    result = {}
    for inputItem in self.inputs:
      result[inputItem.get_id()] = inputItem.to_object_silent()
    return result
  
  def check_update(self):
    for inputItem in self.inputs:
      inputItem.check_update()