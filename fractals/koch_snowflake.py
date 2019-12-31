from utils.geometric_drawings import line_by_length_and_angle
from utils.point_calculations import generate_point_by_distance_and_angle


def koch_triangle(game_display, color, start_point, length, depth):
    koch_curve(game_display, color, start_point, length, -60, depth)
    koch_curve(game_display, color, generate_point_by_distance_and_angle(start_point, length, -60), length, 60, depth)
    koch_curve(game_display, color, generate_point_by_distance_and_angle(start_point, length, 0), length, -180, depth)


def koch_curve(game_display, color, start_point, length, angle, depth):
    if depth == 0:
        line_by_length_and_angle(game_display, color, start_point, length, angle)
        return
    third_length = length / 3
    new_depth = depth - 1

    koch_curve(game_display, color, start_point, third_length, angle, new_depth)

    second_point = generate_point_by_distance_and_angle(start_point, third_length, angle)
    koch_curve(game_display, color, second_point, third_length, angle - 60, new_depth)

    third_point = generate_point_by_distance_and_angle(second_point, third_length, angle - 60)
    koch_curve(game_display, color, third_point, third_length, angle + 60, new_depth)

    fourth_point = generate_point_by_distance_and_angle(start_point, 2 * third_length, angle)
    koch_curve(game_display, color, fourth_point, third_length, angle, new_depth)
