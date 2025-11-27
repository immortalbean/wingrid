# Buttons

Wingrid has simple, built-in support for buttons.

![A test demo using WinGrid's button system](/images/docs/buttons.gif)

# Adding a button

To add a button to a (prexisting) window, create a variable using the button class,
and use the add_element() on the window you want to add it to.
```python
import wingrid
import pygame

example_window = wingrid.create_window('example_window', pygame.Vector2(0,0), pygame.Vector2(4,3))
# Creates a window.

example_button = wingrid.Button('example_button', pygame.Vector2(0, 1), 4, 'example')
# Creates a button at the position (0, 1) with a size of 4. 
# This button will have the text "example" on it.

example_window.add_element(example_button)
# Adds the button to the window.
```

This creates this window:

![A window with an example button](/images/docs/example_button.png)

> [!Warning]
> When a button is placed on a window, it cannot exceed the window's bounds, or else the program will crash. See valid bounds below:
>
>![Window bounds](/images/docs/areas.png)

# Click detection
For obvious reasons, it is important for your programs to be able to detect button input.

You can check if a button was just pressed using the just_pressed() function.

```python
import wingrid
import pygame
window = wingrid.create_window('example_win', pygame.Vector2(0,0), pygame.Vector2(4, 4))
button = wingrid.Button('example', pygame.Vector2(0, 1), 4)

while True:
    # Loop abbreviated to prevent bloat
    if button.just_pressed():
        print("Pressed!")
```