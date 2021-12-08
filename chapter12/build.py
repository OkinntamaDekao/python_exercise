class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Created!")
    
orl = Orange(10, "dark orange")
print(orl)
orl.weight = 100
orl.color = "light orange"
print(orl.weight)
print(orl.color)

orl1 = Orange(4,"light orange")
orl2 = Orange(8, "dark orange")
orl3 = Orange(14,"yellow")