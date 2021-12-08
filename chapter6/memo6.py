author = "Chinko"
author[0]
author[1]
author[2]
author[3]
author[4]
author[5]
author[-1]
author[-2]
author[-3]
author[-4]
author[-5]
author[-6]

"Chinko" * 3

"chinko".upper()
"CHINKO".lower()

"stand up Chinko".capitalize()
"こんにちわ、{}".format("伊藤弘晃様")
name = "伊藤弘晃様"
"こんにちわ、{}".format(name)

name = "伊藤弘晃様"
year_born = 1995
"{}は{}年に生まれました".format(name, year_born)

what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした:")

output = "{}は{}に{}で{}した。".format(what, when, where, do)

"伊藤弘晃様。万歳!!!".split("。")

str = "abc"
result = "ウンチ".join(str)
result

words = ["The", "fox", "jumped", "over", "the", "fence","."]
result = "".join(words)
result = " ".join(words)
result

s = "   ウンチ   "
s = s.strip()
s

equ = "All animals are equal."
equ = equ.replace("a", "@")
equ

"animals".index("m")
try:
    "animals".index("z")
except:
    print("Not Found.")

"Cat" in "Cat in the hat"
"unnchi" in "Cat in the hat"
"unnchi" not in "Cat in the hat"

"彼女は\"そうだね\"といった"