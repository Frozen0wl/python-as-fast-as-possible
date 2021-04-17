class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


tim = person('tim', 18)



print(person.get_population())
print(person.is_adult(2))

tim.display()


