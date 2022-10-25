class MyTelebot:
    def __init__(self):
        self.current_operation = None
        self.calc_command = None
        self.current_message_text = None   
    def set_current_message_text(self, message_text):
        self.current_message_text = message_text
    def set_operation(self, current_operation):
        self.current_operation = current_operation
        
