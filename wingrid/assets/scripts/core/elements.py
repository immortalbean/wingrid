import pygame
from ..render import atlas as atlas
import sys
import inspect
from . import constants
from . import locate
from . import window

class Button(window.Element):
    def __init__(self, name: str,position: pygame.Vector2, size: int, text: str = '', text_color: tuple = (255, 255, 255)):
        super().__init__(name, position)
        if size < 2:
            caller = inspect.stack()[1]
            print(f"[WinGrid] Error: Buttons need to be atleast 2 tiles wide. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
            sys.exit(2)
        raw_font_atlas = pygame.image.load(locate.asset_path( 'art', 'font.png'))
        raw_font_atlas.fill(text_color, special_flags=pygame.BLEND_MULT)
        self.font_atlas = atlas.import_atlas(raw_font_atlas,
        open(locate.asset_path('data', 'render', 'art', 'font.json'), "r").read())
        self.size[0] = size
        self.text = text
        self.pressed = False
        self.is_mouse_over = False
    def check_mouse_inside(self, mouse_position: tuple):
        if (self.position[0] * 16 + 3) < mouse_position[0] < (self.position[0] * 16 - 3 + self.size * 16):
            if (self.position[1] * 16 + 3) < mouse_position[1] < (self.position[1] * 16 + 13):
                return True
            else:
                return False
        else:
            return False
    def tick(self, mouse_position: tuple):
        self.is_mouse_over = self.check_mouse_inside(mouse_position)
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_pressed():
            if self.is_mouse_over:
                self.pressed = True
                self.event()
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_released():
            self.pressed = False
    def just_pressed(self):
        return self.pressed and pygame.BUTTON_LEFT in pygame.mouse.get_just_pressed()
    def draw(self, render_window: window._Window):
        if self.pressed:
            parts = [render_window.atlas['button_l_pressed'], render_window.atlas['button_c_pressed'], render_window.atlas['button_r_pressed']]
        else:
            parts = [render_window.atlas['button_l'], render_window.atlas['button_c'], render_window.atlas['button_r']]
        render_window.surface.blit(parts[0], (self.position[0] * 16, self.position[1] * 16))
        render_window.surface.blit(parts[2], ((self.size - 1) * 16 + self.position[0] * 16, self.position[1] * 16))
        for i in range(1, self.size - 1):
            render_window.surface.blit(parts[1], (self.position[0] * 16 + i * 16, self.position[1] * 16))
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
                render_window.surface.blit(letter_surf, (6 + pos_x + self.position[0] * 16, 6 + self.position[1] * 16))
                break
            if not skip:
                render_window.surface.blit(letter_surf, (6 + pos_x + self.position[0] * 16, 6 + self.position[1] * 16))
            pos_x += 5
class Slider(window.Element):
    def __init__(self, name: str, pos: pygame.Vector2, length_tiles: int, slider_range: tuple[float, float] = (0.0, 1.0)):
        super().__init__(name, pos)
        self.size[0] = length_tiles
        self._value = 0.5
        self.dragging = False
        self.range = slider_range

    def tick(self, mouse_position):
        mx, my = mouse_position
        tile_px = 16
        track_tiles = self.size[0] - 3
        track_length = track_tiles * tile_px + 16
        track_start_x = (self.position.x + 1) * tile_px - 8
        track_y = self.position.y * tile_px + tile_px // 2
        knob_radius = 6
        knob_x = track_start_x + self._value * track_length

        just_pressed = pygame.mouse.get_just_pressed()
        pressed_buttons = pygame.mouse.get_pressed()
        mouse_down = pressed_buttons[0]  # left button pressed bool

        if 1 in just_pressed and not self.dragging:  # 1 is left mouse button
            if abs(mx - knob_x) < knob_radius and abs(my - track_y) < knob_radius:
                self.dragging = True

        if self.dragging and mouse_down:
            rel_x = mx - track_start_x
            self._value = max(0.0, min(1.0, rel_x / track_length))

        if not mouse_down:
            self.dragging = False

    def draw(self, render_window: window._Window):
        surface = render_window.surface
        tile_px = 16
        x = int(self.position.x * tile_px)
        y = int(self.position.y * tile_px)

        surface.blit(render_window.atlas["slider_l"], (x, y))

        track_tiles = int(self.size[0] - 3)
        for i in range(track_tiles):
            surface.blit(render_window.atlas["slider_c"], (x + tile_px * (i + 1), y))

        surface.blit(render_window.atlas["slider_seperate"], (x + tile_px * (track_tiles + 1), y))

        surface.blit(render_window.atlas["slider_r"], (x + tile_px * (track_tiles + 2), y))

        knob_x = x + tile_px * 1 - 8 + self._value * (track_tiles * tile_px + 16)
        knob_y = y + tile_px // 2
        knob_surface = render_window.atlas["slider_knob"]
        knob_rect = knob_surface.get_rect(center=(int(knob_x), int(knob_y)))
        surface.blit(knob_surface, knob_rect)
        final_value = self.range[0] + self._value * (self.range[1] - self.range[0])
        value_str = f"{float(int(final_value * 10)) / 10.0}"
        font_atlas = render_window.font_atlas
        max_width = 16
        label_x = x + tile_px * (track_tiles + 1) + 12
        label_y = y + (tile_px - 4) // 2

        pos_x = label_x
        for ch in value_str:
            ch_low = ch.lower()
            if ch_low in font_atlas:
                letter_surf = font_atlas[ch_low].copy()
            else:
                letter_surf = font_atlas["missing"].copy()

            if pos_x + 4 > label_x + max_width:
                ellipsis_surf = font_atlas["..."].copy()
                ellipsis_surf.fill((255, 255, 255), special_flags=pygame.BLEND_MULT)
                surface.blit(ellipsis_surf, (pos_x, label_y))
                break

            letter_surf.fill((255, 255, 255), special_flags=pygame.BLEND_MULT)
            surface.blit(letter_surf, (pos_x, label_y))
            pos_x += 5
    def get_value(self):
        return self.range[0] + self._value * (self.range[1] - self.range[0])
class InternalSurface(window.Element):
    def __init__(self, name: str, position: pygame.Vector2, size: pygame.Vector2 = pygame.Vector2(2,2)):
        super().__init__(name, position)
        if min(size.x, size.y) < 2:
            caller = inspect.stack()[1]
            print(f"[WinGrid] Error: Internal Surfaces must have a size of atleast 2x2. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
            sys.exit(2)
        self.size = size
        self.surface = pygame.Surface((size.x * 16 - 8, size.y * 16 - 8))
    def draw(self, render_window: window._Window):
        render_window.surface.blit(self.surface, (self.position[0] * 16 + 4, self.position[1] * 16 + 4))
        