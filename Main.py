import sys,pygame, logging
from Engine import Engine
class GraviShot:
    def __init__(self):
        self.screen_w = 0
        self.screen_h = 0
        self.screen = None
        self.clock = None
        self.gamestart = False
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

    def set_game_config(self,screen_w,screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h

    def initial_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption("GraviShot")
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))
    def event_process(self,events):
        inputs = {"w":0,"a":0,"s":0,"d":0}
        for event in events:
            if event.type == pygame.QUIT:
                self.gamestart = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    logging.info("spacebar")
                if event.key == pygame.K_ESCAPE:
                    self.gamestart = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_w:
                    inputs["w"] += 1
                if event.key == pygame.K_a:
                    inputs["a"] += 1
                if event.key == pygame.K_s:
                    inputs["s"] += 1
                if event.key == pygame.K_d:
                    inputs["d"] += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                logging.info("mouseclick")

        return inputs
    def draw(self,obj):
        if obj.obj_type == "circle":
            pygame.draw.circle(self.screen,
                               obj.color,
                               (obj.x,obj.y),
                               obj.radius)
    def start_mainloop(self):
        #vaildation
        self.initial_pygame()
        self.gamestart = True
        game_engine = Engine()
        game_engine.create_obj()

        while self.gamestart:
            game_inputs = self.event_process(pygame.event.get())
            game_engine.update(game_inputs)
            self.screen.fill((0, 0, 0))
            self.draw(game_engine.objects[0])
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
def main():
    game_main = GraviShot()
    game_main.set_game_config(960,540)
    game_main.start_mainloop()
if __name__=="__main__":
    main()
