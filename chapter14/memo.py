class Square:
    pass

print(Square)

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)