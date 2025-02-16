class car():
    def __init__(self,type,brand,color,country):
        self.brand=brand
        self.color=color
        self.type=type
        self.country=country
    def showdetails(self):
        print ("details of the fruits are:")
        print ("type:",self.type)
        print ("color:",self.color)
        print ("brand:",self.brand)
        print ("country:",self.country)

c1=car("microcar","ligier","silver","denmark")
c1.showdetails()
c2=car("hatchback","toyota","red","japanese")
c2.showdetails()    

print(c2.brand)