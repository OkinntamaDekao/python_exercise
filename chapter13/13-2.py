class Shape:
    """def __init__(self):
        print("I am a ga")"""
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l1, l2):
        self.len1 = l1
        self.len2 = l2
    
    def calculate_peremeter(self):
        return self.len1 * 2  + self.len2 * 2

class Square(Shape):
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
rec.what_am_i()
sq.what_am_i()
    