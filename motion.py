from math import sin, cos, pi


def move(speed, angle):
    return sin(angle * pi / 180) * speed, -cos(angle * pi / 180) * speed
