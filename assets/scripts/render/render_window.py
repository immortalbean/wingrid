import random

import pygame
#import assets.scripts.render.atlas as atlas
import assets.scripts.core.window as window
pygame.init()

def render(render_window: window.Window, surface: pygame.Surface, scale: int):
    render_window.surface.fill((0,0,0,0))
    render_window.surface.blit(render_window.bg_surface)
    surface.blit(pygame.transform.scale_by(render_window.surface, scale), (render_window.position.x,render_window.position.y))
def bg_render(render_window: window.Window):
    surface = render_window.bg_surface
    surface.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    surface.blit(render_window.atlas['bg_tl'], (0,0))
    len = 1
    while render_window.size.x - 1 > len:
        surface.blit(render_window.atlas['bg_tc'], (len * 16, 0))
        len += 1
    surface.blit(render_window.atlas['bg_tr'], (render_window.size.x * 16 - 16, 0))