class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
    
    def area(self):
        return self.bottom * self.height / 2
    
triangel = Triangle(3,4)
print(triangel.area())