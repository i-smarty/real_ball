import tkinter
from math import sqrt, sin, cos, pi
from Wall import Wall
from Ball import Ball


def bump_ball(ball, phi):
    """
    Function that returns velocity v and angular velocity omega after bump by the wall with angle phi of slope.

    :param v: velocity
    :param omega: angular velocity
    :param phi: oriented angle from vector (1; 0) to vector from center to bump point --- \measuredangle(horizontal_line, wall_line)
    :return: new velocity and new angular velocity
    """
    R = ball.R
    m = ball.m
    I = ball.I
    v = ball.v
    omega = ball.omega
    mu = ball.mu
    k = ball.k

    v_perp = v[0] * cos(-phi) - v[1] * sin(-phi)  # perpendicular to wall component of velocity
    v_paral = v[0] * sin(-phi) + v[1] * cos(-phi)  # parallel to wall component of velocity

    if v_perp <= 0:
        return

    L_got = v_perp * m * (1 + k) * mu
    v_paral_bal = (m * R ** 2 * v_paral + I * -omega * R) / (m * R ** 2 + I)
    L_needed = abs(v_paral - v_paral_bal) * m
    if L_got >= L_needed:
        v_paral = v_paral_bal
        omega = -v_paral_bal / R
    else:
        dv_paral = (v_paral_bal - v_paral) * L_got / L_needed
        v_paral += dv_paral
        omega += dv_paral * m * R / I
    v_perp *= -k

    v[0] = v_perp * cos(phi) - v_paral * sin(phi)
    v[1] = v_perp * sin(phi) + v_paral * cos(phi)
    ball.v = v
    ball.omega = omega
    
    
def redraw_ball():
    """
    function that moves ball every 30 ms
    """
    grav = True
    ball.move(ball.v[0], ball.v[1])
    ball.rotate(ball.omega)
    # canvas.move(ball._canvas_spot,
    #             ball.omega * (ball.y_spot - canvas.coords(ball._canvas_spot)[1] - ball.r),
    #             ball.omega * (canvas.coords(ball._canvas_spot)[0] + ball.r - ball.x_spot))
    if ball.x <= ball.R:
        bump_ball(ball, pi)
        ball.move(-(ball.x - ball.R), 0)
        grav = False
    elif ball.x >= w - ball.R:
        bump_ball(ball, 0)
        ball.move(w - (ball.x + ball.R), 0)
        grav = False
    if ball.y <= ball.R:
        bump_ball(ball, -pi/2)
        ball.move(0, -(ball.y - ball.R))
        grav = False
    elif ball.y >= h - ball.R:
        bump_ball(ball, pi/2)
        ball.move(0, h - (ball.y + ball.R))
        grav = False
    
    # spot_x = ball.x_spot
    # spot_y = ball.y_spot
    # ball_x = ball.x
    # ball_y = ball.y
    # alpha = (ball.R - ball.r) / sqrt((spot_x - ball_x) ** 2 + (spot_y - ball_y) ** 2)
    # canvas.move(ball._canvas_spot, -(spot_x - ball_x) * (1 - alpha), -(spot_y - ball_y) * (1 - alpha))
    
    if grav:
        ball.v[1] += ball.g
    
    # if not grav:
    #     h_0 = canvas.coords(ball)[1]
    #     v_y0 = v[1]
    
    # h_1 = canvas.coords(ball)[1]
    # if v[1] > 2 * g:
    #     v[1] = sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    # elif v[1] < -2 * g:
    #     v[1] = -sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    
    canvas.after(30, redraw_ball)


master = tkinter.Tk()

h = 800  # height of the canvas
w = 1200  # width of the canvas

master.title('Ball')
master.minsize(800, 700)

canvas = tkinter.Canvas(master, bg='green', height=h, width=w)

ball_pos = (200, 200)  # initial position of ball
ball = Ball(x=200,
            y=200,
            R=30,  # radius of the ball
            r=5,  # radius of spot on the ball
            alpha=0,
            m=1,  # mass of the ball
            I=0.4 * 1 * 30 ** 2,  # moment of inertia of the ball
            v=[0, 0],  # initial velocity
            omega=-0.7,  # initial angular velocity
            g=1,  # acceleration of gravity
            mu=1,  # friction coefficient
            k=0.95,  # coefficient of recovery
            canvas=canvas)
# ball = canvas.create_oval((ball_pos[0], ball_pos[1]), (ball_pos[0] + 2 * R, ball_pos[1] + 2 * R), fill='white')
# spot_pos = (ball_pos[0] + R, ball_pos[1] + r)
# spot = canvas.create_oval((spot_pos[0] - r, spot_pos[1] - r), (spot_pos[0] + r, spot_pos[1] + r), fill='red')

canvas.pack()
redraw_ball()
master.mainloop()
