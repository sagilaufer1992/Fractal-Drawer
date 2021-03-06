from utils.geometric_drawings import equilateral_triangle
from utils.point_calculations import generate_point_by_distance_and_angle


def sierpinski_triangle(game_display, left_base_point, side_length, main_color, secondary_color, depth):
    equilateral_triangle(game_display, main_color, left_base_point, side_length, True, False)
    sierpinski_triangle_aux(game_display, left_base_point, side_length, secondary_color, depth)
    pass


def sierpinski_triangle_aux(game_display, left_base_point, side_length, color, depth):
    if depth == 0:
        return

    half_side_length = side_length / 2

    flipped_left_base_point = generate_point_by_distance_and_angle(left_base_point, half_side_length, -60)
    equilateral_triangle(game_display, color, flipped_left_base_point, half_side_length, True, True)

    third_base_point = generate_point_by_distance_and_angle(left_base_point, half_side_length, 0)

    sierpinski_triangle_aux(game_display, left_base_point, half_side_length, color, depth - 1)
    sierpinski_triangle_aux(game_display, flipped_left_base_point, half_side_length, color, depth - 1)
    sierpinski_triangle_aux(game_display, third_base_point, half_side_length, color, depth - 1)
