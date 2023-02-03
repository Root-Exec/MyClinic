from ClinicClasses.AnimalClasses import *
from ClinicClasses.ClientClass import Client
from Data import DB_API_Communicator as api

if __name__ == "__main__":
    cat = CatClass.Cat("Siamese", "Cat", "Mr. Bigglesworth", "3")
    cat.vaccinate("Rabies", "27 Jan 20")
    cat.vaccinate("Distemper", "27 Jan 23")
    cat.vaccinate("Rabies", "27 Jan 23")

    firstclient = Client()
    firstclient.register("Paige", "Greer", "Bonner", "(304)593-3147)")
    firstclient.set_address("22911 Malabar Peak", "San Antonio", "78261")
    firstclient.add_pet_to_owner(cat)
    firstclient.print_client_info()

    API_Caller = api.API_Communicator()
    API_Caller.create_json_ob(cat)
    # API_Caller.print_json_obj()
