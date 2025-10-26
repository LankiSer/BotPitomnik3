from telebot import TeleBot
from keyboards import main_menu, menu_dogs, menu_cats, back_to_main
from texts import CALL_TEXT


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Главное меню:", reply_markup=main_menu())

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == 'back':
            bot.send_message(call.message.chat.id, "Главное меню", reply_markup=main_menu())
        elif call.data == 'menu_cats':
            bot.send_message(call.message.chat.id, "Породы кошек:", reply_markup=menu_cats())
        elif call.data == 'menu_dogs':
            bot.send_message(call.message.chat.id, "Породы собак:", reply_markup=menu_dogs())
        elif call.data in CALL_TEXT:
            bot.send_message(call.message.chat.id, CALL_TEXT[call.data], reply_markup=back_to_main())
