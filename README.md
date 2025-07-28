# spyking
This Python script is a basic keylogger designed to capture and record all keyboard activity on a system. It uses the pynput library to listen for keypress events and stores them in a log. Every 15 seconds, the log data is sent to a Telegram bot via the Telegram Bot API, allowing remote monitoring of the captured keystrokes in real-time. 
🔧 Main Features:
Captures all keyboard inputs, including special keys like Enter, Space, etc.

Uses threading to run a background reporter that sends logs every 15 seconds.

Sends data securely via HTTP POST requests to a specified Telegram chat.

Runs continuously and invisibly in the background.

📦 Technologies Used:
pynput: For detecting and recording keypresses.

requests: To send HTTP POST requests to the Telegram Bot API.

threading: To handle background execution without blocking keyboard capture.

⚠️ Disclaimer:
This script is for educational and ethical use only. Unauthorized use of keyloggers to monitor someone else's device without explicit consent is illegal and unethical. Always ensure compliance with local laws and obtain proper permission before deploying or testing this script.
