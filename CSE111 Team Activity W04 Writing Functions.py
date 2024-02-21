import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def compute_efficiency(radius, height):
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    efficiency = volume / area
    return efficiency

def main(name, radius, height):
    print(f"{name} - {compute_efficiency(radius, height):.2f}")

main("#1 Picnic", 6.83, 10.16)
main("#1 Tall", 7.78, 11.91)
main("#2", 8.73, 11.59)
main("#2.5", 10.32, 11.91)
main("#3 Cylinder", 10.79, 17.78)
main("#5", 13.02, 14.29)
main("#6Z", 5.40, 8.89)
main("#8Z short", 6.83, 7.62)
main("#10", 15.72, 17.78)
main("#211", 6.83, 12.38)
main("#300", 7.62, 11.27)
main("#303", 8.10, 11.11)