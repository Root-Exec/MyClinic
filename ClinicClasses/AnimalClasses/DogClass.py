from ClinicClasses.AnimalClasses.AnimalClass import Animal


class Dog(Animal):
    breed: str
    vaccines = {}

    def __init__(self, dog_breed, animal_type, name, age):
        super().__init__(animal_type, name, age)
        self.breed = dog_breed

    def print_pet_info(self):
        print(f"Name: {self.name}\nType: {self.type}\nBreed: {self.breed}\nAge: {self.age}\n")
        for record in self.vaccines:
            print(record)
            for entry in self.vaccines[record]:
                print(f"\t{entry}")

    def vaccinate(self, vaccine, date):
        if vaccine in self.vaccines.keys():
            self.vaccines[vaccine].append(date)
        else:
            self.vaccines[vaccine] = [date]
