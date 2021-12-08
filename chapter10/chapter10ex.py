
def hangman(word):
    wrong = 0                           #間違いカウンター
    stages = [
        "",
        "_______       ",
        "|             ",
        "|      |      ",
        "|      0      ",
        "|     /|\     ",
        "|     / \     ",
        "|             "
        ]                               #ハングマン配列。間違えたらこの配列の要素がひとつづつ出力されていき、この配列の要素がすべて出力されるとプレイヤーの負け
    rletters = list(word)               #走査用文字列
    board = ["_"] * len(word)           #出力用文字列。この文字列の初期値はwordの要素数の"_"
    win = False                         #プレイヤーの勝利フラグ。全ての文字を当てるとTrueになる。
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:      #wrongは1スタートで配列の要素は0スタートなので-1して合わせる
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)               #charにプレイヤーの文字列入力
        if char in rletters:            #走査用文字列内に入力用文字列がある = True
            cind = rletters.index(char) #何番目にあるか走査（0スタート）その文字が配列の何番目の要素か記憶
            board[cind] = char          #出力用文字列の該当箇所に入力された文字列を出力
            rletters[cind] = '$'        #見つけた文字列は$に置換しておく。こうして置くことで、これ以後の同じ文字場所をindexで取得できるようになる。
        else:                           #走査用文字列内に入力用文字列がある = False
            wrong += 1                  #間違いカウンタープラス1
        print(" ".join(board))          #出力用文字列に" "をはさんで出力"
        e = wrong + 1                   #ハングマン外列出力用にまた以外カウンターから出力用数値を作る。
        print("\n".join(stages[0:e]))   #ハングマン出力
        if "_" not in board:            #出力用文字列に_がなかったら（文字をすべて当てられたら）
            print("あなたの勝ち!")
            print(" ".join(board))      #答えの表示
            win = True
            break
    
    if not win:                                             #まけなら
        print("\n".join(stages[0:wrong + 1]))               #ハングマンの完成を表示
        print("あなたの負け!正解は{}.".format(word))          #正解を表示        

def randomstr(x):
    try:
        x = int(x)
    except ValueError:
        print("数字を指定してください")


    list = ["strong","weak","genius"]
    if x % 3 == 0:
        return list[0]
    elif x % 3 == 1:
        return list[1]
    elif x % 3 == 2:
        return list[2]

a = input("数値を入力してください。その数値から文字列を生成します:")
hangman(randomstr(a))