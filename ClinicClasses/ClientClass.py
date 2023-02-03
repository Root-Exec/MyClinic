from ClinicClasses.AnimalClasses import *


class Client:
    FirstName: str
    MiddleName: str
    LastName: str

    Address: str
    City: str
    ZipCode: str

    TelephoneNumber: str
    pets = []

    def register(self, f_name, m_name, l_name, telephone_number):
        self.FirstName = f_name
        self.MiddleName = m_name
        self.LastName = l_name
        self.TelephoneNumber = telephone_number

    def set_address(self, address, city, zipcode):
        self.Address = address
        self.City = city
        self.ZipCode = zipcode

    def add_pet_to_owner(self, pet_object):
        self.pets.append(pet_object)

    def remove_pet_from_owner(self, name):
        for animal in self.pets:
            if animal.get_pet_name() == name:
                del animal
                return
        print("Could not find pet in client record")

    def print_client_info(self):
        print(f"Name: {self.FirstName} {self.MiddleName} {self.LastName}")
        print(f"{self.TelephoneNumber}")
        print(f"{self.Address} {self.City}, {self.ZipCode}")
        print("-----Pets-----")
        for pet in self.pets:
            print(f"{pet.print_pet_info()}")
            print("-------")

