import keyboard
import logging

logging.basicConfig(level=logging.DEBUG)

class KeyboardInterface:
    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.center_pressed = False

    def on_key_event(self, event):
        key = event.name
        is_press = event.event_type == 'down'
        logging.debug(f"Key {key} {'pressed' if is_press else 'released'}")
        
        if key == 'up':
            self.up_pressed = is_press
        elif key == 'down':
            self.down_pressed = is_press
        elif key == 'left':
            self.left_pressed = is_press
        elif key == 'right':
            self.right_pressed = is_press
        elif key == 'space':
            self.center_pressed = is_press

    def is_key_pressed(self, key):
        value = getattr(self, f"{key.lower()}_pressed", False)
        # Reset the value to False after reading
        setattr(self, f"{key.lower()}_pressed", False)
        return value

    def start(self):
        try:
            logging.debug("Starting keyboard listener")
            keyboard.on_press(self.on_key_event)
            keyboard.on_release(self.on_key_event)
        except Exception as e:
            logging.error(f"Error starting keyboard listener: {e}")

    def stop(self):
        try:
            logging.debug("Stopping keyboard listener")
            keyboard.unhook_all()
        except Exception as e:
            logging.error(f"Error stopping keyboard listener: {e}")
