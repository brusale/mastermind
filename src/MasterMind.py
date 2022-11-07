from src.MasterMindGUI import *
from src.CodeGenerator import *

class MasterMind:
    
    def __init__(self, attempts):
        self.attempts = attempts
        self.code = CodeGenerator().GetCode()

        self.gui = MasterMindGUI(self.attempts, self.code)

