import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(row)
    
    print(r.line_num)

    #この例ではcsvファイルの中身は
    #one,two,three
    #four,five,six
    #となっている。一行を一つの配列とし、その配列の要素はカンマで区切られたもの
    #実行結果
    #['one', 'two', 'three']
    #['four', 'five', 'six']
