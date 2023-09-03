import math


class Solution:
    def square(self, triangle: list, rectangle: list, circle: list) -> dict:
        p = sum(triangle) / 2
        triangle_square = (p * (p - triangle[0]) * (p - triangle[1]) * (p - triangle[2])) ** 0.5
        rectangle_square = rectangle[0] * rectangle[1]
        circle_square = math.pi * circle[0] ** 2
        return {
            'Площадь треугольника ': triangle_square,
            'Площадь прямоугльника ': rectangle_square,
            'Площадь круга ': circle_square
        }


if __name__ == '__main__':
    triangle = list(map(int, input('Введите параметры треугольника - ').split()))
    rectangle = list(map(int, input('Введите параметры прямоугольника - ').split()))
    circle = list(map(int, input('Введите параметры круга - ').split()))
    print(Solution().square(triangle, rectangle, circle))
