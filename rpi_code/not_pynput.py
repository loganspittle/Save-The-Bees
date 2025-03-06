import keyboard

def on_key_event(event):
    print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")

# Register a callback for key events
keyboard.on_press(on_key_event)
keyboard.on_release(on_key_event)

# Add a hotkey
keyboard.add_hotkey('ctrl+alt+p', lambda: print("CTRL+ALT+P Pressed!"))

# Add an abbreviation
keyboard.add_abbreviation("@email", "example@email.com")

print("Press 'esc' to exit...")
keyboard.wait('esc')

# Clean up
keyboard.unhook_all()
