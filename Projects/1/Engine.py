import pygame, sys
import Notif
from Maze import Maze

# TODO:
# - populate neighbors array for Cell(s)
# - update Cell color based on neighbor state
# - make Cells clickable for beginning seeds? need to be able to watch as maze changes states

DISPLAY_DIMS = 800 # 800 x 800
BOARDSIZE = 20 # 50 x 50
CELLSIZE = DISPLAY_DIMS / BOARDSIZE # 16 x 16
DISPLAY = pygame.display.set_mode((DISPLAY_DIMS, DISPLAY_DIMS))

class Engine:
    FPS = 60
    clock = pygame.time.Clock()
    running = False


    def __init__(self):
        self.events = pygame.event.get()
        self.maze = Maze(size=BOARDSIZE, cellSize=CELLSIZE)
        pygame.init()
        pygame.display.set_caption('Maze Generator')
        self.drawBoard()


    def drawBoard(self):
        for row in self.maze.board:
            for cell in row:
                pygame.draw.rect(DISPLAY, cell.color, cell.rect, int(CELLSIZE))


    # main game loop
    def loop(self):
        last = Engine.clock.get_time()
        lag = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Notif.notifyMBDEvent(event, x, y)
            
            # wait to run sim until beginning maze is drawn (4 cells with color?)
            Engine.clock.tick(Engine.FPS)
            pygame.display.update()


if __name__ == '__main__':
    engine = Engine()
    engine.loop()