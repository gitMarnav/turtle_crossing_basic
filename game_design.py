from turtle import Turtle


class Gamedesign(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-290, 240)
        self.draw_line()

    def draw_line(self):
        while self.xcor() < 290:
            self.down()
            self.fd(10)
            self.up()
            self.fd(10)
# Will add new features later
