# Elements
# wingrid.Element
The basic element class used by WinGrid. Cannot be used on its own.

**Parameters:**
- name: str - The name used to identify elements.
- position: pygame.Vector - The default position of an element, in tiles.

# wingrid.Element.event()
Deprecated, previously used to run code through, for example, a button press.
# wingrid.Element.clone()
Creates and returns a clone of the element.

**Parameters:**
> None.

**Returns:**
> An exact copy of the element, to be parented to a different window.

**Return type:**
> wingrid.Element

# wingrid.Element.tick()
The element's update function, called every frame. Called by the element's parent window.

**Parameters:**
- mouse_position: tuple - The mouse position, in pixels, relative to the top-left corner of the window

**Returns:**
>None.
# wingrid.Element.draw()
The element's draw function, called every frame by the element's parent window.

**Parameters:**
- render_window: wingrid._Window - The window the element is rendered on, contains the surface and atlas

**Returns:**
> None.