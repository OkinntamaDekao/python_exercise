a = input("何か入力して下さい:")

with open("text.txt","w",encoding="utf-8") as f:
    f.writelines(a)

print("text.txtに入力したものを出力しました。")