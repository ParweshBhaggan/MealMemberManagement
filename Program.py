from Menu import MenuController


class Program:
    def __init__(self) -> None:
        self.menuController = MenuController()
        self.menuController.LoginMenu()
   
program = Program()

