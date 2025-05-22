import assets.scripts.core.window as window
import pygame
import os; os.chdir(os.path.dirname(__file__))
import assets.scripts.render.atlas as atlas

#atlas.import_atlas(pygame.image.load('assets/art/tiles.png'), open("assets/data/render/art/tiles.json", "r").read())
#print(open("assets/data/render/art/tiles.json", "r").read())
pygame.init()

screen = pygame.display.set_mode((960, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()

running = True

window.create_window('test_window', pygame.Vector2(0,0), pygame.Vector2(4, 4))
window.create_window('test_window2', pygame.Vector2(256,0), pygame.Vector2(4, 4), atlas_path='assets/art/tiles_high_contrast.png')
window.create_window('test_window3', pygame.Vector2(0,256), pygame.Vector2(3, 3), atlas_path='assets/art/tiles_sleek.png')
window.create_window('test_window4', pygame.Vector2(192,256), pygame.Vector2(3, 4), atlas_path='assets/art/tiles_dark.png')
window.create_window('test_window5', pygame.Vector2(384,256), pygame.Vector2(3, 4), atlas_path='assets/art/tiles_green.png')

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    window.tick_windows(screen, 4)
    pygame.display.flip()
    clock.tick(60)
    if pygame.K_F11 in pygame.key.get_just_pressed():
        pygame.display.toggle_fullscreen()
pygame.quit()