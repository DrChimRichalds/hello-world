# Python code​​​​​‌​​​​​‌​​​‌​​‌​‌​​‌‌‌​‌​‌​ below
class Shape:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.printChar = '#'
        self.spaceChar = " "

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)


class Right_Triangle(Shape):
    # This can be the same because you start at the same height and iterate down
    def printRow(self, i):
        # This needs to be different than a square
        print(self.printChar * (i+1))

class Isolece_Triange(Shape):

    def printRow(self, i):
        print(self.spaceChar * i + self.printChar * (self.width + -2 * i) + self.spaceChar * i)
        if i == self.height - 1:
            pass
        
s = Isolece_Triange(6,6)
s.print()