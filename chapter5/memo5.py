#リスト[]
fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
fruit

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")

fruit = ["Apple", "Orange", "Pear"]
fruit[0]
fruit[1]
fruit[2]
fruit[3]

"Hello".replace("o","ooooooo")

colors = ["blue","green","yellow"]
colors
colors[2] = "red"
colors

colors = ["blue","green","yellow"]
colors
item = colors.pop()
item
colors

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
colors2 + colors1 

colors = ["blue", "green", "yellow"]
"green" in colors
"black" not in colors
len(colors)

colors = ["purple", "orange", "green"]
guess = input("私は何色を想像しているでしょう？")

if guess in colors:
    print("あたり")
else:
    print("はずれ")

#タプル()
my_tuple = tuple()
my_tuple

my_tuple = ()
my_tuple

rndm = ("M. Jackson", 1958, True)
rndm

#This is tuple
("self_taught",)
#This is not tuple, but calcuration()
(9) + 1

dys = ("1984", "Brave NewWorld", "Fahrenheit 451")
dys[2]
"1984" in dys

#ディクショナリー
my_dict = dict()
my_dict = {}
my_dict

fruits = {"Apple" : "Red" ,
        "Banana" : "Yellow"}
fruits

facts = dict()
facts["code"] = "fun"
facts["code"]
facts["Bill"] = "Gates"
facts["Bill"]
facts["fouded"] = 1776
facts["fouded"]

bill = {"Bill Gates": "charutable"}
"Bill Gates" in bill

books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
del books["The Trial"]
books

#リストのリスト
list = []
dish = {"Ramen", "Sushi", "Gyouza", "Humberger"}
furit = {"Apple", "Orange", "Green"}
drink = {"Beer", "Cola"}

list.append(dish)
list.append(furit)
list.append(drink)

list

locations = []

la = (34.0522, 188.2437)
chicago = (47.8781, 87.6298)

locations.append(la)
locations.append(chicago)

locations

ny = {
    "座標":(40.7128, 74.0059),

    "セレブ":[
        "Ito",
        "Hiroaki"
    ],
    
    "事実":{
        "州": "ニューヨーク",
        "国": "アメリカ"
    }   
}

ny["事実"]