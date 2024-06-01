
from abc import ABC, abstractmethod

class Input(ABC):
  
  def __init__(self, inputId, inputType) -> None:
    super().__init__()
    self.id = inputId
    self.type = inputType

  def get_id(self):
    return self.id
  
  def get_type(self):
    return self.type

  @abstractmethod
  def set_value(self, value):
    pass
  
  @abstractmethod
  def get_value(self):
    pass
  
  @abstractmethod
  def get_changed(self):
    pass

  @abstractmethod
  def get_value_silent(self):
    pass
  
  @abstractmethod
  def check_update(self):
    pass

  def to_object(self):
    return {
      "type": self.get_type(),
      "id": self.get_id(),
      "changed": self.get_changed(),
      "value": self.get_value(),
    }
  
  def to_object_silent(self):
    return {
      "type": self.get_type(),
      "id": self.get_id(),
      "changed": self.get_changed(),
      "value": self.get_value_silent(),
    }