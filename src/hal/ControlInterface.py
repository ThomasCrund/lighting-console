from typing import List
from src.hal.Input import Input

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

  def add_input(self, deskInput: Input):
    self.inputs.append(deskInput)

  def get_inputs(self):
    return list(map(lambda deskInput: deskInput.get_id(), self.inputs))