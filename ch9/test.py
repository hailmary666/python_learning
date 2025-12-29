class Ball():
    def __init__(self, *type):
        self.type = type
        if self.type:
            self.ball_type = "super"
        else:
            self.ball_type = "regular"

ball1 = Ball()
ball2 = Ball('super')
ball3 = Ball('shit', 'fuck')
ball4 = Ball('gogogo')

print(ball1.ball_type)
print(ball2.ball_type)
print(ball3.ball_type)
print(ball4.ball_type)
