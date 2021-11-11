import keyboard

keyboard.hook(lambda k: print(k.to_json()))
keyboard.wait()