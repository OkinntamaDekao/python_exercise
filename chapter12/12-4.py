class Hexagon:
    def __init__(self, e):
        self.edge = e

    def calculate_perimeter(self):
        return self.edge * 6
    
hexagon = Hexagon(12)
print(hexagon.calculate_perimeter())