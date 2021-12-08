colors = ["purple", "orange", "green"]
guess = input("私は何色を想像しているでしょう？→入力:")

if guess in colors:
    print("あたり")
else:
    print("はずれ")

