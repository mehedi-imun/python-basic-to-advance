# Encapsulation
# class car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.__model = model
#     def getInfo(self):
#         return {self.__brand , self.__model}

# mycar= car("toyota","corolla")

# print(mycar.getInfo())

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def introduce(self):
#         print(f"hi im {self.name}")

# # s = Person("Karim")
# class Student(Person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def introduce(self):
#         print(f"hi im {self.name}, in grade {self.grade}")
# s = Student("karim",10)
# s.introduce()


# class Dog:
#     def sound(self):
#         print("Woof!")

# class Cat:
#     def sound(self):
#         print("Meow!")

# for animal in [Dog(), Cat()]:
#     animal.sound()




from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r


shapes = [Circle(5), Circle(10)]

for s in shapes:
    print(s.area())
