import pygame
from sys import exit

class Agent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        agent_idle_0 = pygame.image.load('graphics/idle0.png').convert_alpha()
        agent_idle_1 = pygame.image.load('graphics/idle1.png').convert_alpha()
        agent_idle_2 = pygame.image.load('graphics/idle2.png').convert_alpha()
        agent_idle_3 = pygame.image.load('graphics/idle3.png').convert_alpha()
        self.player_idle = [agent_idle_0, agent_idle_1, agent_idle_2, agent_idle_3]
        self.player_index = 0
        self.image = self.player_idle[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))

    def animation_state(self):
        self.player_index += 0.1
        if self.player_index >= len(self.player_idle):
            self.player_index = 0
        self.image = self.player_idle[int(self.player_index)]

    def update(self):
        self.animation_state()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("First habitation")
    clock = pygame.time.Clock()

    # agent
    agent = pygame.sprite.GroupSingle()
    agent.add(Agent())

    # assets
    background = pygame.image.load('graphics/white_cloud.jpg').convert()
    #ground = pygame.image.load('graphics/ground.png').convert()
    ground = pygame.Surface((800, 100))
    ground.fill('black')
    game_active = True

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not game_active:
                if event.type == pygame.K_SPACE:
                    game_active = True

        if game_active:
            # draw all elements
            screen.blit(background, (0,0)) # put one surface on another
            screen.blit(ground, (0, 300))

            agent.draw(screen)
            agent.update()


        # update everything
        pygame.display.update()
        clock.tick(60) # set max framerate