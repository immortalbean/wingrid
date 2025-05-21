import assets.scripts.core.window as window
import pygame

import assets.scripts.render.atlas as atlas

atlas.import_atlas(pygame.image.load('assets/art/tiles.png'), open("assets/data/render/art/tiles.json", "r").read())
#print(open("assets/data/render/art/tiles.json", "r").read())
pygame.init()

screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock

running = True

window.create_window('test_window', pygame.Vector2(0,0), pygame.Vector2(4, 4))
window.create_window('test_window2', pygame.Vector2(192,0), pygame.Vector2(4, 4))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    window.tick_windows(screen, 3)
    pygame.display.flip()
pygame.quit()