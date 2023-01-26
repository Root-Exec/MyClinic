from ClinicClasses.AnimalClasses.AnimalClass import AnimalClass


class Dog(AnimalClass):
    breed: str

    def __init__(self, dogBreed, speak, animal_type, name, age):
        super().__init__(speak, animal_type, name, age)
        self.breed = dogBreed

    def review(self):
        print(
            "{0} is a {1} and is {2} years old. The {3} says {4}".format(self.name, self.type, self.age, self.type,
                                                                         self.speak))
