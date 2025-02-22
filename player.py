from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, shape="turtle"):
        super().__init__(shape)
        self.penup()
        self.color('White')
        self.setheading(90)
        self.refresh_position()

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def refresh_position(self):
        self.goto(STARTING_POSITION)
