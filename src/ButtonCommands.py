from src.Referee import *

class ButtonCommands:

    def __init__(self, *args):
        self.command=ButtonCommands.Insert(*args)

    def Insert(*args):
        if (len(args) == 2):
            args[1].append(args[0])

        if (len(args) == 3):
             Referee(args[0], args[1], args[2])
             print(args[0])