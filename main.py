import assets.scripts.core.window as window
import pygame
import os; os.chdir(os.path.dirname(__file__))
import assets.scripts.render.atlas as atlas

#atlas.import_atlas(pygame.image.load('assets/art/tiles.png'), open("assets/data/render/art/tiles.json", "r").read())
#print(open("assets/data/render/art/tiles.json", "r").read())

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('window testing')
running = True

window.create_window('test_window', pygame.Vector2(64, 64), pygame.Vector2(4, 4))
window.create_window('test_window2', pygame.Vector2(400, 64), pygame.Vector2(10, 2), atlas_path='assets/art/tiles_high_contrast.png')
window.create_window('test_window3', pygame.Vector2(400, 400), pygame.Vector2(7, 3), atlas_path='assets/art/tiles_sleek.png')
window.set_window_caption('test_window', 'Window!', (234, 212, 170))
window.set_window_caption('test_window2', "I like this window, it\'s cool", (44, 232, 245))
window.set_window_caption('test_window3', "2 < 4", (255, 255, 255))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((38,43,68))
    window.tick_windows(screen, 4)
    pygame.display.flip()
    clock.tick(60)

    if pygame.K_F11 in pygame.key.get_just_pressed():
        pygame.display.toggle_fullscreen()
pygame.quit()