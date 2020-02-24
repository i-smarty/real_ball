import tkinter
from math import sqrt, sin, cos, pi


def bump_ball(v, omega, phi):
    """
    Function that returns velocity v and angular velocity omega after bump by the wall with angle phi of slope.

    :param v: velocity
    :param omega: angular velocity
    :param phi: oriented angle from horizontal line to line of wall --- \measuredangle(horizontal_line, wall_line)
    :return: new velocity and new angular velocity
    """
    v_perp = v[0] * cos(-phi) - v[1] * sin(-phi)  # parallel to wall component of velocity
    v_paral = v[0] * sin(-phi) + v[1] * cos(-phi)  # perpendicular to wall component of velocity

    if v_perp <= 0:
        return v, omega

    P = v_perp * (1 + k) * mu
    v_paral_bal = (R ** 2 * v_paral + I * -omega * R) / (R ** 2 + I)
    Q = abs(v_paral - v_paral_bal)
    if P >= Q:
        v_paral = v_paral_bal
        omega = -v_paral_bal / R
    else:
        dv_paral = (v_paral_bal - v_paral) * P / Q
        v_paral += dv_paral
        omega += dv_paral * R / I
    v_perp *= -k

    v[0] = v_perp * cos(phi) - v_paral * sin(phi)
    v[1] = v_perp * sin(phi) + v_paral * cos(phi)
    return v, omega
    
    
def move_ball():
    """
    function that moves ball every 30 ms
    """
    global omega, v, v_y0, h_0
    grav = True
    canvas.move(ball, v[0], v[1])
    canvas.move(spot, v[0], v[1])
    canvas.move(spot, omega * (canvas.coords(ball)[1] + R - canvas.coords(spot)[1] - r), omega * (canvas.coords(spot)[0] + r - canvas.coords(ball)[0] - R))
    if canvas.coords(ball)[0] <= 0:
        v, omega = bump_ball(v, omega, pi)
        canvas.move(ball, -canvas.coords(ball)[0], 0)
        grav = False
    elif canvas.coords(ball)[2] >= w:
        v, omega = bump_ball(v, omega, 0)
        canvas.move(ball, w - canvas.coords(ball)[2], 0)
        grav = False
    if canvas.coords(ball)[1] <= 0:
        v, omega = bump_ball(v, omega, -pi/2)
        canvas.move(ball, 0, -canvas.coords(ball)[1])
        grav = False
    elif canvas.coords(ball)[3] >= h:
        v, omega = bump_ball(v, omega, pi/2)
        canvas.move(ball, 0, h - canvas.coords(ball)[3])
        grav = False
    
    spot_x = canvas.coords(spot)[0] + r
    spot_y = canvas.coords(spot)[1] + r
    ball_x = canvas.coords(ball)[0] + R
    ball_y = canvas.coords(ball)[1] + R
    alpha = (R - r) / sqrt((spot_x - ball_x) ** 2 + (spot_y - ball_y) ** 2)
    canvas.move(spot, -(spot_x - ball_x) * (1 - alpha), -(spot_y - ball_y) * (1 - alpha))
    
    if grav:
        v[1] += g
    
    #if not grav:
        #h_0 = canvas.coords(ball)[1] 
        #v_y0 = v[1]
    
    #h_1 = canvas.coords(ball)[1] 
    #if v[1] > 2 * g:
        #v[1] = sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    #elif v[1] < -2 * g:
        #v[1] = -sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    
    canvas.after(30, move_ball)


master = tkinter.Tk()

# variables
v = [6, -3]  # initial velocity
h = 800  # height of the canvas
w = 1200  # width of the canvas
omega = 0.7  # initial angular velocity
g = 0.5  # acceleration of gravity
mu = 1  # friction coefficient
I = 0.6  # moment of inertia of the ball
k = 0.98  # coefficient of recovery


R = 30  # radius of the ball
r = 5  # radius of spot on the ball

master.title('Ball')
master.minsize(800, 700)

canvas = tkinter.Canvas(master, bg = 'green', height = h, width = w)

ball_pos = (210, 200) # initial position of ball
ball = canvas.create_oval((ball_pos[0], ball_pos[1]), (ball_pos[0] + 2 * R, ball_pos[1] + 2 * R), fill='white')
h_0 = canvas.coords(ball)[1]
v_y0 = v[1]
spot_pos = (ball_pos[0] + R, ball_pos[1] + r)
spot = canvas.create_oval((spot_pos[0] - r, spot_pos[1] - r), (spot_pos[0] + r, spot_pos[1] + r), fill='red')

canvas.pack()
move_ball()
master.mainloop()