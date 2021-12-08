class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    ##def  __init__(self):はいらない
    def area(self):
        return self.width * self.len
    
    def print_size(self, flg = True):
        if flg == True:
            print("I am {} by {}".format(self.width, self.len))
        else:
            super().print_size()    #親クラスのprint関数にオーバライドしたprint関数があるが、
                                    #どちらを選択するか選ぶことができるようにした。



a_square = Square(20,20)
a_square.print_size()
a_square.print_size(False)  
