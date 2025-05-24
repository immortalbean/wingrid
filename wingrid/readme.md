# Requirements
- This package requires python 3.7 or above.
- You need pygame or pygame-ce. (Not included in install requirements due to possible conflict)
# Quickstart
For a simple 4x4 window, run this code:
``` python
import pygame
import wingrid
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

wingrid.create_window('test', pygame.Vector2(0,0), pygame.Vector2(4, 4), atlas_path=wingrid.THEME_TILES_PINK)
# Creates a window named "test" at the position (0, 0) with a size of 4x4.

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    wingrid.tick_windows(screen, 4)
	# Ticks all windows and draws them to the screen. Also scales them to 4x scale.
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
```
This creates a window with the pink theme, one of the included themes in WinGrid.
For more control, you can use this function to give the window a custom caption:
``` python
wingrid.set_window_caption('test', 'Caption!', (255, 255, 255))
# This sets the caption of our window named "test" to "Caption!", it also sets it's color to white. (255, 255, 255)
```