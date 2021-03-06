import config
import telebot
import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)
#Создаем клавиатуру
menu = types.ReplyKeyboardMarkup( resize_keyboard=True)
#Создаем кнопку
btnUSD = types.KeyboardButton(text="🇺🇸 Доллар США")
btnEUR = types.KeyboardButton(text="🇪🇺 Евро")
btnGPT = types.KeyboardButton(text="Британский фунт")
btnСNY = types.KeyboardButton(text="Китайский юань")
btnCZK = types.KeyboardButton(text="Чешская крона")
#добавляем кнопку на клавиатуру
menu.add(btnUSD)
menu.add(btnEUR)
menu.add(btnGPT)
menu.add(btnCZK)
menu.add(btnСNY)
@bot.message_handler(commands=["start"])
def start(message):
	#reply_markup=menu - прикрепляем клавиатуру к сообщению
	bot.send_message(message.chat.id, "Выбери валюту:", reply_markup=menu)
#делаем реакцию на кнопку
@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=='🇪🇺 Евро')
def usd(message):
	text = "1 Евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=='Британский фунт')
def usd(message):
	text = "1 Британский фунт ="+str(rates['GBP'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=='Китайский юань')
def usd(message):
	text = "1 Китайский юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=='Чешская крона')
def usd(message):
	text = "1 Чешская крона"+str(rates['CZK'].rate)+"руб."
	bot.send_message(message.chat.id, text)


if __name__ == '__main__':
	bot.infinity_polling()