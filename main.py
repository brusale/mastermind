from src.MasterMind import *

class App:
    
    def __init__(self, attempts):
        self.app = App.Run(self, attempts)

    def Run(self, attempts):
        MasterMind(attempts)

if __name__ == "__main__":
    print("Insert number of attempts")
    attempts = int(input())

    App(attempts)
