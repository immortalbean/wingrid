import assets.scripts.core.window as window
import pygame
import os; os.chdir(os.path.dirname(__file__))

#atlas.import_atlas(pygame.image.load('assets/art/tiles.png'), open("assets/data/render/art/tiles.json", "r").read())
#print(open("assets/data/render/art/tiles.json", "r").read())

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('window testing')
running = True

window.create_window('test_window01', pygame.Vector2(64, 64), pygame.Vector2(5, 5))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    window.tick_windows(screen, 4)
    pygame.display.flip()
    clock.tick(60)

    if pygame.K_F11 in pygame.key.get_just_pressed():
        pygame.display.toggle_fullscreen()
pygame.quit()