from warnings import warn


def move_ball_intel(ball, dt):
    ball.move(ball.v[0] * dt + ball.g[0] * dt ** 2 / 2,
              ball.v[1] * dt + ball.g[1] * dt ** 2 / 2)
    ball.v[0] += ball.g[0] * dt
    ball.v[1] += ball.g[1] * dt


def move_ball_silly(ball, dt):
    ball.move(ball.v[0] * dt,
              ball.v[1] * dt)
    ball.v[0] += ball.g[0] * dt
    ball.v[1] += ball.g[1] * dt


def will_ball_bump_line(ball, x_0, y_0, x_1, y_1, dt):
    dx, dy = x_1 - x_0, y_1 - y_0
    bx, by = ball.coords
    vx, vy = ball.v
    ax, ay = ball.g
    RL = ball.R * (dx ** 2 + dy ** 2) ** 0.5

    if (bx - x_0) * dy - (by - y_0) * dx < 0:
        x_0, y_0, x_1, y_1 = x_1, y_1, x_0, y_0
        dx = -dx
        dy = -dy

    if (bx - x_0) * dy - (by - y_0) * dx < RL:
        warn("will_ball_bump_line was called in intersection situation", RuntimeWarning)
        return True

    A = (ax * dy - ay * dx) / 2
    B = (vx * dy - vy * dx)
    C = ((bx - x_0) * dy - (by - y_0) * dx) - RL
    if A != 0:
        t = -B / (2 * A)
        if C > 0 and (A * t ** 2 + B * t + C) > 0 and (A * dt ** 2 + B * dt + C) > 0:
            return False
        else:
            return True
    else:
        if C > 0 and (A * dt ** 2 + B * dt + C) > 0:
            return False
        else:
            return True


def when_ball_bump_line(ball, x_0, y_0, x_1, y_1):
    dx, dy = x_1 - x_0, y_1 - y_0
    bx, by = ball.coords
    vx, vy = ball.v
    ax, ay = ball.g
    RL = ball.R * (dx ** 2 + dy ** 2) ** 0.5

    if (bx - x_0) * dy - (by - y_0) * dx < 0:
        x_0, y_0, x_1, y_1 = x_1, y_1, x_0, y_0
        dx = -dx
        dy = -dy

    if (bx - x_0) * dy - (by - y_0) * dx < RL:
        warn("will_ball_bump_line was called in intersection situation", RuntimeWarning)
        return 0

    A = (ax * dy - ay * dx) / 2
    B = (vx * dy - vy * dx)
    C = ((bx - x_0) * dy - (by - y_0) * dx) - RL
    if A != 0:
        D = B ** 2 - 4 * A * C
        if D < 0:
            return None
        else:
            D **= 0.5
            roots = list(filter(lambda t: 0 <= t, [(-B - D) / (2 * A), (-B + D) / (2 * A)]))
            if len(roots) == 0:
                return None
            else:
                return min(roots)
    else:
        if B != 0:
            t = -C / B
            if not 0 <= t:
                return None
            else:
                return t
        else:
            if C == 0:
                return 0
            return None


class FaKeBaLl:
    def __init__(self, x, y, R, v, g):
        self._x = x
        self._y = y
        self._R = R
        self._v = v
        self._g = g

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def coords(self):
        return [self.x, self.y]

    @property
    def R(self):
        return self._R

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, new_v):
        self._v = new_v

    @property
    def g(self):
        return self._g

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
