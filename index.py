import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("white")

star = turtle.Turtle()
star.speed(0)
star.pensize(8)
star.color("blue")

def rotate_3d(x, y, z, ax, ay, az):
    x1, y1, z1 = x, y * math.cos(ax) - z * math.sin(ax), y * math.sin(ax) + z * math.cos(ax)
    x2, y2, z2 = x1 * math.cos(ay) + z1 * math.sin(ay), y1, -x1 * math.sin(ay) + z1 * math.cos(ay)
    x3, y3, z3 = x2 * math.cos(az) - y2 * math.sin(az), x2 * math.sin(az) + y2 * math.cos(az), z2
    return x3, y3, z3

def calculate_8_point_star(size):
    angle = math.pi / 4
    return [(size * math.cos(i * angle), size * math.sin(i * angle), 0) for i in range(8)]

def draw_star(size):
    ax, ay, az = 0, 0, 0
    points = calculate_8_point_star(size)
    while(True):
        star.clear()
        rotated_points = [rotate_3d(x, y, z, ax, ay, az) for x, y, z in points]
        star.penup()
        star.goto(rotated_points[0][0], rotated_points[0][1])
        star.pendown()
        for i in [5, 2, 7, 4, 1, 6, 3, 0]:
            star.goto(rotated_points[i][0], rotated_points[i][1])
        ax += math.radians(10)
        ay += math.radians(8)
        az += math.radians(6)
        screen.update()
        time.sleep(0.05)

screen.tracer(0, 0)
draw_star(200)
star.hideturtle()
turtle.done()