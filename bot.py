import telebot
from handlers import register_handlers

TOKEN = '8258963893:AAFIEwGQRAMA5c5hGd39BJOeHog6rErN-A0'
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

bot.polling(none_stop=True)