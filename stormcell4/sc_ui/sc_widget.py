class SCWidget(object):

    def __init__(self):
        self.parent=None

    def get_width(self):
        return 0

    def get_height(self):
        return 0

    def get_size(self):
        return self.get_width(), self.get_height()

    def draw(self, screen, location):
        pass

    def update(self):
        pass

    def get_surface(self):
        pass