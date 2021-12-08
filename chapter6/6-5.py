words = ["The", "fox", "jumped", "over", "the", "fence","."]
str = " ".join(words)
num = str.index(".")
print(num)
#print(str[0:-3])
#str = str[0:-2]
str = str[0:num-1] + "."
print(str)
