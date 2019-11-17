from country import *


class Countries(object):
    def __init__(self):
        self.country_list = []
        self.country_by_name = {}

    def construct_countries(self, country_list, continent_data):
        for country_name in country_list:
            self.construct_country(country_name, continent_data)

    def find_continent_for_country(self, country_name, continent_data):
        for continent, country_dict in continent_data.items():
            if country_name in country_dict:
                return continent
        return None


    def construct_country(self, name, continent_data):

        continent = self.find_continent_for_country(name, continent_data)
        if not continent:
            print("Could not find continent data for "+name)
        else:
            new_country = Country(name)
            new_country.continent = continent
            self.add_county(new_country)

    def add_county(self, country_obj):
        self.country_list.append(country_obj)
        self.country_by_name[country_obj.name] = country_obj
