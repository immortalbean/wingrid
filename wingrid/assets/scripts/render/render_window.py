
import pygame
from ..core import window as window
import math
from . import atlas
from ..core import locate
pygame.init()

cursor_move = pygame.image.load(locate.asset_path('art', 'cursor', 'move.png'))
def blur_surface(surface, scale_factor=1.0):
    size = surface.get_size()
    small = pygame.transform.smoothscale(surface, (int(size[0]*scale_factor), int(size[1]*scale_factor)))
    return pygame.transform.smoothscale(small, size)
def render(render_window: window._Window, surface: pygame.Surface, scale: int):
    if 'blur' in render_window.render_args:
        behind = atlas.crop(surface, pygame.Vector2(math.floor(render_window.position.x / scale) * scale, math.floor(
            render_window.position.y / scale) * scale), pygame.Vector2(render_window.size.x * scale * 16, render_window.size.y * scale * 16))
        blurred = blur_surface(behind, 1/scale)
        surface.blit(blurred, (
            math.floor(render_window.position.x / scale) * scale, math.floor(render_window.position.y / scale) * scale))

    render_window.surface.fill((0, 0, 0, 0))
    render_window.surface.blit(render_window.bg_surface, (0, 0))
    for i in render_window.elements:
        render_window.elements[i].draw(render_window)
    surface.blit(
        pygame.transform.scale_by(render_window.surface, scale),
        (
            math.floor(render_window.position.x / scale) * scale,
            math.floor(render_window.position.y / scale) * scale
        )
    )

    if render_window.moving_window:
        cursor_img = pygame.transform.scale_by(cursor_move, scale)
        surface.blit(
            cursor_img,
            (
                pygame.mouse.get_pos()[0] - cursor_img.get_width() / 2,
                pygame.mouse.get_pos()[1] - cursor_img.get_height() / 2
            )
        )
def bg_render(render_window: window._Window, caption_color: tuple = (255, 255, 255)):
    surface = render_window.bg_surface
    surface.fill((0, 0, 0, 0))

    w, h = int(render_window.size.x), int(render_window.size.y)

    atlas = render_window.atlas
    font_atlas = render_window.font_atlas

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

    for x in range(1, w - 1):
        for y in range(1, h - 1):
            surface.blit(atlas['bg_cc'], (x * 16, y * 16))
    pos_x = 0
    for i in render_window.caption:
        letter = i.lower()
        skip = False
        if letter in font_atlas:
            letter_surf = font_atlas[letter].copy()
        else:
            if i == ' ':
                skip = True
                letter_surf = font_atlas['missing'].copy()
            else:
                letter_surf = font_atlas['missing'].copy()
        if pos_x + 10 > (w * 16) - 2:
            letter_surf = font_atlas['...'].copy()
            letter_surf.fill(caption_color, special_flags=pygame.BLEND_MULT)
            surface.blit(letter_surf, (2 + pos_x, 2))
            break
        if not skip:
            letter_surf.fill(caption_color, special_flags=pygame.BLEND_MULT)
            surface.blit(letter_surf, (2+pos_x, 2))
        pos_x += 5