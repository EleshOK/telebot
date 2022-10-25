
def convert(str_val):
    try:
        if float(str_val).is_integer():
            return int(str_val)
        else:
            return float(str_val)
    except ValueError:
        return False


class Calculator:
    def __init__(self):
        self.values = []
        self.operator = None
        self.exist_dot = False
        self.current_number = None

    def clean(self):
        self.values.clear()
        self.exist_dot = False
        self.operator = None
        self.update_text()

    def set_numbers(self, number):
        text_number = ''
        if self.operator == None:
            if len(self.values) <= 0:
                text_number = str(number)
                self.values.append(text_number)
            else:
                text_number = self.values[-1] + str(number)
                if self.exist_dot == True:
                    self.exist_dot = False
                self.values[-1] = text_number
        else:
            self.values.append(str(number))
            self.operator = None
        self.update_text()

    def update_text(self):
        if len(self.values) <= 0:
            self.label.configure(text='0')
            return

        text = ''
        for value in self.values:
            text = text + value

    def set_operator(self, operator):
        if len(self.values) == 3:
            self.calculate()
        if self.operator == operator:
            return
        if self.operator != None:
            self.operator = operator
            self.values[-1] = operator
            self.update_text()
            return
        self.operator = operator
        if self.exist_dot == True:
            self.values[-1] = self.values[-1] + 0
        self.values.append(operator)
        self.update_text()

    def set_point(self):
        if self.exist_dot == True:
            return
        if len(self.values) <= 0:
            self.values.append('0.')
            self.update_text()
            return
        self.exist_dot = True
        self.values[-1] = self.values[-1] + '.'

    def calculate(self):
        if len(self.values) < 3:
            return
        num1 = None
        num2 = None
        operator = None
        for vi in self.values:
            convertet_vi = convert(vi)
            if convertet_vi and isinstance(convertet_vi, float | int):
                if num1 == None:
                    num1 = convertet_vi
                elif num2 == None:
                    num2 = convertet_vi
            elif isinstance(vi, str):
                operator = vi
        try:
            if num1 == None and num2 == None and operator == None:
                raise Exception('Не определены данные для расчёта')
            self.values.clear()
            if operator == '+':
                result = num1 + num2
            if operator == '-':
                result = num1 - num2
            if operator == '*':
                result = num1 * num2
            if operator == '÷':
                result = num1 / num2
            self.values.append(str(result))
            self.update_text()
        except Exception as error:
            print(error)

