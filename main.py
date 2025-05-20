import assets.scripts.core.window as window
import pygame

import assets.scripts.render.atlas as atlas

atlas.import_atlas(pygame.image.load('assets/art/tiles.png'), open("assets/data/render/art/tiles.json", "r").read())
#print(open("assets/data/render/art/tiles.json", "r").read())
pygame.init()

screen = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock

running = True

window.create_window('test_window', pygame.Vector2(0,0), pygame.Vector2(4, 4))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.render_windows(screen)
    pygame.display.flip()
pygame.quit()