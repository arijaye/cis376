from time import sleep
import pygame, sys
import Notif
from Player import Player
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
        self.playerGroup = pygame.sprite.Group()
        self.maze = Maze(size=BOARDSIZE, cellSize=CELLSIZE, group=self.mazeGroup)
        self.player = Player(position=(0,0), size=10, group=self.playerGroup)
        pygame.init()
        pygame.display.set_caption('Maze Generator')


    def drawBoard(self):
        for row in range(BOARDSIZE):
            for col in range(BOARDSIZE):
                cell = self.maze.board[row][col]
                pygame.draw.rect(DISPLAY, cell.color, cell.rect)
        
        pygame.display.update()

    
    # main game loop
    def loop(self):
        FPS = 20
        clock = pygame.time.Clock()
        update = False
        play = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # click to clear???
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Notif.notifyMBDEvent(x, y)

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            update = not update
                        case pygame.K_p:
                            play = not play
                        case _:
                            Notif.notifyKeyEvent(event.key)

            if play:
                self.playerGroup.update()
                DISPLAY.blit(self.player.surf, self.player.coordinates, self.player.rect)
            elif update:
                self.mazeGroup.update()
                
            self.drawBoard()
            clock.tick(FPS)


if __name__ == '__main__':
    engine = Engine()
    engine.loop()