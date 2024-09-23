from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
movex = 5
y = 90
movey = 0


while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x = x + movex
    y = y + movey
    if x >= 800 and y <= 90:
        movex = 0
        movey = 5
    elif x >= 800 and y >= 600:
        movex = -5
        movey = 0
    elif x <= 0 and y >= 600:
        movex = 0
        movey = -5
    elif x <= 0 and y <= 90:
        movex = 5
        movey = 0
    delay(0.01)

