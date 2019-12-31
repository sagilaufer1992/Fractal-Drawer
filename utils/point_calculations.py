from math import sin, cos, pi


def generate_point_by_distance_and_angle(base, radius, theta):
    x = base[0]
    y = base[1]
    radians = 2 * pi * theta / 360
    delta_x = radius * cos(radians)
    delta_y = radius * sin(radians)
    return x + delta_x, y + delta_y
