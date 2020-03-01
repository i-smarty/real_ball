from recompiling import *
from math import pi


class System:
    def __init__(self, wall_list, ball_list, k, mu, dt, canvas):
        self.wall_list = wall_list
        self.ball_list = ball_list
        self.k = k
        self.mu = mu
        self.dt = dt
        self.canvas = canvas

    def recompute(self, dt):
        for ball in self.ball_list:
            # grav = True
            # ball.move(ball.v[0], ball.v[1])
            # ball.rotate(ball.omega)
            # if ball.x <= ball.R + 100:
            #     ball.bump_angle(pi, self.k, self.mu)
            #     ball.move(-(ball.x - ball.R - 100), 0)
            #     grav = False
            # elif ball.x >= 1100 - ball.R:
            #     ball.bump_angle(0, self.k, self.mu)
            #     ball.move(1100 - (ball.x + ball.R), 0)
            #     grav = False
            # if ball.y <= ball.R + 100:
            #     ball.bump_angle(-pi/2, self.k, self.mu)
            #     ball.move(0, -(ball.y - ball.R - 100))
            #     grav = False
            # elif ball.y >= 700 - ball.R:
            #     ball.bump_angle(pi/2, self.k, self.mu)
            #     ball.move(0, 700 - (ball.y + ball.R))
            #     grav = False
            #
            # if grav:
            #     ball.v[0] += ball.g[0]
            #     ball.v[1] += ball.g[1]

            bump = False

            # print(ball.coords, ball.v, ball.g, ball.omega)

            for wall in self.wall_list:
                if will_ball_bump_line(ball, wall.x_0, wall.y_0, wall.x_1, wall.y_1, dt):
                    direct = how_ball_bump_line(ball, wall.x_0, wall.y_0, wall.x_1, wall.y_1)
                    # print(wall.x_0, wall.y_0, wall.x_1, wall.y_1, dt, direct)
                    ball.move(ball.v[0], ball.v[1])
                    ball.rotate(ball.omega)
                    ball.bump(*direct, self.k, self.mu)
                    overstep = max((ball.x - wall.x_0) * direct[0] + (ball.y - wall.y_0) * direct[1] + ball.R, 0)
                    ball.move(-overstep * direct[0], -overstep * direct[1])
                    bump = True
                    break

            # print()

            if not bump:
                ball.move(ball.v[0], ball.v[1])
                ball.rotate(ball.omega)
                ball.v[0] += ball.g[0] * dt
                ball.v[1] += ball.g[1] * dt

    def redraw(self):
        for ball in self.ball_list:
            ball.redraw()
        # for wall in self.wall_list:
        #     wall.redraw()

    def step(self):
        self.recompute(self.dt)
        self.redraw()

    def start(self):
        self.step()
        self.canvas.after(30, self.start)
