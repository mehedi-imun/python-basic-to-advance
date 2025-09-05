class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def showInfo(self):
        print("name",self.model)
# mycar= car("toyota","corolla")

# print(mycar.brand,mycar.model)
car = car("toyota","cololla")
car.showInfo()