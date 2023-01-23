import pygame, sys

# updateTime = 60 / 1000
# last = clock.now()
# lag = 0
# while not_finished:
#     current = clock.now()
#     delta = current - last
#     lag = lag + delta
#     processInputs()
#     # fixed-time loop
#     while lag >= updateTime:
#         update()
#         lag = lag - updateTime
    
#     # Interpolate so things aren't jumpy
#     processOutputs(lag / updateTime)


class Engine:
    DISPLAY = pygame.display.set_mode((800, 600))
    FPS = 60
    clock = pygame.time.Clock()
    events = pygame.event.get()

    

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Maze Generator')
        self.loop()

     # main game loop
    def loop(self):
        last = Engine.clock.now()
        lag = 0
        while True:
            # process input (events)
            # update game objects
            # generate outputs
            current = Engine.clock.now()
            delta = current - last
            lag = lag + delta
            # process inputs

            while lag >= Engine.FPS:
                # update()
                lag = lag - Engine.FPS
            
            # processOutputs(lag/FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                print(event)
            
            Engine.DISPLAY.fill((255,255,255))
            pygame.display.update()
            Engine.clock.tick(Engine.FPS)

engine = Engine()