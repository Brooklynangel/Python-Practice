from pynput import keyboard
def on_press(key):
     print(key)
from pynput.keyboard import Listener
listener = keyboard.Listener(on_press=on_press
)
listener.start()
