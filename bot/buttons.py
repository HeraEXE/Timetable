from telebot.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button_1 = KeyboardButton('🌝ПАРЫ СЕГОДНЯ')
buttons_2 = KeyboardButton('🌚ПАРЫ ЗАВТРА')
keyboard.add(button_1, buttons_2)