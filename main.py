from app import App
from igets import igets

class Program:
    def __init__(self):
        self.app = App()
    
    def run(self):
        while True:
            user_input = igets.Str(">> ")
            self.app.handleCommand(user_input)

if __name__ == "__main__":
    program = Program()
    program.run()