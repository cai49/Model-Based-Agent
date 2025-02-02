from math import floor
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pygame

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Window")

clock = pygame.time.Clock()

bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill((0,0,0))

gui = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
gui.fill(pygame.Color(0,0,0,0))

cell_number = 5
cell_size: int = floor(width / cell_number)
padding = cell_size / 2

grid_font = pygame.font.Font(None, 40)

map_tiles = np.random.randint(2, size=(cell_number, cell_number))
memory = np.zeros((cell_number, cell_number), dtype=int)

def render_text(surface: pygame.surface.Surface, font: pygame.font.Font, text: str, position:list[float], color=pygame.Color("white")):
    _render_text = font.render(text, True, color)
    _text_pos = _render_text.get_rect()
    _text_pos = _text_pos.move(position[0], position[1])
    surface.blit(_render_text, _text_pos)

def render_text_centered(surface: pygame.surface.Surface, font: pygame.font.Font, text: str, position:list[float], color=pygame.Color("white")):
    _render_text = font.render(text, True, color)
    _text_pos = _render_text.get_rect()
    _text_pos = _text_pos.move(position[0]-_render_text.get_width()/2, position[1]-_render_text.get_height()/2)
    surface.blit(_render_text, _text_pos)

is_rendering_gui = False
def render_gui():
    render_text(gui, grid_font, str(floor(clock.get_fps())), [5, 5], color=pygame.Color("brown2"))

def render_map():
    for _ix, _x in enumerate(map_tiles):
        for _jy, _y in enumerate(_x):
            _tile = _y
            memory_tile = "X" if memory[_ix][_jy] == 1 else "?"

            if _tile != 0:
                pygame.draw.rect(bg, pygame.Color("white"), pygame.Rect(_ix * cell_size, _jy * cell_size, cell_size, cell_size), 0)
                render_text_centered(bg, grid_font, memory_tile, [_ix * cell_size + padding, _jy * cell_size + padding + grid_font.size(memory_tile)[1]/2], pygame.Color("black"))
                render_text_centered(bg, grid_font, str(_tile), [_ix * cell_size + padding, _jy * cell_size + padding - grid_font.size(str(_tile))[1]/2], pygame.Color("black"))
            else:
                pygame.draw.rect(bg, pygame.Color("black"), pygame.Rect(_ix * cell_size, _jy * cell_size, cell_size, cell_size), 0)
                render_text_centered(bg, grid_font, memory_tile, [_ix * cell_size + padding, _jy * cell_size + padding + grid_font.size(memory_tile)[1]/2], pygame.Color("white"))
                render_text_centered(bg, grid_font, str(_tile), [_ix * cell_size + padding, _jy * cell_size + padding - grid_font.size(str(_tile))[1]/2], pygame.Color("white"))

            pygame.draw.rect(bg, pygame.Color("grey50"), pygame.Rect(_ix * cell_size, _jy * cell_size, cell_size, cell_size), 2)

running = True
while running:
    clock.tick(30)

    screen.fill(pygame.Color("black"))
    gui.fill(pygame.Color(0,0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_rendering_gui = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_rendering_gui = False

    if is_rendering_gui:
        render_gui()

    render_map()

    for i, x in enumerate(map_tiles):
        for j, y in enumerate(x):
            pass

    screen.blit(bg, (0, 0))
    screen.blit(gui, (0, 0))

    pygame.display.flip()

pygame.quit()
