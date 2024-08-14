# screenshot.py
import pyautogui
import time
import threading

def capture_screenshot():
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{int(time.time())}.png")
        time.sleep(60)  # Capture every 60 seconds

def start_screenshot_thread():
    screenshot_thread = threading.Thread(target=capture_screenshot)
    screenshot_thread.start()
