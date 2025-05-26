import pygame
from ..render import atlas as atlas
import sys
import inspect
from . import constants
from . import locate
from . import window

class Button(window.Element):
    def __init__(self, name: str,position: pygame.Vector2, size: int, text: str = '', text_color: tuple = (255, 255, 255), atlas_path: str = constants.THEME_TILES_DEFAULT):
        super().__init__(name, position, atlas_path)
        if size < 2:
            caller = inspect.stack()[1]
            print(f"[WinGrid] Error: Buttons need to be atleast 2 tiles wide. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
            sys.exit(2)
        raw_font_atlas = pygame.image.load(locate.asset_path( 'art', 'font.png'))
        raw_font_atlas.fill(text_color, special_flags=pygame.BLEND_MULT)
        self.font_atlas = atlas.import_atlas(raw_font_atlas,
        open(locate.asset_path('data', 'render', 'art', 'font.json'), "r").read())
        self.size = size
        self.text = text
        self.pressed = False
    def check_mouse_inside(self, mouse_position: tuple):
        if (self.position[0] * 16 + 3) < mouse_position[0] < (self.position[0] * 16 - 3 + self.size * 16):
            if (self.position[1] * 16 + 3) < mouse_position[1] < (self.position[1] * 16 + 13):
                return True
            else:
                return False
        else:
            return False
    def tick(self, mouse_position: tuple):
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_pressed() and self.check_mouse_inside(mouse_position):
            self.pressed = True
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_released():
            if self.check_mouse_inside(mouse_position):
                self.event()
            self.pressed = False

    def draw(self, window_surface: pygame.Surface):
        if self.pressed:
            parts = [self.atlas['button_l_pressed'], self.atlas['button_c_pressed'], self.atlas['button_r_pressed']]
        else:
            parts = [self.atlas['button_l'], self.atlas['button_c'], self.atlas['button_r']]
        window_surface.blit(parts[0], (self.position[0] * 16, self.position[1] * 16))
        window_surface.blit(parts[2], ((self.size - 1) * 16 + self.position[0] * 16, self.position[1] * 16))
        for i in range(1, self.size - 1):
            window_surface.blit(parts[1], (self.position[0] * 16 + i * 16, self.position[1] * 16))
        pos_x = 0
        for i in self.text:
            letter = i.lower()
            skip = False
            if letter in self.font_atlas:
                letter_surf = self.font_atlas[letter].copy()
            else:
                if i == ' ':
                    skip = True
                    letter_surf = self.font_atlas['missing'].copy()
                else:
                    letter_surf = self.font_atlas['missing'].copy()
            if pos_x + 10 > (self.size * 16) - 6:
                letter_surf = self.font_atlas['...'].copy()
                window_surface.blit(letter_surf, (6 + pos_x + self.position[0] * 16, 6 + self.position[1] * 16))
                break
            if not skip:
                window_surface.blit(letter_surf, (6 + pos_x + self.position[0] * 16, 6 + self.position[1] * 16))
            pos_x += 5