import requests


BOT_TOKEN = '# Replace with your actual Bot Token'

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(url)

print(response.json())
