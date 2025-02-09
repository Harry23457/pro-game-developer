class fruit():
    def __init__(self,name,color,taste,country):
        self.name=name
        self.color=color
        self.taste=taste
        self.country=country
    def showdetails(self):
        print ("details of the fruits are:")
        print ("name:",self.name)
        print ("color:",self.color)
        print ("taste:",self.taste)
        print ("country:",self.country)

f1=fruit("banana","yellow","sweet","south east asia")
f1.showdetails()
f2=fruit("peach","pink","sweet","china")
f2.showdetails()   