import requests
import json


number = "917428428237"
message = "Hi!!"
MESSAGE_API = f"https://api.callmebot.com/whatsapp.php?phone={number}&text={message}&apikey=3367362"

response = requests.get(MESSAGE_API)
