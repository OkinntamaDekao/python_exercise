list = [1,3,5,7,9]
inputmatch = False

while True:
    num = input("数値を入力してください(qでプログラムを終了します):")
    if num == "q":
        break

    try:
        num = int(num)
    except ValueError:
        print("数字かqを入力してください")
        continue

    if num in list:
        print("正解")
    else:
        print("不正解")