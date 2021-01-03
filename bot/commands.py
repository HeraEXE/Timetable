from datetime import datetime, timedelta
from __main__ import bot
from dicts import LESSONS, FUNCS
from buttons import keyboard

utc = timedelta(hours=4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '👁👁', reply_markup=keyboard)
    bot.delete_message(message.chat.id, message.id)



@bot.message_handler(commands=['today'])
def today(message):
    date = str((datetime.today() + utc).strftime('%A'))
    bot.send_message(message.chat.id, LESSONS.get(date))
    bot.delete_message(message.chat.id, message.id)



@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    date = str((datetime.today() + utc + timedelta(days=1)).strftime('%A'))
    bot.send_message(message.chat.id, LESSONS.get(date))
    bot.delete_message(message.chat.id, message.id)



@bot.message_handler(content_types=['text'])
def translate(message):
    func = FUNCS.get(message.text)
    if func is not None:
        eval(func)
    else:
        bot.delete_message(message.chat.id, message.id)