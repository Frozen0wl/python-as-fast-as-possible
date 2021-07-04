# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Bark")

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")

    def speak(self):
        print("Meow")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "white")
c.speak()
c.show()
    