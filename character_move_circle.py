from pico2d import *
import os
import math

os.chdir('C:\\Git\\2DGP\\2DGP-Drill-2')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

r = 270
x = math.sin(r) * 400
y = math.cos(r) * 300

while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    r = r + 1
    x = math.sin(r) * 400 + 400
    y = math.cos(r) * 300 + 300
    delay(0.01)

