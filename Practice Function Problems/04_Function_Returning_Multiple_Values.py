import math

def circle_radius(radius):
    area = math.pi * radius ** 2
    curcumference = 2 * math.pi * radius
    return area,curcumference

a , c = circle_radius(5)

print("Area", a, "Curcumference : ", c)

