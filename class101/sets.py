class Details:
    def __init__(self , name, clas):
        self.name = name
        self.clas = clas

    def __str__(self):
        print("Name = {self.name} and class = {self.clas}")


p1 = Details("Nashit", "Cs")
p2 = Details("Anjum", "dropper")

print(p1.name)
print(p2.name)
print(p1)