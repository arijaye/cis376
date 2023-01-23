import Scene

class Maze(Scene):
    cells = []
    living = 0
    dead = 0

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f"Living cells: {self.living} Dead cells:{self.dead} \n {self.cells}"
