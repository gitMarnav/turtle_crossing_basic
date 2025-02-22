from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_COLOR = 'white'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.goto(-200, 250)
        self.level = 0
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False,
                   align="center", font=FONT)

    def refresh_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", move=False,
                   align="center", font=FONT)

    def final_score(self):
        self.clear()
        self.goto(-140, 250)
        self.write(f"Final Score: {self.level * 10}", move=False,
                   align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"\nGAME OVER", move=False, align='center', font=FONT)
