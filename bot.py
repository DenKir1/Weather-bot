import json
import telebot
import requests
from config import tokenTele, weathertoken

bot = telebot.TeleBot(tokenTele)
API = weathertoken


@bot.message_handler(command=["start"])
def start(message):
	bot.send_message(message.chat.id, "message type here")


@bot.message_handler(content_types=['text'])
def get_weather(message):
	city = message.text.strip().lower()
	res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
	if res.status_code == 200:
		data = json.loads(res.text)
		temp = data['main']['temp']
		bot.reply_to(message, f'weather is: {temp}')


		#image = 'sunny.png' if temp > 5.0 else 'sun.png'
		#file = open('./' + image, 'rb')
		#bot.send_photo(message.chat_id, file)
	else:
		bot.reply_to(message, 'city unaproove')

bot.polling(none_stop=True)
