# Window creation and properties

Despite how quick and easy it is to create and set up a window, WinGrid gives developers a ton of control.

# wingrid._Window():

The private window class internally used by WinGrid. This class contains all information stored by a window, like its position, size, and elements.

> [!Warning]
> Any window you create should be instantiated with the create_window() function, unless you know what you're doing. Not doing this causes the window to be fully ignored by WinGrid.

# wingrid.create_window()

Creates a window and properly instantiates it.

**Parameters:**

- name: str - The name of the window, not to be confused with the caption, as this is for identification.
- position: pygame.Vector2 - The position of the window, in pixels.
- size: pygame.Vector2 - The size of the window, in tiles. (16x16 pixel areas)
- atlas_path: str - (Optional) The location of the window's tile atlas, usually from the theme constants.
- font_atlas: str - (Optional) The location of the window's font atlas.
- movable: bool - (Optional) Whether the window is movable or not, helpful for animating the window through code.
- replace: bool - (Optional) If you input a window with the same name as another, adding replace will replace it instead of causing an error.
- caption: str - (Optional) The window's caption, without this it defaults to the window's name.
- caption_color: tuple[int, int, int] - (Optional) The color of the window's caption.

**Returns:**

>The window instance, required to be able to add elements to the window.
	
**Return type:**

>wingrid._Window - The internal window class, used to control default window behaviour.

# wingrid.set_window_caption()

Sets a window's caption.

**Parameters:**

- window_name: str - The identifying string name that each window is given.
- caption: str - The caption (text on the top bar) that the window will be given.
- caption_color: tuple[int, int, int] - (Optional) The color of the caption, by default this is white (255, 255, 255)

**Returns:**

>None.

# wingrid.destroy_window()

Destroys/deletes a window.
> [!Warning]
> Does not guarantee that all references to the window are destroyed

**Parameters:**

- window_name: str - The identifying string name that each window is given.

**Returns:**

>A boolean that states whether the window was successfully destroyed. If not, WinGrid raises a soft error (warning) to prevent possible crashes.
	
**Return type:**

>boolean

# wingrid._Window.set_theme()

Allows you to set the window's tile atlas after it was created.

**Parameters:**

- atlas_path: str - (Optional) The path of the window's atlas, usually one of the theme constants. Falls back to the default window theme.

**Returns:**

>None.

# wingrid._Window.add_element()

Adds an element to a window.

**Parameters:**

- element: wingrid.Element - The element you wish to add to the window, cannot be added to another window already.

**Returns:**

>None.
 
# wingrid._Window.get_element()

Gets the instance of a specific element within a window.

**Parameters:**

- element: str - The name of the element.

**Returns:**

>The element associated with the string name.
 
**Return type:**

>wingrid.Element - The basic element class used by WinGrid

# wingrid._Window.remove_element()

Removes an element from a window and returns the element.
> [!Warning]
> Does not guarantee that all references to the element are destroyed

**Parameters:**

- element: str - The name of the element.

**Returns:**

> A reference to the removed element.

**Return type:**

> wingrid.Element - The basic element class used by WinGrid

# Theme constants
The pre-included themes that WinGrid has by default. These include:
- Default - callable with wingrid.THEME_TILES_DEFAULT
- High contrast - callable with wingrid.THEME_TILES_HIGH_CONTRAST
- Sleek - callable with wingrid.THEME_TILES_SLEEK
- Gray - callable with wingrid.THEME_TILES_GRAY
- Pink - callable with wingrid.THEME_TILES_PINK
- Green - callable with wingrid.THEME_TILES_GREEN
- Dark - callable with wingrid.THEME_TILES_DARK
- White - callable with wingrid.THEME_TILES_WHITE
- Orange - callable with wingrid.THEME_TILES_ORANGE
- Notebook paper - callable with wingrid.THEME_TILES_PAPER
- Cubed - callable with wingrid.THEME_TILES_CUBED
- Frosted glass - callable with wingrid.THEME_TILES_GLASS
- Grass - callable with wingrid.THEME_TILES_GRASS

These themes are pictured below:

![The WinGrid themes](/images/docs/themes.png)