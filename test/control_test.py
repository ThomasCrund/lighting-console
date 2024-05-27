
from src.control.ControlInterface import ControlInterface
from src.control.Button import Button

class TestInterface:
  
  def test_create(self):
    interface = ControlInterface()
    assert interface.__class__.__name__ == "ControlInterface"

  def test_get_empty_interface(self):
    interface = ControlInterface()
    assert interface.get_updates() == {}
    assert interface.get_updates_silent() == {}
    assert interface.get_inputs() == []

class TestButton:

  def test_add_to_interface(self):
    interface = ControlInterface()
    assert interface.__class__.__name__ == "ControlInterface"
    interface.add_input(Button("button1"))
    assert interface.get_inputs() == ["button1"]

  def test_check_pressed_not_pressed(self):
    interface = ControlInterface()
    interface.add_input(Button("button1"))
    assert interface.get_updates() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": False
      }
    }

  def test_check_pressed_when_pressed(self):
    interface = ControlInterface()
    button = Button("button1")
    interface.add_input(button)
    button.set_value(True)
    assert interface.get_updates() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": True
      }
    }

  def test_check_pressed_when_pressed_multiple(self):
    interface = ControlInterface()
    button = Button("button1")
    interface.add_input(button)
    button.set_value(True)
    assert interface.get_updates() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": True
      }
    }
    assert interface.get_updates() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": False
      }
    }

  def test_check_pressed_when_pressed_silent(self):
    interface = ControlInterface()
    button = Button("button1")
    interface.add_input(button)
    button.set_value(True)
    assert interface.get_updates_silent() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": True
      }
    }
    assert interface.get_updates_silent() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": True
      }
    }