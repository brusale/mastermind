class Referee:

    def __init__(self, guess, code, attempts):
        self.guess = guess
        self.code = code

        if (attempts > 1):
            print("Attempts left %d" % (int(attempts)-1))
            answer = Referee.CheckGuess(self)
            if (answer):
                quit()
            
        else:
            print("No attempts left, GAME OVER\n Solution: "+str(self.code))
            quit()

    def CheckGuess(self):
        tot_correct_colors = 0
        tot_correct_positions = 0        

        for i in range(0, len(self.code)):
            correct_color = False
            correct_position = False

            if(self.guess[i] in self.code and self.guess[i] == self.code[i]):
                    correct_position = True

            elif(self.guess[i] in self.code and self.guess[i] != self.code[i]):
                    correct_color = True
            else:
                continue
            
            if (correct_position):
                tot_correct_positions += 1
            if (correct_color):
                tot_correct_colors += 1
            
        
        if (tot_correct_positions == 4):
            print(str(self.guess) + " | YOU CRACKED THE CODE")
            return True
        else: 
            print("Correct colors: %d" % tot_correct_colors)
            print("Correct positions: %d" %tot_correct_positions)

            return False
            
