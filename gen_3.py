import math

def calculate_lateral_surface_area_cone(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    lateral_surface_area = math.pi * radius * slant_height
    return lateral_surface_area
