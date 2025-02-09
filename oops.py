class student():
    def __init__(self,name,age,house,year,teacher):
        self.name=name
        self.age=age
        self.house=house
        self.year=year
        self.teacher=teacher
    def showdetails(self):
        print ("details of this student are :")
        print ("name :",self.name)
        print ("age:",self.age)
        print ("house:",self.house)
        print ("year:", self.year)
        print ("teacher:",self.teacher)
    
s1 =student("Bob","11","griffindor",8,"proffeser magonical")
s1.showdetails()