import pygame
from utils.point_calculations import generate_point_by_distance_and_angle


def equilateral_triangle(game_display, color, base_left_point, side_length, should_fill, should_flip):
    base_right_point = generate_point_by_distance_and_angle(base_left_point, side_length, 0)
    head_point = generate_point_by_distance_and_angle(base_left_point, side_length, 120 if should_flip else -120)
    pygame.draw.polygon(game_display, color, (base_left_point, base_right_point, head_point),
                        1 if not should_fill else 0)
    pass
