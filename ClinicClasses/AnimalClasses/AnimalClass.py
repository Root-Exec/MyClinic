class Animal:
    name: str
    type: str
    age: str
    medical_notes: str

    def __init__(self, animal_type, name, age):
        self.type = animal_type
        self.name = name
        self.age = age

    def get_pet_name(self):
        return self.name
