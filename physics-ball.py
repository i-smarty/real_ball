import tkinter
from math import pi
from Wall import Wall
from Ball import Ball
from System import System
    
    
def redraw_ball(ball):
    """
    function that moves ball every 30 ms
    """
    grav = True
    ball.move(ball.v[0], ball.v[1])
    ball.rotate(ball.omega)
    if ball.x <= ball.R + 100:
        ball.bump_angle(pi, k, mu)
        ball.move(-(ball.x - ball.R - 100), 0)
        grav = False
    elif ball.x >= 1100 - ball.R:
        ball.bump_angle(0, k, mu)
        ball.move(1100 - (ball.x + ball.R), 0)
        grav = False
    if ball.y <= ball.R + 100:
        ball.bump_angle(-pi/2, k, mu)
        ball.move(0, -(ball.y - ball.R - 100))
        grav = False
    elif ball.y >= 700 - ball.R:
        ball.bump_angle(pi/2, k, mu)
        ball.move(0, 700 - (ball.y + ball.R))
        grav = False
    
    if grav:
        ball.v[0] += ball.g[0]
        ball.v[1] += ball.g[1]
    
    # if not grav:
    #     h_0 = canvas.coords(ball)[1]
    #     v_y0 = v[1]
    
    # h_1 = canvas.coords(ball)[1]
    # if v[1] > 2 * g:
    #     v[1] = sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    # elif v[1] < -2 * g:
    #     v[1] = -sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))

    ball.redraw()
    
    canvas.after(30, redraw_ball, ball)


master = tkinter.Tk()

h = 800  # height of the canvas
w = 1200  # width of the canvas

master.title('Ball')
master.minsize(800, 700)

canvas = tkinter.Canvas(master, bg='green', height=h, width=w)

mu = 1  # friction coefficient
k = 0.7  # coefficient of recovery

alone_ball = Ball(
            x=200,  # initial position of ball
            y=200,
            R=30,  # radius of the ball
            r=5,  # radius of spot on the ball
            alpha=0,
            m=1,  # mass of the ball
            I=0.4 * 1 * 30 ** 2,  # moment of inertia of the ball
            v=[0, 0],  # initial velocity
            omega=-0.2,  # initial angular velocity
            g=(0, 1),  # acceleration of gravity
            canvas=canvas)

just_the_same_ball = Ball(
            x=200,  # initial position of ball
            y=200,
            R=30,  # radius of the ball
            r=5,  # radius of spot on the ball
            alpha=0,
            m=1,  # mass of the ball
            I=0.4 * 1 * 30 ** 2,  # moment of inertia of the ball
            v=[0, 0],  # initial velocity
            omega=-0.2,  # initial angular velocity
            g=(0, 1),  # acceleration of gravity
            canvas=canvas)

canvas.itemconfig(alone_ball._canvas_ball, fill='yellow')

wall_list = [
    Wall(100, 100, w - 100, 100, canvas),
    Wall(100, 100, 100, h - 100, canvas),
    Wall(100, h - 100, w - 100, h - 100, canvas),
    Wall(w - 100, 100, w - 100, h - 100, canvas),
    Wall(w / 2, h - 100, 100, h / 2, canvas)
]

my_sys = System(wall_list, [alone_ball], k, mu, 1, canvas)

canvas.pack()
redraw_ball(just_the_same_ball)
my_sys.start()
master.mainloop()
