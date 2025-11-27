import pygame
import copy
from ..render import atlas as atlas
import sys
import inspect
from . import constants
from . import locate

pygame.init()

windows = {}

class Element:
    def __init__(self, name: str,position: pygame.Vector2):
        self.name = name
        self.position = position
        self.parented = False
        self.size = pygame.Vector2(1,1)
    def event(self):
        pass
    def tick(self, mouse_position: tuple):
        pass
    def draw(self, window_surface: pygame.Surface):
        pass
    def clone(self, name: str = ""):
        clone = copy.copy(self)
        clone.parented = False
        if name:
            clone.name = name
        else:
            clone.name = clone.name + "2"
        return clone
    def __str__(self):
        return self.name



class _Window:
    def __init__(self, name: str, position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = constants.THEME_TILES_DEFAULT, font_atlas: str = locate.asset_path( 'art', 'font.png')):
        caller_frame = inspect.stack()[1]
        caller_filename = caller_frame.filename
        caller_function = caller_frame.function
        if caller_function != 'create_window':
            print(
                f"[WinGrid error 001] Error: WOAH BUDDY, please create windows with 'create_window()' instead of directly instantiating Window. Called from {caller_filename}:{caller_frame.lineno}",
                file=sys.stderr)
            sys.exit(2)
        self.name = name
        self.caption = ''
        self.position = position
        self.size = pygame.Vector2(int(size.x), int(size.y))
        self.elements = {}
        self.render_args = []
        if atlas_path in constants.DEFAULT_THEME_ARGS:
            self.render_args.append(constants.DEFAULT_THEME_ARGS[atlas_path])
        self.atlas = atlas.import_atlas(pygame.image.load(atlas_path), open(locate.asset_path('data', 'render', 'art', 'tiles.json'), "r").read())
        self.font_atlas = atlas.import_atlas(pygame.image.load(font_atlas), open(locate.asset_path('data', 'render', 'art', 'font.json'), "r").read())
        self.bg_surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.surface = pygame.Surface((size.x * 16, size.y * 16), pygame.SRCALPHA, 32).convert_alpha()
        self.moving_window = False
        self.movable = True
    def add_element(self, *elements: Element):
        for element in elements: # So that I don't have to desipher this again, it loops over the added elements, not the ones already in the window.
            if element.parented:
                caller = inspect.stack()[1]
                print(f"[WinGrid error 002] Error: Element is already in another window, adding it to this one can cause conflicts. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
                sys.exit(2)
            #if element.position[0] < 0 or element.size[0] + int(element.position[0]) > self.size[0] or element.position[1] < 1 or self.size[1] < element.position[1]:
            #    caller = inspect.stack()[1]
            #    print(f"[WinGrid] Error: Element is out of window's bounds. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
            #    sys.exit(2)
            elif element.name in self.elements:
                caller = inspect.stack()[1]
                print(f"[WinGrid error 003] Error: Name already used, please use a unique name or make sure element isn't already in that window. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
                sys.exit(2)
            else:
                if element:
                    self.elements[element.name] = element
            element.parented = True
    def get_element(self, element: str):
        if element in self.elements:
            return self.elements[element]
        else:
            caller = inspect.stack()[1]
            print(f"[WinGrid error 004] Warning: Element {element} does not exist. Check your code for typos or inconsistencies. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
            return None
    def tick(self, scale: int, behind_window: bool, surface: pygame.Surface):
        mouse_position = pygame.mouse.get_pos()
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
                    print(f"[WinGrid error 005] Error: Please create windows with the 'create_window()' function, instead of directly using the class. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
                    sys.exit(2)
                if mouse_position[1] < self.position.y + (8 * scale):
                    if self.movable:
                        self.moving_window = True
                        self._relative_mouse_position = pygame.mouse.get_pos() - self.position
                        pygame.mouse.set_visible(False)

        else:
            if pygame.BUTTON_LEFT in pygame.mouse.get_just_released():
                if self.moving_window and self.movable:
                    self.moving_window = False
                    pygame.mouse.set_visible(True)
                    try:
                        del self._relative_mouse_position
                    except AttributeError:
                        pass
        if not behind_window:
            for i in self.elements:
                self.elements[i].tick(((mouse_position[0] - self.position[0]) / scale, (mouse_position[1] - self.position[1]) / scale))
        if self.moving_window:
            self.position = pygame.mouse.get_pos() - self._relative_mouse_position
        self.position.x = min(max(self.position.x, 0), surface.size[0] - (self.size.x * 16 * scale))
        self.position.y = min(max(self.position.y, 0), surface.size[1] - (8 * scale))
        return mouse_in_window
    def render(self, surface: pygame.Surface, scale: int):
        from ..render import render_window as render_window
        render_window.render(self, surface, scale)

    def set_theme(self, atlas_path: str = constants.THEME_TILES_DEFAULT, caption_color: tuple[int, int, int] = (255, 255, 255)):
        self.atlas = atlas.import_atlas(pygame.image.load(atlas_path),open(locate.asset_path('data', 'render', 'art', 'tiles.json'), "r").read())
        from ..render import render_window as render_window
        render_window.bg_render(render_window=self, caption_color=caption_color)

def create_window(name: str,  position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = constants.THEME_TILES_DEFAULT,
font_atlas: str = locate.asset_path('art', 'font.png'), movable: bool = True,replace: bool = False,caption: str = '',caption_color: tuple[int, int, int] = (255, 255, 255)):
    if name in windows:
        if replace:
            destroy_window(name)
        else:
            caller = inspect.stack()[1]
            print(
                f"[WinGrid error 006] Error: Window already exists. (line {caller.lineno} in {caller.filename}) \n If you intended to replace the existing window, add \"replace=True\" to the arguments."
            ,file=sys.stderr)
            sys.exit(2)
    if size.x < 2 or size.y < 2:
        caller = inspect.stack()[1]
        print(f"[WinGrid error 007] Error: Window size must be at least 2x2. (line {caller.lineno} in {caller.filename})", file=sys.stderr)
        sys.exit(2)
    created_window = _Window(name, position, size, atlas_path, font_atlas)
    if caption:
        created_window.caption = caption
    else:
        created_window.caption = name
    created_window.movable = movable
    from ..render import render_window
    render_window.bg_render(created_window, caption_color)
    windows[name] = created_window
    return created_window
def tick_windows(surface: pygame.Surface, scale: int):
    behind_window = False
    reversed_windows = reversed(list(windows.values()))
    for i in reversed_windows:
        if i.tick(scale, behind_window, surface):
            behind_window = True
    for i in windows:
        windows[i].render(surface, scale)
def set_window_caption(window_name: str, caption: str, color: tuple[int, int, int] = (255, 255, 255)):
    if window_name in windows:
        windows[window_name].caption = caption
        from ..render import render_window as render_window
        render_window.bg_render(windows[window_name], color)
    else:
        caller = inspect.stack()[1]
        print(f"[WinGrid error 008] Error: Window does not exist. (line {caller.lineno} in {caller.filename})", file=sys.stderr)
        sys.exit(2)
def get_window(window_name: str):
    if window_name in windows:
        return windows[window_name]
    else:
        caller = inspect.stack()[1]
        print(f"[WinGrid error 009] Error: Window does not exist. (line {caller.lineno} in {caller.filename})",file=sys.stderr)
        sys.exit(2)
def destroy_window(window_name: str) -> bool:
    if window_name in windows:
        windows.pop(window_name)
        return True
    else:
        print(f"[WinGrid error 010] Warning: Window ({window_name}) does not exist.")
        return False