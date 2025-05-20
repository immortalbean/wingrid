import pygame
import assets.scripts.render.atlas as atlas

pygame.init()

windows = {}



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
        self.bg_surface = pygame.Surface((size.x * 16, size.y * 16))
        self.surface = pygame.Surface((size.x * 16, size.y * 16))
    def add_element(self, element: Element):
        if element:
            self.elements.append(element)
    def render(self, surface: pygame.Surface):
        import assets.scripts.render.render_window as render_window
        render_window.render(self, surface)

def create_window(name: str,  position: pygame.Vector2, size: pygame.Vector2, atlas_path: str = 'assets/art/tiles.png', font_atlas: str = 'assets/art/font.png'):
    created_window = Window(position, size, atlas_path, font_atlas)
    import assets.scripts.render.render_window as render_window
    render_window.bg_render(created_window)
    windows[name] = created_window
def render_windows(surface: pygame.Surface):
    for i in windows:
        windows[i].render(surface)