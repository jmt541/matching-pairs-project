import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("test window")


#load asset
background_image = pygame.image.load("asset/background.png")




running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        screen.fill((30,30,30))

        screen.blit(background_image, (0,0))
        pygame.display.flip()


pygame.quit()        