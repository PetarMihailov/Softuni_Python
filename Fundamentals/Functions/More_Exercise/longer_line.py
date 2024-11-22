import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def closest_point(x1, y1, x2, y2):
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)
    if distance1 <= distance2:
        return math.floor(x1), math.floor(y1), math.floor(x2), math.floor(y2)
    else:
        return math.floor(x2), math.floor(y2), math.floor(x1), math.floor(y1)


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length1 = calculate_distance(x1, y1, x2, y2)
    length2 = calculate_distance(x3, y3, x4, y4)

    if length1 >= length2:
        x_start, y_start, x_end, y_end = closest_point(x1, y1, x2, y2)
    else:
        x_start, y_start, x_end, y_end = closest_point(x3, y3, x4, y4)

    print(f"({x_start}, {y_start})({x_end}, {y_end})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
