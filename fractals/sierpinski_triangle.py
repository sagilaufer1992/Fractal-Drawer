from utils.polygon_drawings import equilateral_triangle
from utils.point_calculations import generate_point_by_distance_and_angle


def sierpinski_triangle(game_display, left_base_point, side_length, main_color, secondary_color, depth):
    equilateral_triangle(game_display, main_color, left_base_point, side_length, True, False)
    sierpinski_triangle_aux(game_display, left_base_point, side_length, secondary_color, depth)
    pass


def sierpinski_triangle_aux(game_display, left_base_point, side_length, color, depth):
    if depth == 0:
        return
    flipped_left_base_point = generate_point_by_distance_and_angle(left_base_point, side_length / 2, -120)
    equilateral_triangle(game_display, color, flipped_left_base_point, side_length / 2, True, True)
