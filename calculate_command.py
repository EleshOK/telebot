import calculator

SEND_OPERATOR = 'Введите оператор'
SEND_NUMBER_ONE = 'Введите первое число'
SEND_NUMBER_TWO = 'Введите второе число'
INCORRECT_DATA = 'Некоректно введены данные!'
NEXT_OPERATOR = 'Введите оператор если желаете продолжить'

class CalculateCommand:
    def __init__(self):
        self.calc_object = calculator.Calculator()
    
    def start_calc(self):
        return SEND_NUMBER_ONE

    def calculate(self, message_text):
        if self.calc_object:
            if calculator.convert(message_text):
                self.calc_object.set_numbers(message_text)

            elif message_text == '+' or message_text == '-' or message_text == '*' or message_text == '/':
                self.calc_object.set_operator(message_text)

            else:
                return INCORRECT_DATA

            if len(self.calc_object.values) == 0:
                return SEND_NUMBER_ONE

            elif len(self.calc_object.values) == 1:
                return SEND_OPERATOR

            elif len(self.calc_object.values) == 2:
                return SEND_NUMBER_TWO


            elif len(self.calc_object.values) == 3:
                text = f"{''.join(self.calc_object.values)} = "
                return text + str(self.calc_object.calculate()) + NEXT_OPERATOR
                