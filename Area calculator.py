import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #set width
    def set_width(self, width):
        self.width = width

    #set height
    def set_height(self, height):
        self.height = height
    
    # calculate area
    def get_area(self):
        return self.width * self.height

    #calculate perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    #calculate length of the diagonal
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    #creates a rough image of the shape with the given lengths
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    #returns the numeber of shapes that can fit inside the current shape
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    #sets the width
    def set_width(self, width):
        self.width = width
        self.height = width

    #sets the height
    def set_height(self, height):
        self.width = height
        self.height = height

    #width and height are the same
    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
