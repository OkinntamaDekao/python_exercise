name = "Ted"
for character in name:
    print(character)

shows = {"伊","藤","弘","晃","様"}
for show in shows:
    print(show)

shows = ("伊","藤","弘","晃","様")
for show in shows:
    print(show)

people = {
    "G. Blurh II": "A Development",
    "Barney": "HIMYM",
    "Dennis": "Always Sunny"
    }


#for character in people.values():
for character in people:
    print(character)    

tv = ["GOT", "Narcos", "Vice"]
i = 0

for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
"""
for show in tv:
    new = show
    new = new.upper()
    tv[i] = new
    i += 1
"""
print(tv)

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends","Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for i in range(1,11):
    print(i)

x = 10
while x > 0:
    #print("{}".format(x))
    print(x)
    x -=1

print("Happy New Year")

while True:
    print("Hello, World!")

for i in range(0,100):
    print(i)

for i in range(0,100):
    print(i)
    break

qs = [
    "What is your name?",
    "What is your fav. color?",
    "What is your quest?"  
]

n = 0
while True:
    print("type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

for i in range(1,6):
    if i == 3:
        continue        #for i in range(1,6):へ
    print(i)

#上記for分のコードと同じ結果
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#入れ子
for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


while input("y or n? ") != "n":
    for i in range(1,6):
        print(i)
        