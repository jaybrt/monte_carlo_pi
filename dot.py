class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_circle(self):
        return self.x**2 + self.y**2 <= 1
