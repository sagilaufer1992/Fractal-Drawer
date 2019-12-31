import pygame
from utils.point_calculations import generate_point_by_distance_and_angle


def equilateral_triangle(game_display, color, base_left_point, side_length, should_fill, should_flip):
    base_right_point = generate_point_by_distance_and_angle(base_left_point, side_length, 0)
    head_point = generate_point_by_distance_and_angle(base_left_point, side_length, 60 if should_flip else -60)
    pygame.draw.polygon(game_display, color, (base_left_point, base_right_point, head_point),
                        1 if not should_fill else 0)
    pass


def line_by_length_and_angle(game_display, color, start_point, length, angle):
    end_point = generate_point_by_distance_and_angle(start_point, length, angle)
    pygame.draw.line(game_display, color, start_point, end_point)
