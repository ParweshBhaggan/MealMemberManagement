import sys
import time
import os
from termcolor import colored

class Utilities:
    def __init__(self) -> None:
        pass
    
    def ClearConsole(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def SleepConsole(self, timer):
        time.sleep(timer)
    
    def PrintMenuTitle(self, title):
        print(f"-----    {title}    -----\n")

    def SuccessMessage(self, message):
        message = colored(message, "green", attrs=['bold'])
        return message
    def ConsoleMessage(self, message):
        message = colored(message, "yellow", attrs=['bold'])
        return message
    def ErrorMessage(self, message):
        message = colored(message, "red", attrs=['bold'])
        return message
    def ReturnMessage(self, message):
        message = colored(message, "blue", attrs=['bold'])
        return message

    def QuitApplication(self):
        print(self.ConsoleMessage("Closing application..."))
        self.SleepConsole(1.1)
        self.ClearConsole()
        sys.exit()
