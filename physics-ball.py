import tkinter
from math import sqrt


def move_ball():
    """
    function that moves ball every 30 ms
    """
    global omega, v, v_y0, h_0
    grav = True
    canvas.move(ball, v[0], v[1])
    canvas.move(spot, v[0], v[1])
    canvas.move(spot, omega * (canvas.coords(ball)[1] + R - canvas.coords(spot)[1] - r),
                omega * (canvas.coords(spot)[0] + r - canvas.coords(ball)[0] - R))
    if canvas.coords(ball)[0] <= 0:
        if mu == 0:
            v[0] = - k * v[0]
        else:
            dv_y = (v[1] - omega * 10) * I / mu / (I + 1)
            if abs(dv_y) <= abs((1 + k) * v[0]):
                v[1] = v[1] - mu * dv_y
                omega += mu * dv_y / I / 10
                v[0] = - k * v[0]
            elif dv_y > 0:
                v[1] = v[1] + mu * (1 + k) * v[0]
                omega -= mu * (1 + k) * v[0] / I / 10
                v[0] = - k * v[0]
            else:
                v[1] = v[1] - mu * (1 + k) * v[0]
                omega += mu * (1 + k) * v[0] / I / 10
                v[0] = - k * v[0]
        canvas.move(ball, -canvas.coords(ball)[0], 0)
        grav = False
    elif canvas.coords(ball)[2] >= w:
        if mu == 0:
            v[0] = - k * v[0]
        else:
            dv_y = (-v[1] - omega * 10) * I / mu / (I + 1)
            if abs(dv_y) <= abs((1 + k) * v[0]):
                v[1] = v[1] + mu * dv_y
                omega += mu * dv_y / I / 10
                v[0] = - k * v[0]
            elif dv_y > 0:
                print(v, omega)
                v[1] = v[1] + mu * (1 + k) * v[0]
                omega += mu * (1 + k) * v[0] / I / 10
                v[0] = - k * v[0]
                print(v, omega)
            else:
                v[1] = v[1] - mu * (1 + k) * v[0]
                omega -= mu * (1 + k) * v[0] / I / 10
                v[0] = - k * v[0]
                print(v, omega)
        canvas.move(ball, w - canvas.coords(ball)[2], 0)
        grav = False
    if canvas.coords(ball)[1] <= 0:
        if mu == 0:
            v[1] = - k * v[1]
        else:
            dv_y = -(v[0] + omega * 10) * I / mu / (I + 1)
            if abs(dv_y) <= abs((1 + k) * v[1]):
                v[0] = v[0] + mu * dv_y
                omega += mu * dv_y / I / 10
                v[1] = - k * v[1]
            elif dv_y > 0:
                v[0] = v[0] - mu * (1 + k) * v[1]
                omega -= mu * (1 + k) * v[1] / I / 10
                v[1] = - k * v[1]
            else:
                v[0] = v[0] + mu * (1 + k) * v[1]
                omega += mu * (1 + k) * v[1] / I / 10
                v[1] = - k * v[1]
        canvas.move(ball, 0, -canvas.coords(ball)[1])
        grav = False
    elif canvas.coords(ball)[3] >= h:
        if mu == 0:
            v[1] = - k * v[1]
        else:
            dv_y = (v[0] - omega * 10) * I / mu / (I + 1)
            if abs(dv_y) <= abs((1 + k) * v[1]):
                v[0] = v[0] - mu * dv_y
                omega += mu * dv_y / I / 10
                v[1] = - k * v[1]
            elif dv_y > 0:
                v[0] = v[0] - mu * (1 + k) * v[1]
                omega += mu * (1 + k) * v[1] / I / 10
                v[1] = - k * v[1]
            else:
                v[0] = v[0] + mu * (1 + k) * v[1]
                omega -= mu * (1 + k) * v[1] / I / 10
                v[1] = - k * v[1]
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

    # if not grav:
    # h_0 = canvas.coords(ball)[1]
    # v_y0 = v[1]

    # h_1 = canvas.coords(ball)[1]
    # if v[1] > 2 * g:
    # v[1] = sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))
    # elif v[1] < -2 * g:
    # v[1] = -sqrt(v_y0 ** 2 + 2 * g * (h_1 - h_0))

    canvas.after(30, move_ball)


master = tkinter.Tk()

# variables
v = [6, 0]  # initial velocity
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

canvas = tkinter.Canvas(master, bg='green', height=h, width=w)

ball_pos = (200, 200)  # initial position of ball
ball = canvas.create_oval((ball_pos[0], ball_pos[1]), (ball_pos[0] + 2 * R, ball_pos[1] + 2 * R), fill='white')
h_0 = canvas.coords(ball)[1]
v_y0 = v[1]
spot_pos = (ball_pos[0] + R, ball_pos[1] + r)
spot = canvas.create_oval((spot_pos[0] - r, spot_pos[1] - r), (spot_pos[0] + r, spot_pos[1] + r), fill='red')

canvas.pack()
move_ball()
master.mainloop()
