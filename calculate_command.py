def calculate(message, calc_obj):
    if len(calc_obj.values) == 1:
        bot.send_message(message.chat.id, 'Введите оператор')
    if len(calc_obj.values) == 2:
        bot.send_message(message.chat.id, 'Введите второе число')
    if calculator.convert(message.text):
        calc_obj.set_numbers(message.text)
    else:
        if message.text == '+' or message.text == '-' or message.text == '*' or message.text == '/':
            calc_obj.set_operator(message.text)
    if len(calc_obj.values) == 3:
        calc_obj.calculate()
    bot.register_next_step_handler(message, lambda x: calculate(message, calc_obj))