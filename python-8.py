class Family:
    def __int__(self, name,age,gender,relation):
        self.name=name
        self.age=age
        self.gender=gender
        self.relation=relation

    def together(self):
        print("our famil eat together")
son=Family("atharv",12,"male","son")
father=Family("sunil",42,"male","father")
print(son.name)
print(father.name)
print(son.age)
father.together()
our_family=[]
our_family.append(son)
our_family.append(father)
for i in our_family:
    print(i.name,i.age,i.relation)