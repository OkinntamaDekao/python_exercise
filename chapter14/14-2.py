"""
def CompareObject(a, b):
    if type(a) is type(b):
        return True
    elif type(a) is not type(b):
        return False
"""
#より簡単な書き方
def CompareObject(a, b):
    return a is b
"""
print(CompareObject(1, 8))
print(CompareObject(1.0,8))
print(CompareObject(1,"8"))
"""
print(CompareObject("b","b"))
print(CompareObject("a","b"))
print(CompareObject(1, 8))
print(CompareObject(8, 8))