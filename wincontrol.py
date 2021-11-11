import sys
import keyboard
from pywinauto.application import Application

class WinController:
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

    def __init__(self, pid):
        self.app = Application().connect(process=pid)
        self.window = self.app.top_window()

        # mouse bindings
        keyboard.add_hotkey("home", lambda: print("home"), suppress=True)
        keyboard.add_hotkey("end", lambda: print("end"), suppress=True)
        keyboard.add_hotkey("page up", lambda: print("page up"), suppress=True)
        keyboard.add_hotkey("page down", lambda: print("page down"), suppress=True)
        # numpad keys
        for keycode, fkey in self.MAPPING:
            keyboard.add_hotkey(keycode, self.forward, args=(fkey,), suppress=True)

    def forward(self, fkey):
        self.window.send_keystrokes("{%s}" % fkey)
    
    def listen(self):
        # wait forever
        keyboard.wait()

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print(f"Pass the process PID plz.\nUsage: {sys.argv[0]} PID")
        sys.exit(1)
    pid = int(sys.argv[-1])
    w = WinController(pid)
    w.listen()

if __name__ == "__main__":
    main()
