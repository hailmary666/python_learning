from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

me = Die()
for rolls in range(10):
    me.roll_die()
