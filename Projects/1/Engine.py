from time import sleep
import pygame, sys
import Notif
from Player import Player
from Maze import Maze

DISPLAY_DIMS = 600 # 800 x 800
BOARDSIZE = 20 # 50 x 50
CELLSIZE = DISPLAY_DIMS / BOARDSIZE # 16 x 16
DISPLAY = pygame.display.set_mode((DISPLAY_DIMS, DISPLAY_DIMS))
FPS = 60

class Engine:

    # initialize Engine
    def __init__(self):
        self.mazeGroup = pygame.sprite.Group()
        self.player = Player(position=(0,0))
        self.maze = Maze(size=BOARDSIZE, player=self.player, cellSize=CELLSIZE, group=self.mazeGroup)
        self.winningCell = self.maze.board[BOARDSIZE - 1][BOARDSIZE - 1]
        
        pygame.init()
        pygame.display.set_caption('Maze Generator')


    # main game loop
    def loop(self):
        clock = pygame.time.Clock()
        last = clock.get_time()
        runGenerator = False
        play = False
        self.won = False
        while not self.won:
            current = clock.get_time()
            delta = current - last
            delta /= 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    Notif.notifyMBDEvent(x, y)

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            runGenerator = not runGenerator
                            play = False
                        case pygame.K_p:
                            play = not play
                            runGenerator = False

            self.updateObjects(runGenerator, play, delta)
            self.drawBoard(play)
            clock.tick(FPS)

        print('YOU WIN')


    def updateObjects(self, run, playing, delta):
        if playing:
            keys = pygame.key.get_pressed()
            moveKeys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
            for key in moveKeys:
                if keys[key]:
                    self.mazeGroup.update(run, playing, key, delta)
                    
        elif run:
            self.mazeGroup.update(run, playing)


    def drawBoard(self, playing):
        for row in range(BOARDSIZE):
            for col in range(BOARDSIZE):
                cell = self.maze.board[row][col]
                pygame.draw.rect(DISPLAY, cell.color, cell.rect)
        
        if playing:
            DISPLAY.blit(self.player.image, self.player.coordinates)
            if self.winningCell.rect.bottomright == self.player.rect.bottomright:
                self.won = True
        pygame.display.update()


if __name__ == '__main__':
    engine = Engine()
    engine.loop()