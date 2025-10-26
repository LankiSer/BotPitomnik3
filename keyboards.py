from telebot import types

def main_menu():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Кошки', callback_data='menu_cats'))
    keyboard.add(types.InlineKeyboardButton('Собаки', callback_data='menu_dogs'))
    return keyboard

def menu_cats():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Сфинкс', callback_data='sphinks'))
    keyboard.add(types.InlineKeyboardButton('Аббиссинская', callback_data='abby'))
    keyboard.add(types.InlineKeyboardButton('Сиамская', callback_data='siams'))
    keyboard.add(types.InlineKeyboardButton('Вернуться', callback_data='back'))
    return keyboard

def menu_dogs():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Чихуахуа', callback_data='chihuahua'))
    keyboard.add(types.InlineKeyboardButton('Корги', callback_data='corgi'))
    keyboard.add(types.InlineKeyboardButton('Такса', callback_data='taksa'))
    keyboard.add(types.InlineKeyboardButton('Вернуться', callback_data='back'))
    return keyboard

def back_to_main():
    keyboard_main = types.InlineKeyboardMarkup()
    keyboard_main.add(types.InlineKeyboardButton('Вернуться', callback_data='back'))
    return keyboard_main