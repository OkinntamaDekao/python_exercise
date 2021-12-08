def get_float(x):
    """
    Returns float x
    :param x: string
    return xを浮動小数点に変換したもの
    """
    return float(x)

try:
    a = input("input number:")
    print(get_float(a))
except ValueError:
    print("input should be number")

