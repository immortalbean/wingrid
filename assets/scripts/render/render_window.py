import pygame
#import assets.scripts.render.atlas as atlas
import assets.scripts.core.window as window
pygame.init()

def render(render_window: window.Window, surface: pygame.Surface):
    render_window.surface.fill((0,0,0,0))
    render_window.surface.blit(render_window.bg_surface)
    surface.blit(render_window.surface, (render_window.position.x,render_window.position.y))
def bg_render(render_window: window.Window):
    surface = render_window.bg_surface
    surface.blit(render_window.atlas['bg_tl'], (0,0))