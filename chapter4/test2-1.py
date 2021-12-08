def sqre(x):
    """
    Retruns x ** 2
    :param x: int.
    return: int x ** 2
    """
    return x ** 2

print("sqre num")

try:
    a = float(input("type a number:"))
    print(sqre(a))
except ValueError:
    print("input should be number")


