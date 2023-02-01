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

    # initialize Engine
    def __init__(self):
        self.mazeGroup = pygame.sprite.Group()
        self.maze = Maze(size=BOARDSIZE, cellSize=CELLSIZE, group=self.mazeGroup)
        self.player = None
        pygame.init()
        pygame.display.set_caption('Maze Generator')


    # main game loop
    def loop(self):
        FPS = 60
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Notif.notifyMBDEvent(x, y) # update clicked cell
            
            self.mazeGroup.update(DISPLAY)
            pygame.display.update()


if __name__ == '__main__':
    engine = Engine()
    engine.loop()