import random

class CodeGenerator:

    def __init__(self):
        colors = ['blue', 'red', 'green', 'violet', 'orange', 'yellow']
        self.code = []
        for i in range(0, 4):
            self.code.append(random.choice(colors))
        # print("***** CODE *****")
        # print(self.code)
        # print("****************")

    def GetCode(self):
        return self.code