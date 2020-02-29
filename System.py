from recompiling import *


class System:
    def __init__(self, wall_list, ball_list):
        self.wall_list = wall_list
        self.ball_list = ball_list

    def recompute(self, dt):
        grav = True
        ball.move(ball.v[0], ball.v[1])
        ball.rotate(ball.omega)
        if ball.x <= ball.R:
            bump_ball(ball, pi)
            ball.move(-(ball.x - ball.R), 0)
            grav = False
        elif ball.x >= w - ball.R:
            bump_ball(ball, 0)
            ball.move(w - (ball.x + ball.R), 0)
            grav = False
        if ball.y <= ball.R:
            bump_ball(ball, -pi / 2)
            ball.move(0, -(ball.y - ball.R))
            grav = False
        elif ball.y >= h - ball.R:
            bump_ball(ball, pi / 2)
            ball.move(0, h - (ball.y + ball.R))
            grav = False

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

    def redraw(self):
        for ball in self.ball_list:
            ball.redraw()
        # for wall in self.wall_list:
        #     wall.redraw()