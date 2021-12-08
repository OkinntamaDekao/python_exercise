class Horse:
    def __init__(self, p):
        self.partner = p
    
class Rider:
    def __init__(self, n):
        self.name = n

r = Rider("伊藤弘晃様")
h = Horse(r)

print(h.partner.name)