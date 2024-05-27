
from src.control.Button import Input

class ButtonInput(Input):
  
  def __init__(self, buttonId) -> None:
    super().__init__(buttonId, False)

