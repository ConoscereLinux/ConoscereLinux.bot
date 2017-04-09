import telepot
import dataset
from config import api_keys

from time import sleep

bot = telepot.Bot(api_keys['telegram'])

def handler(msg):
	message = msg
	chat_id = message['from']['id']
	bot.sendMessage(chat_id, message)

bot.message_loop(handler)

while True:
	sleep(10)
	
	
