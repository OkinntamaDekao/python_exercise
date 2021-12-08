try:
    a = int(input("type a number:"))
    b = int(input("type another:"))
    print(a/b)
    print("b cannnot be zero")
except(ZeroDivisionError, ValueError):
    print("Invalid input")
