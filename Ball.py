from math import sin, cos
from warnings import warn


class Ball:
    def __init__(self, x, y, R, r, alpha, m, I, v, omega, g, canvas, ball_canvas_args={}, spot_canvas_args={}):
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
        self._canvas = canvas
        BCA = {"fill": "white"}
        BCA.update(ball_canvas_args)
        SPA = {"fill": "red"}
        SPA.update(spot_canvas_args)
        self._canvas_ball = canvas.create_oval((self._x - R, self._y - R),
                                               (self._x + R, self._y + R), **BCA)
        self._canvas_spot = canvas.create_oval((self._x_spot - r, self._y_spot - r),
                                               (self._x_spot + r, self._y_spot + r), SPA)

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

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x_spot += dx
        self.y_spot += dy

    def rotate(self, phi):
        self.alpha += phi
        alpha = self.alpha
        self.x_spot = self.x + cos(alpha) * (self.R - self.r)
        self.y_spot = self.y + sin(alpha) * (self.R - self.r)

    def redraw(self):
        self._canvas.coords(self._canvas_ball,
                            self.x - self.R, self.y - self.R,
                            self.x + self.R, self.y + self.R)
        self._canvas.coords(self._canvas_spot,
                            self.x_spot - self.r, self.y_spot - self.r,
                            self.x_spot + self.r, self.y_spot + self.r)

    def bump(self, cos_phi, sin_phi, k, mu):
        """
        Function that recomputes velocity $v$ and angular velocity $\\omega$ after bump by the wall in the direction
        $e^{i \\phi}$ from center.

        :param phi: an oriented angle of direction of bump
        :param k: coefficient of recovery
        :param mu: friction coefficient
        :return: None
        """

        R = self.R
        m = self.m
        I = self.I
        v = self.v
        omega = self.omega

        v_perp = v[0] * cos_phi + v[1] * sin_phi  # perpendicular to wall component of velocity
        v_paral = -v[0] * sin_phi + v[1] * cos_phi  # parallel to wall component of velocity

        if v_perp <= 0:
            warn("Ball.bump was called in not bumping situation", RuntimeWarning)
            return

        p_got = v_perp * m * (1 + k) * mu
        v_paral_bal = (m * R ** 2 * v_paral + I * -omega * R) / (m * R ** 2 + I)
        p_needed = abs(v_paral - v_paral_bal) * m
        if p_got >= p_needed:
            v_paral = v_paral_bal
            omega = -v_paral_bal / R
        else:
            dv_paral = (v_paral_bal - v_paral) * p_got / p_needed
            v_paral += dv_paral
            omega += dv_paral * m * R / I
        v_perp *= -k

        v[0] = v_perp * cos_phi - v_paral * sin_phi
        v[1] = v_perp * sin_phi + v_paral * cos_phi
        self.v = v
        self.omega = omega

    def bump_angle(self, phi, k, mu):
        self.bump(cos(phi), sin(phi), k, mu)