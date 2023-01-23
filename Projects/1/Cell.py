import GameObject

class Cell(GameObject):
     
    neighbors = -1
    color = (0,0,0) # open cell

    def __init__(self, neighbors):
        self.neighbors = neighbors

    def __str__(self):
        return f"Neighbors: {self.neighbors}"
