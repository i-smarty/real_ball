import tkinter
from Wall import Wall
from Ball import Ball
from System import System

master = tkinter.Tk()

p = 100  # padding
h = 2 * p + 482  # height of the canvas
w = 2 * p + 482  # width of the canvas

master.title('Ball')
master.minsize(800, 700)

canvas = tkinter.Canvas(master, bg='green', height=h, width=w)

mu = 1  # friction coefficient
k = 1  # coefficient of recovery

ball_list = [
    Ball(140, 341, 40, 5, 0, 1, 0.0000001, [7, 0], 0, (0, 0), canvas),
    Ball(185, 185, 20, 2.5, 0, 1, 0.0000001, [0, 15], 0, (0, 0), canvas),
    # Ball(x, y, R, r, alpha, m, I, v, omega, g, canvas, ball_canvas_args={}, spot_canvas_args={})
    # Ball(300, 500, 50, 5, 0, 2.777, 0.4 * 2.777 * 50 ** 2, [0, 0], 15, (1, -1), canvas,  # Большой и толстый
    #      ball_canvas_args={
    #          "fill": "blue"
    #      }),
    Ball(300, 300, 30, 5, 0, 1, 0.4 * 1 * 30 ** 2, [0, 5], -0.2, (0, 1), canvas,
         ball_canvas_args={
             "fill": "yellow"
         }),
    Ball(251, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(271, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(291, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(311, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(331, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(351, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(371, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(391, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(411, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
    Ball(431, 110, 10, 2.5, 0, 1, 0.4 * 1 * 10 ** 2, [0, 0], 0, (0, -1), canvas),
]

wall_list = [
    Wall(p, 141 + p, 141 + p, p, canvas),
    Wall(141 + p, p, 341 + p, p, canvas),
    Wall(341 + p, p, 482 + p, 141 + p, canvas),
    Wall(482 + p, 141 + p, 482 + p, 341 + p, canvas),
    Wall(482 + p, 341 + p, 341 + p, 482 + p, canvas),
    Wall(341 + p, 482 + p, 141 + p, 482 + p, canvas),
    Wall(141 + p, 482 + p, p, 341 + p, canvas),
    Wall(p, 341 + p, p, 141 + p, canvas),
    # Wall(p, p, p, p, canvas),
    # Wall(p, p, p, p, canvas),
    # Wall(p, p, p, p, canvas),
    # Wall(p, p, p, p, canvas),
    # Wall(p, p, p, p, canvas)
]

my_sys = System(wall_list, ball_list, k, mu, 1, canvas)

canvas.pack()
my_sys.start()
master.mainloop()
