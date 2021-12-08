class Rectangle:
    def __init__(self, l1, l2):
        self.len1 = l1
        self.len2 = l2
    
    def calculate_peremeter(self):
        return self.len1 * 2  + self.len2 * 2

class Square:
    def __init__(self, l):
        self.length = l
    
    def calculate_peremeter(self):
        return 4 * self.length

    def change_size(self,l):
            self.length += l
            if self.length <= 0:
                print("値が有効ではありません。")

            

rec = Rectangle(2,3)
sq = Square(3)
print(rec.calculate_peremeter())
print(sq.calculate_peremeter())
sq.change_size(-3)
print(sq.calculate_peremeter())
