import telebot
from handlers import register_handlers

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)


bot.polling(none_stop=True)
