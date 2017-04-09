import telepot
import dataset

from time import sleep

bot = telepot.Bot("379100520:AAF_-BKVmVmky2ZVDJIoeWAJNKtbDxWTVnY")

def handler(msg):
	message = msg
	chat_id = message['from']['id']
	bot.sendMessage(chat_id, message)

bot.message_loop(handler)

while True:
	sleep(10)
	
	
