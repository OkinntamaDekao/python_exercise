class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    
    #"+"の演算子を使用するためにメソッドを定義した。
    #例えば2 + 2のどちらのオブジェクトもこのメソッドを持っている
    def __add__(delf, other):
        return abs(delf.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)