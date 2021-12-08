class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

s1 = Square(20)
s2 = Square(40)
s3 = Square(80)

print(s1)
print(s2)
print(s3)
