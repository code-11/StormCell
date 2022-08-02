ai_types = ["Human", "CPU-Def", "CPU-Aggr"]


class Nation(object):
    def __init__(self, color, name, starting_gold=0):
        self.color = color
        self.name = name
        self.gold = starting_gold
        self.ai_type = None

    def sc_json_save(self):
        return {
            "color": self.color,
            "name": self.name,
            "gold": self.gold,
            "ai_type": self.ai_type
        }

    def sc_json_load(self, nation_dict):
        self.color = nation_dict['color']
        self.name = nation_dict['name']
        self.gold = nation_dict['gold']
        self.ai_type = nation_dict.get('ai_type', None)



