# imports

import telebot
from telebot import types
import config
from my_telebot import MyTelebot

# main

bot = telebot.TeleBot(config.get_token())
my_telebot = MyTelebot()

# functions

def generate_buttons(btns_names, markup):
    for btn_name in btns_names:
        markup.add(types.KeyboardButton(btn_name))
    return markup
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    generate_buttons(['info'], markup)
    bot.send_message(message.chat.id, "Привет, меня зовут Джон, и я являюсь твоим помощником. "+
    "Ознакомиться с моими возможностями можно нажав на кнопку 'info'.", reply_markup=markup)

# calculator

@bot.message_handler(commands=['calc'])
def calc_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    generate_buttons(['Да', 'Нет'], markup)
    bot.send_message(message.chat.id, 'Для работы калькулятора нужно ввести значения и оператор.')
    bot.send_message(message.chat.id, 'Готовы приступить?', reply_markup=markup)
    bot.register_next_step_handler(message, calc_answer)

def calc_answer(message):
    message_text = None
    if message.text == 'Да' and not my_telebot.calc_command:
        my_telebot.set_operation('Калькулятор')
        bot.send_message(message.chat.id, 'Введите первое число')
    if message_text != 'Да' or message_text != 'Нет' and not my_telebot.calc_command:
        markup = types.ReplyKeyboardMarkup(row_width=2)

# dollarex

@bot.message_handler(commands=['dollarex'])
def dollarex(message):
    pass

# info 

@bot.message_handler(content_types='text')
def show_info(message):
    if message.text == 'info':
        bot.send_message(message.chat.id, "Что я могу: \n/calc - посчитать пример, \n/dollarex - курс доллара.")
    if current_operation == 'Калькулятор':
        calc_obj = calculator.Calculator()
        bot.register_next_step_handler(message, lambda x: calculate(message, calc_obj))

bot.polling(none_stop=True)