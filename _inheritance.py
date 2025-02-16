#parent class
class person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def details (self):
        print(f"name is {self.name}")
        print(f"id is {self.id}")
        
#child class
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id)
    def display (self):
        print(f"name is {self.name}")
        print(f"id = {self.id}")
        print(f"post = {self.post}")
        print(f"salary={self.salary}")

p1=person("Bob","3575")
p1.details()
p2=employee("paul","3648","49675","software engineer")
p2.display()
p2.details()
p1.display()