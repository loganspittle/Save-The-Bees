import tkinter as tk
import threading

class ArrowButtonApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        
        # Key state variables
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.center_pressed = False
        
        self.setup_ui()

    def setup_ui(self):
        # Center button
        button = tk.Button(self.root, text="Click me!", command=lambda: self.button_pressed("Center"))
        button.place(relx=0.5, rely=0.5, anchor="center")

        # Arrow buttons
        up_button = tk.Button(self.root, text="↑", command=lambda: self.button_pressed("Up"))
        up_button.place(relx=0.5, rely=0.15, anchor="center")

        down_button = tk.Button(self.root, text="↓", command=lambda: self.button_pressed("Down"))
        down_button.place(relx=0.5, rely=0.85, anchor="center")

        left_button = tk.Button(self.root, text="←", command=lambda: self.button_pressed("Left"))
        left_button.place(relx=0.15, rely=0.5, anchor="center")

        right_button = tk.Button(self.root, text="→", command=lambda: self.button_pressed("Right"))
        right_button.place(relx=0.85, rely=0.5, anchor="center")

        # Bind keys for arrow key presses and releases
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)

    def on_key_press(self, event):
        self.update_key_state(event.keysym, True)

    def on_key_release(self, event):
        self.update_key_state(event.keysym, False)

    def update_key_state(self, key, state):
        if key in ('Up', 'Down', 'Left', 'Right'):
            setattr(self, f"{key.lower()}_pressed", state)
        elif key == 'space':
            self.center_pressed = state

    def button_pressed(self, direction):
        self.update_key_state(direction, True)
        # Simulate key release after a short delay
        self.root.after(100, lambda: self.update_key_state(direction, False))

    def is_key_pressed(self, key):
        return getattr(self, f"{key.lower()}_pressed", False)

    def run(self):
        self.root.mainloop()

    def start_threaded(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True  # This allows the thread to exit when the main program does
        thread.start()
        return thread

# # Usage example:
# if __name__ == "__main__":
#     app = ArrowButtonApp()
#     app.run()
