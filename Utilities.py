import sys
import time
import os


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

    def QuitApplication(self):
        print("Closing application...")
        self.SleepConsole(1.1)
        self.ClearConsole()
        sys.exit()
    