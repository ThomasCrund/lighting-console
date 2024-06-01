
from src.hal.ControlInterface import ControlInterface
from src.hal.Button import Button
from src.hal.Slider import Slider

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
        "value": False,
        "changed": False
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
        "value": True,
        "changed": True
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
        "value": True,
        "changed": True
      }
    }
    assert interface.get_updates() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": False,
        "changed": False
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
        "value": True,
        "changed": True
      }
    }
    assert interface.get_updates_silent() == {
      "button1": {
        "type": "button",
        "id": "button1",
        "value": True,
        "changed": True
      }
    }

class TestSlider:

  def test_add_to_interface(self):
    interface = ControlInterface()
    assert interface.__class__.__name__ == "ControlInterface"
    interface.add_input(Slider("slider1", 0))
    assert interface.get_inputs() == ["slider1"]

  def test_check_get_initial_value(self):
    interface = ControlInterface()
    interface.add_input(Slider("slider1", 0))
    assert interface.get_updates() == {
      "slider1": {
        "type": "slider",
        "id": "slider1",
        "value": 0,
        "changed": False
      }
    }

  def test_check_get_valuee(self):
    interface = ControlInterface()
    slider = Slider("slider1", 0)
    interface.add_input(slider)
    slider.set_value(129)
    assert interface.get_updates() == {
      "slider1": {
        "type": "slider",
        "id": "slider1",
        "value": 129,
        "changed": True
      }
    }
    assert interface.get_updates() == {
      "slider1": {
        "type": "slider",
        "id": "slider1",
        "value": 129,
        "changed": False
      }
    }
