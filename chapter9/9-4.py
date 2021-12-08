import csv

list = [
    ["トップガン", "リスキービジネス", "マイノリティーレポート"],
    ["タイタニック", "ザ・レヴェナント", "インセプション"],
    ["トレーニングデイ","マンオンファイアー", "フライト"]]

with open("9-4.csv","w",newline="") as f:
    w = csv.writer(f, delimiter = ",")
    for row in list:
        w.writerow(row)

#8行目のNewLine=""がないと一行おきに書かれてしまう。
#一回核と改行コードが2回書かれるイメージ
#日本語入力だがエンコーディングなしで行けた