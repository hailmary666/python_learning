class Ball():
    def __init__(self, type='regular'):
        self.ball_type = type

ball1 = Ball()
print(ball1.ball_type)

ball2 = Ball('shitball')
print(ball2.ball_type)
