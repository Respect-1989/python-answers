# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:52:04 2022

@author: Proger
"""

from transliterate import to_cyrillic,to_latin
import telebot

TOKEN='5266736184:AAGZLQcQfOB4UGiRyrQNlBeLgKKFPMhYC4E'
bot = telebot.TeleBot( TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalom alaykum, Xush kelibsiz!"
    answer += "\nMatn kiriting:"
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text  
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)    
    bot.reply_to(message, answer(msg))

bot.infinity_polling()
