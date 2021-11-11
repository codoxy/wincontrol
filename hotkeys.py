import keyboard

MAPPING = [
    (79, "F1"),
    (80, "F2"),
    (81, "F3"),
    (75, "F4"),
    (76, "F5"),
    (77, "F6"),
    (71, "F7"),
    (72, "F8"),
    (73, "F9"),
]

def main():
    # mouse bindings
    keyboard.add_hotkey("home", lambda: print("home"), suppress=True)
    keyboard.add_hotkey("end", lambda: print("end"), suppress=True)
    keyboard.add_hotkey("page up", lambda: print("page up"), suppress=True)
    keyboard.add_hotkey("page down", lambda: print("page down"), suppress=True)
    # numpad keys
    for keycode, fkey in MAPPING:
        keyboard.add_hotkey(keycode, print, args=(fkey,), suppress=True)
    # wait forever
    keyboard.wait()

if __name__ == "__main__":
    main()
