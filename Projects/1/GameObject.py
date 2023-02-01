class GameObject():

    coordinates = (-1, -1)

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def update(self, coordinates: tuple):
        self.rect.center = coordinates
