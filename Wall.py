class Wall:
    def __init__(self, x_0, y_0, x_1, y_1, canvas, infinite=False):
        self._x_0 = x_0
        self._y_0 = y_0
        self._x_1 = x_1
        self._y_1 = y_1
        self._infinite = infinite
        self._canvas = canvas
        self._canvas_line = canvas.create_line(x_0, y_0, x_1, y_1, fill="#00FFFF")

    @property
    def x_0(self):
        return self._x_0

    @property
    def y_0(self):
        return self._y_0

    @property
    def x_1(self):
        return self._x_1

    @property
    def y_1(self):
        return self._y_1

    @property
    def infinite(self):
        return self._infinite
