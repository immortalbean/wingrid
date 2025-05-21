import pygame
import assets.scripts.render.atlas as atlas
import sys
import inspect

pygame.init()

windows = {}

prev_mouse_position = pygame.mouse.get_pos(False)
mouse_position = pygame.mouse.get_pos(False)

class Element:
    def __init__(self, position: pygame.Vector2):
        self.position = position



class Window:
    def __init__(self, position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = 'assets/art/tiles.png', font_atlas: str = 'assets/art/font.png'):
        self.position = position
        self.size = pygame.Vector2(int(size.x), int(size.y))
        self.elements = []
        self.atlas = atlas.import_atlas(pygame.image.load(atlas_path), open("assets/data/render/art/tiles.json", "r").read()) #
        self.font_atlas = pygame.image.load(font_atlas)
        self.bg_surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.moving_window = False
    def add_element(self, element: Element):
        if element:
            self.elements.append(element)
    def tick(self, scale: int, behind_window: bool):
        global prev_mouse_position
        global mouse_position
        mouse_in_window = False
        if mouse_position[0] > self.position.x and mouse_position[1] > self.position.y:
            if mouse_position[0] < self.position.x + (self.size.x * 16 * scale) and mouse_position[1] < self.position.y + (self.size.y * 16 * scale):
                mouse_in_window = True
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_pressed():
            if mouse_position[0] > self.position.x and mouse_position[1] > self.position.y:
                if mouse_position[0] < self.position.x + (self.size.x * 16 * scale) and mouse_position[1] < self.position.y + (8 * scale):
                    if not behind_window:
                        self.moving_window = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
        else:
            if pygame.BUTTON_LEFT in pygame.mouse.get_just_released():
                self.moving_window = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if self.moving_window:
            self.position += pygame.Vector2(mouse_position[0] - prev_mouse_position[0], mouse_position[1] - prev_mouse_position[1])
        return mouse_in_window
    def render(self, surface: pygame.Surface, scale: int):
        import assets.scripts.render.render_window as render_window
        render_window.render(self, surface, scale)

def create_window(name: str,  position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = 'assets/art/tiles.png', font_atlas: str = 'assets/art/font.png'):
    if size.x < 2 or size.y < 2:
        caller = inspect.stack()[1]
        print(f"[WinGrid] Error: Window size must be at least 2x2. (line {caller.lineno} in {caller.filename})", file=sys.stderr)
        sys.exit(1)
    created_window = Window(position, size, atlas_path, font_atlas)
    import assets.scripts.render.render_window as render_window
    render_window.bg_render(created_window)
    windows[name] = created_window
def tick_windows(surface: pygame.Surface, scale: int):
    global prev_mouse_position
    global mouse_position
    prev_mouse_position = mouse_position
    mouse_position = pygame.mouse.get_pos()
    behind_window = False
    for i in reversed(windows):
        if windows[i].tick(scale, behind_window):
            behind_window = True
    for i in windows:
        windows[i].render(surface, scale)