import tkinter
from src.ButtonCommands import *

class MasterMindGUI:

    def __init__(self, attempts, code):
        self.guess = []
        self.attempts = attempts
        self.code = code
        self.gui = tkinter.Tk()
        MasterMindGUI.InitializeGame(self)

    def InitializeGame(self):

        self.gui.title("MasterMind")
        self.gui.geometry('800x1600')

        mainframe = tkinter.Frame(self.gui)
        mainframe.grid(column=0, row=0)

        blue_button = tkinter.Button(self.gui, 
                                     text='Blue', 
                                     fg='white',
                                     bd='5', 
                                     command=lambda:ButtonCommands('blue', self.guess), bg='blue', 
                                     height=10, 
                                     width=20)
        blue_button.grid(column=1,row=1)

        red_button = tkinter.Button(self.gui, 
                                    text='Red', 
                                    fg='white', 
                                    bd='5', 
                                    command=lambda:ButtonCommands('red', self.guess), 
                                    bg='red',
                                    height=10, 
                                    width=20)
        red_button.grid(column=1,row=2)

        green_button = tkinter.Button(self.gui, 
                                      text='Green', 
                                      fg='white', 
                                      bd='5', 
                                      command=lambda:ButtonCommands('green', self.guess), 
                                      bg='green', 
                                      height=10, 
                                      width=20 )
        green_button.grid(column=1,row=3) 

        violet_button = tkinter.Button(self.gui, 
                                       text='Violet', 
                                       fg='white', 
                                       bd='5', 
                                       command=lambda:ButtonCommands('violet', self.guess), 
                                       bg='violet', 
                                       height=10, 
                                       width=20)
        violet_button.grid(column=1,row=4) 

        orange_button = tkinter.Button(self.gui, 
                                       text='Orange', 
                                       fg='white', 
                                       bd='5', 
                                       command=lambda:ButtonCommands('orange', self.guess), 
                                       bg='orange', 
                                       height=10, 
                                       width=20)
        orange_button.grid(column=1,row=5)

        yellow_button = tkinter.Button(self.gui, 
                                       text='Yellow', 
                                       bd='5', 
                                       command=lambda:ButtonCommands('yellow', self.guess), 
                                       bg='yellow', 
                                       height=10, 
                                       width=20)
        yellow_button.grid(column=1,row=6)

        compare_button = tkinter.Button(self.gui, 
                                        text='Answer', 
                                        bd='5', command=lambda:[ButtonCommands(self.guess, self.code, self.attempts), MasterMindGUI.UpdateAttempts(self), MasterMindGUI.ResetGuess(self)], 
                                        height=10, 
                                        width=20)
        compare_button.grid(column=2, row=1)

        self.gui.mainloop()
    
    def UpdateAttempts(self):
        self.attempts-=1
        return self.attempts

    def ResetGuess(self):
        return self.guess.clear()