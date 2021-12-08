#これでimportされたときに下記コードが実行されるのを防ぐ。
#python.module.py の時のみ Hello!が出力されるということ。
if __name__ == "__main__":
    print("Hello!")