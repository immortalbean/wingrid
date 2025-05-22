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
    surface.fill((0, 0, 0, 0))

    w, h = int(render_window.size.x), int(render_window.size.y)

    atlas = render_window.atlas

    surface.blit(atlas['bg_tl'], (0, 0))
    surface.blit(atlas['bg_tr'], ((w - 1) * 16, 0))
    surface.blit(atlas['bg_bl'], (0, (h - 1) * 16))
    surface.blit(atlas['bg_br'], ((w - 1) * 16, (h - 1) * 16))

    for x in range(1, w - 1):
        surface.blit(atlas['bg_tc'], (x * 16, 0))
        surface.blit(atlas['bg_bc'], (x * 16, (h - 1) * 16))

    for y in range(1, h - 1):
        surface.blit(atlas['bg_cl'], (0, y * 16))
        surface.blit(atlas['bg_cr'], ((w - 1) * 16, y * 16))

    # Center tiles
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            surface.blit(atlas['bg_cc'], (x * 16, y * 16))
