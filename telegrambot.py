#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('id_owm', config_dict )
bot = telebot.TeleBot("token_telegram")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура сейчас в районе " + str(temp) + " градусов\n\n"

	if temp < -20:
                answer += "Сейчас очень холодно, одевайся потеплее!"
	elif temp < -10:
                answer += "Сейчас холодно, одевайся тепло"
	else:
		answer += "На улице лето!"
	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
