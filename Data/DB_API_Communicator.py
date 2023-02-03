import json


class API_Communicator:
    json_obj: str
    json_obj_items = {}

    def create_json_ob(self, entry):
        self.json_obj_items["Name"] = entry.name
        self.json_obj_items["Species"] = entry.type
        self.json_obj_items["Breed"] = entry.breed
        self.json_obj_items["Age"] = entry.age
        self.json_obj_items["Vaccines"] = entry.vaccines
        self.json_obj = json.dumps(self.json_obj_items, indent=3)

    def send_record(self):
        pass

    def retrieve_record(self):
        pass

    def print_json_obj(self):
        print(self.json_obj)
