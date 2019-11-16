import json
import os

COUNTRY_FILE_PROPNAME = "countryLocation"
DATA_PATH_PROPNAME = "dataLocation"


class CountriesIO():
    def __init__(self, prop_reader):
        self.prop_reader = prop_reader
        self.country_file_path = None
        self.data = None

    def init_properties(self):
        filename = self.prop_reader.get_property(COUNTRY_FILE_PROPNAME)
        data_path = self.prop_reader.get_property(DATA_PATH_PROPNAME)
        self.country_file_path = os.path.join(data_path, filename)

    def load(self):
        with open(self.country_file_path, "r") as read_file:
            self.data = json.load(read_file)