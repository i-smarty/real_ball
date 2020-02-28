from math import sin, cos


class Ball:
    def __init__(self, x, y, R, r, alpha, m, I, v, omega, g, mu, k, canvas):
        self._x = x
        self._y = y
        self._x_spot = x + cos(alpha) * (R - r)
        self._y_spot = y + sin(alpha) * (R - r)
        self._R = R
        self._r = r
        self._alpha = alpha
        self._m = m
        self._I = I
        self._v = v
        self._omega = omega
        self._g = g
        self._mu = mu
        self._k = k
        self._canvas = canvas
        self._canvas_ball = canvas.create_oval((self._x - R, self._y - R),
                                               (self._x + R, self._y + R), fill='white')
        self._canvas_spot = canvas.create_oval((self._x_spot - r, self._y_spot - r),
                                               (self._x_spot + r, self._y_spot + r), fill='red')

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
    def x_spot(self):
        return self._x_spot

    @x_spot.setter
    def x_spot(self, new_x_spot):
        self._x_spot = new_x_spot

    @property
    def y_spot(self):
        return self._y_spot

    @y_spot.setter
    def y_spot(self, new_y_spot):
        self._y_spot = new_y_spot

    @property
    def R(self):
        return self._R

    @property
    def r(self):
        return self._r

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, new_alpha):
        self._alpha = new_alpha

    @property
    def m(self):
        return self._m

    @property
    def I(self):
        return self._I

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, new_v):
        self._v = new_v

    @property
    def omega(self):
        return self._omega

    @omega.setter
    def omega(self, new_omega):
        self._omega = new_omega

    @property
    def g(self):
        return self._g

    @property
    def mu(self):
        return self._mu

    @property
    def k(self):
        return self._k

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x_spot += dx
        self.y_spot += dy
        self._canvas.move(self._canvas_ball, dx, dy)
        self._canvas.move(self._canvas_spot, dx, dy)
        # self._canvas.coords(self._canvas_ball,
        #                     self.x - self.R, self.y - self.R,
        #                     self.x + self.R, self.y + self.R)
        # self._canvas.coords(self._canvas_spot,
        #                     self.x_spot - self.r, self.y_spot - self.r,
        #                     self.x_spot + self.r, self.y_spot + self.r)

    def rotate(self, phi):
        self.alpha += phi
        alpha = self.alpha
        x_spot_old = self.x_spot
        y_spot_old = self.y_spot
        self.x_spot = self.x + cos(alpha) * (self.R - self.r)
        self.y_spot = self.y + sin(alpha) * (self.R - self.r)
        self._canvas.move(self._canvas_spot, self.x_spot - x_spot_old, self.y_spot - y_spot_old)
