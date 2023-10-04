import datetime
import json
import telebot
import requests
from config import tokenTele, weathertoken

bot = telebot.TeleBot(tokenTele)
API = weathertoken


@bot.message_handler(command=["start"])
def start(message):
	bot.send_message(message.chat.id, "Приветствуем в боте погоды Кирдянкиных! Напишите название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
	city = message.text.strip().lower()
	#res2 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API}")
	#lat = json.loads(res2.text)[0]["lat"]
	#lon = json.loads(res2.text)[0]["lon"]
	res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API}&units=metric&lang=ru")
	print(res.text)
	if res.status_code == 200:
		data = json.loads(res.text)
		coord = data["coord"]
		description = data["weather"][0]["description"]
		temp = data['main']['temp']
		temp_feel = data['main']['feels_like']
		pressu = data['main']['pressure']
		wind = data['wind']['speed']
		bot.reply_to(message, f'{description}, температура {temp} С, чувствуется как {temp_feel}, давление {pressu}, ветер {wind} м/с')


		#image = 'sunny.png' if temp > 5.0 else 'sun.png'
		#file = open('./' + image, 'rb')
		#bot.send_photo(message.chat_id, file)
	else:
		bot.reply_to(message, 'city unaproove')

bot.polling(none_stop=True)
