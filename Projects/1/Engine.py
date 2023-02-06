from time import sleep
import pygame, sys
import Notif
from Player import Player
from Maze import Maze

# GLOBALS
DISPLAY_DIMS = 600 # 800 x 800
BOARDSIZE = 20 # 50 x 50
CELLSIZE = DISPLAY_DIMS / BOARDSIZE # 16 x 16
DISPLAY = pygame.display.set_mode((DISPLAY_DIMS, DISPLAY_DIMS))
FPS = 20

""" Main Game Engine for Maze Generator/Game.

Engine for Maze Generator/Game. Runs the main
game loop and contains objects of the Maze
and Player classes. 

Typical usage example:
  engine = Engine()
  engine.loop()
"""
class Engine:
    """Initializes Engine.x
    Initializes pygame, Maze, and Player.
    Returns:
        a new Engine object
    """
    def __init__(self):
        self.mazeGroup = pygame.sprite.Group()
        self.player = Player(position=(0,0))
        self.maze = Maze(size=BOARDSIZE, player=self.player, cellSize=CELLSIZE, group=self.mazeGroup)
        self.winningCell = self.maze.board[BOARDSIZE - 1][BOARDSIZE - 1]
        
        pygame.init()
        pygame.display.set_caption('Maze Generator')


    """Main game loop.x
    Processes input, updates objects,
    generates outputs.
    """
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
                    Notif.notifyMBDEvent(x, y) #remove

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


    """Update game objects.x
    Updates objects depending on setting.
    If running, updates maze cells. If playing,
    updates player.
    Args:
        run: running maze generator?
        playing: playing maze game?
        delta: delta from game loop
    """
    def updateObjects(self, run, playing, delta):
        if playing:
            keys = pygame.key.get_pressed()
            moveKeys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
            for key in moveKeys:
                if keys[key]:
                    self.mazeGroup.update(run, playing, key, delta)
                    
        elif run:
            self.mazeGroup.update(run, playing)


    """Draw board.x
    Draws board from maze object.
    Draws player if playing.
    Args:
        playing: playing maze game?
    """
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