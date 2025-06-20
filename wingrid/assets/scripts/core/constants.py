import os

# Get the directory this file is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path helper
def asset_path(relative_path):
    return os.path.join(BASE_DIR, '..', '..', 'art', 'tiles', relative_path)

# Asset paths
THEME_TILES_DEFAULT = asset_path('tiles_default.png')
THEME_TILES_HIGH_CONTRAST = asset_path('tiles_high_contrast.png')
THEME_TILES_SLEEK = asset_path('tiles_sleek.png')
THEME_TILES_GRAY = asset_path('tiles_gray.png')
THEME_TILES_PINK = asset_path('tiles_pink.png')
THEME_TILES_GREEN = asset_path('tiles_green.png')
THEME_TILES_DARK = asset_path('tiles_dark.png')
THEME_TILES_WHITE = asset_path('tiles_white.png')
THEME_TILES_ORANGE = asset_path('tiles_orange.png')
THEME_TILES_PAPER = asset_path('tiles_paper.png')
THEME_TILES_CUBED = asset_path('tiles_cubed.png')
THEME_TILES_GLASS = asset_path('tiles_glass.png')
THEME_TILES_GRASS = asset_path('tiles_grass.png')
THEME_TILES_GRID_TEST = asset_path('grid_test.png')
TILE_BLUR_THEMES = [THEME_TILES_GLASS]