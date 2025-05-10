from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


class HFractal:
    def __init__(self, start_point: Point, size: float, depth: int):
        self.start_point = start_point
        self.size = size
        self.depth = depth
        self.lines = []
        self._generate_fractal(start_point, size, depth)

    def _generate_fractal(self, center: Point, size: float, depth: int):
        if depth == 0:
            return

        half_size = size / 2
        quarter_size = size / 4

        self.lines.append((
            Point(center.x - half_size, center.y),
            Point(center.x + half_size, center.y)
        ))

        self.lines.append((
            Point(center.x - half_size, center.y - quarter_size),
            Point(center.x - half_size, center.y + quarter_size)
        ))
        self.lines.append((
            Point(center.x + half_size, center.y - quarter_size),
            Point(center.x + half_size, center.y + quarter_size)
        ))

        new_size = size / 2
        new_depth = depth - 1

        self._generate_fractal(
            Point(center.x - half_size, center.y - quarter_size),
            new_size,
            new_depth
        )

        self._generate_fractal(
            Point(center.x + half_size, center.y - quarter_size),
            new_size,
            new_depth
        )

        self._generate_fractal(
            Point(center.x - half_size, center.y + quarter_size),
            new_size,
            new_depth
        )

        self._generate_fractal(
            Point(center.x + half_size, center.y + quarter_size),
            new_size,
            new_depth
        )
