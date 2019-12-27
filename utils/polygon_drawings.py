import pygame
from utils.point_calculations import generate_point_by_distance_and_angle


def equilateral_triangle(game_display, color, bottom_left_point, side_length, should_fill):
    right_point = generate_point_by_distance_and_angle(bottom_left_point, side_length, 0)
    top_point = generate_point_by_distance_and_angle(bottom_left_point, side_length, -120)
    pygame.draw.polygon(game_display, color, (bottom_left_point, right_point, top_point), 1 if not should_fill else 0)
    pass
