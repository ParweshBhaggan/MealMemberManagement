from Menu import MenuController


class Program:
    '''The main execution of the application'''
    def __init__(self) -> None:
        self.menuController = MenuController()
        self.menuController.LoginMenu()
   
program = Program()

