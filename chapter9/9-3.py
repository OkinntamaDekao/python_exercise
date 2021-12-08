import csv

list = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day","Man on Fire", "Flight"]]

with open("9-3.csv","w",newline="") as f:
    w = csv.writer(f, delimiter = ",")
    for row in list:
        w.writerow(row)

#8行目のNewLine=""がないと一行おきに書かれてしまう。
#一回核と改行コードが2回書かれるイメージ