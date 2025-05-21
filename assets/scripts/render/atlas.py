import pygame
import json
import os
pygame.init()

pygame.display.set_mode((480,360))

def crop(surface: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2):
    output = pygame.Surface((size.x, size.y), pygame.SRCALPHA, 32).convert_alpha()
    output.blit(surface, (-position.x, -position.y))
    return output

def import_atlas(atlas: pygame.Surface, key: str):
    output = {}
    load = json.loads(key)
    for i in load:
        info = load[i]
        output[i] = crop(atlas, pygame.Vector2(info['x'], info['y']), pygame.Vector2(info['w'], info['h']))
    return output