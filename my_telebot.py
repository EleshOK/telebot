import calculate_command

class MyTelebot:
    def __init__(self):
        self.current_operation = None
        self.calc_command = None
        self.current_message_text = None   
    def set_current_message_text(self, message_text):
        self.current_message_text = message_text

    def set_operation(self, current_operation):
        self.current_operation = current_operation

    def run_calc(self):
        if self.calc_command == None:
            self.calc_command = calculate_command.CalculateCommand()
            return self.calc_command.start_calc()
        return self.calc_command.calculate(self.current_message_text)
