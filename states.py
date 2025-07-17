from turtle import Turtle
FONT = ("Courier", 10, "bold")

class States(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def relocate(self,coordinates,state):

        self.goto(coordinates)
        self.write(f"{state}", move=False, align="center", font=FONT)
        #self.hideturtle()

    def win_game(self):
        # self.clear()
        self.goto(0,-5)
        self.write("Congratulations You Guessed All States.", move=False, align="center", font=("Courier", 20, "bold"))