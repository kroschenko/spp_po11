from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def is_inside_rectangle(self, rect: 'Rectangle') -> bool:
        # Проверяем, находится ли точка внутри прямоугольника, учитывая его центр
        left = rect.x - rect.width/2
        right = rect.x + rect.width/2
        top = rect.y - rect.height/2
        bottom = rect.y + rect.height/2

        return (left <= self.x <= right and
                top <= self.y <= bottom)


@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float

    def contains_point(self, point: Point) -> bool:
        return point.is_inside_rectangle(self)
