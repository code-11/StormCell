import json

class PropertyReader ():

    def __init__(self):
        self.data = {}
        with open("properties.json", "r") as read_file:
            self.data = json.load(read_file)

    def get_property(self, str_prop_name):
        return self.data[str_prop_name]