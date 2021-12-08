dict = {"height":170,"weight":70,"favorite_color":"red","favorite_author":"Isaka_Koutaro"}

key = input("input key:")
if key in dict:
    print(dict[key])
else:
    print("This key isn't dictionary")


#print(dict["height"])
#print(dict["weight"])
#print(dict["favorite_author"])
#print(dict["favorite_color"])