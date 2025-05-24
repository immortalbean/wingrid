import pygame
import ...render.atlas as atlas
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
    def __init__(self, name: str, position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = 'assets/art/tiles_default.png', font_atlas: str = 'assets/art/font.png'):
        self.name = name
        self.caption = name
        self.position = position
        self.size = pygame.Vector2(int(size.x), int(size.y))
        self.elements = []
        self.atlas = atlas.import_atlas(pygame.image.load(atlas_path), open("assets/data/render/art/tiles.json", "r").read())
        self.font_atlas = atlas.import_atlas(pygame.image.load(font_atlas), open("assets/data/render/art/font.json", "r").read())
        self.bg_surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.moving_window = False
    def add_element(self, element: Element):
        if element:
            self.elements.append(element)
    def tick(self, scale: int, behind_window: bool, surface: pygame.Surface):
        global prev_mouse_position
        global mouse_position
        mouse_in_window = False
        if mouse_position[0] > self.position.x and mouse_position[1] > self.position.y:
            if mouse_position[0] < self.position.x + (self.size.x * 16 * scale) and mouse_position[1] < self.position.y + (self.size.y * 16 * scale):
                mouse_in_window = True
        if pygame.BUTTON_LEFT in pygame.mouse.get_just_pressed() and not behind_window:
            if mouse_in_window:
                global windows
                if self.name in windows:
                    item = windows.pop(self.name)
                    windows[self.name] = item
                else:
                    caller = inspect.stack()[1]
                    print(f"[WinGrid] Error: Please create windows with the 'create_window()' function, instead of directly using the class. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
                    sys.exit(2)
                if mouse_position[0] > self.position.x and mouse_position[1] > self.position.y:
                    if mouse_position[0] < self.position.x + (self.size.x * 16 * scale) and mouse_position[1] < self.position.y + (8 * scale):
                        self.moving_window = True
                        self._relative_mouse_position = pygame.mouse.get_pos() - self.position
                        pygame.mouse.set_visible(False)
        else:
            if pygame.BUTTON_LEFT in pygame.mouse.get_just_released():
                self.moving_window = False
                pygame.mouse.set_visible(True)
                try:
                    del self._relative_mouse_position
                except AttributeError:
                    pass
        if self.moving_window:
            self.position = pygame.mouse.get_pos() - self._relative_mouse_position
        self.position.x = min(max(self.position.x, 0), surface.size[0] - (self.size.x * 16 * scale))
        self.position.y = min(max(self.position.y, 0), surface.size[1] - (8 * scale))
        return mouse_in_window
    def render(self, surface: pygame.Surface, scale: int):
        import ...render.render_window as render_window
        render_window.render(self, surface, scale)

def create_window(name: str,  position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = 'assets/art/tiles_default.png', font_atlas: str = 'assets/art/font.png'):
    if size.x < 2 or size.y < 2:
        caller = inspect.stack()[1]
        print(f"[WinGrid] Error: Window size must be at least 2x2. (line {caller.lineno} in {caller.filename})", file=sys.stderr)
        sys.exit(2)
    created_window = Window(name, position, size, atlas_path, font_atlas)
    import ...render.render_window as render_window
    render_window.bg_render(created_window)
    windows[name] = created_window
def tick_windows(surface: pygame.Surface, scale: int):
    global prev_mouse_position
    global mouse_position
    prev_mouse_position = mouse_position
    mouse_position = pygame.mouse.get_pos()
    behind_window = False
    reversed_windows = reversed(windows)
    for i in reversed_windows:
        if windows[i].tick(scale, behind_window, surface):
            behind_window = True
    for i in windows:
        windows[i].render(surface, scale)
def set_window_caption(window_name: str, caption: str, color: tuple = (255, 255, 255)):
    windows[window_name].caption = caption
    import ...render.render_window as render_window
    render_window.bg_render(windows[window_name], color)
def get_window(window_name: str):
    if window_name in windows:
        return windows[window_name]
    else:
        caller = inspect.stack()[1]
        print(f"[WinGrid] Error: Window does not exist. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
        sys.exit(2)