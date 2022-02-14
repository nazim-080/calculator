import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from math import sin, radians, cos

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

matplotlib.use('TkAgg')


def square_draw(side):
    x = np.array([0, 0, 0 + side, 0 + side, 0])
    y = np.array([0, 0 + side, 0 + side, 0, 0])

    plt.plot(x, y)
    plt.savefig('static/img/square.png')
    plt.close()


def rectangle_draw(length, width):
    x = np.array([0, 0, 0 + length, 0 + length, 0])
    y = np.array([0, 0 + width, 0 + width, 0, 0])

    plt.plot(x, y)
    plt.savefig('static/img/rectangle.png')
    plt.close()


def triangle_draw(side_a, side_b, angle):
    x = np.array([0, side_a, side_a + cos(radians(180 - angle)) * side_b, 0])
    y = np.array([0, 0, side_b * cos(radians(90 - angle)), 0])

    plt.plot(x, y)
    plt.savefig('static/img/triangle.png')
    plt.close()


def rhomb_draw(side, angle):
    second_angle = (360 - 2 * angle) / 2

    x = np.array([0, 0 - side * cos(radians(angle)),
                  0, 0 - side * cos(radians(second_angle)), 0])

    y = np.array([0, 0 + side * sin(radians(angle)),
                  (0 + side * sin(radians(angle)) + side * sin(radians(second_angle))),
                  0 + side * sin(radians(angle)), 0])

    plt.plot(x, y)
    plt.savefig('static/img/rhomb.png')
    plt.close()


def trapezoid_draw(upper_base, lower_base, height):
    x = np.array([0, lower_base, lower_base, lower_base - upper_base, 0])
    y = np.array([0, 0, height, height, 0])

    plt.plot(x, y)
    plt.savefig('static/img/trapezoid.png')
    plt.close()


def sphere_draw(radius):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color="b")

    plt.savefig('static/img/sphere.png')
    plt.close()


def cube_draw(side):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    v = np.array(
        [[0, 0, 0], [0, side, 0], [side, side, 0], [side, 0, 0], [0, 0, side], [0, side, side], [side, side, side],
         [side, 0, side]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    verts = [[v[0], v[1], v[2], v[3]], [v[0], v[1], v[5], v[4]], [v[1], v[2], v[6], v[5]], [v[2], v[3], v[7], v[6]],
             [v[0], v[3], v[7], v[4]], [v[4], v[5], v[6], v[7]]]

    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors='b', edgecolors='b', alpha=.6))
    plt.savefig('static/img/cube.png')
    plt.close()


def parallelepiped_draw(length, width, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    v = np.array(
        [[0, 0, 0], [0, width, 0], [length, width, 0], [length, 0, 0], [0, 0, height], [0, width, height],
         [length, width, height], [length, 0, height]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    verts = [[v[0], v[1], v[2], v[3]], [v[0], v[1], v[5], v[4]], [v[1], v[2], v[6], v[5]], [v[2], v[3], v[7], v[6]],
             [v[0], v[3], v[7], v[4]], [v[4], v[5], v[6], v[7]]]

    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors='b', edgecolors='b', alpha=.6))
    plt.savefig('static/img/parallelepiped.png')
    plt.close()


def cylinder_draw(radius, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    z = np.linspace(0, height, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)

    x, y, z = x_grid, y_grid, z_grid
    ax.plot_surface(x, y, z, color="b")

    plt.savefig('static/img/cylinder.png')
    plt.close()


def pyramid_draw(side, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    v = np.array(
        [[-side, -side, -side], [side, -side, -side], [side, side, -side], [-side, side, -side], [0, 0, height]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
             [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors='b', edgecolors='b', alpha=.8))

    plt.savefig('static/img/pyramid.png')
    plt.close()


def cone_draw(radius, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    choose = max(radius, height)

    theta = np.linspace(0, 2 * np.pi, 50)
    r = np.linspace(0, choose, 50)
    T, R = np.meshgrid(theta, r)

    X = R * np.sin(T)
    Y = R * np.cos(T)
    Z = (np.sqrt(X ** 2 + Y ** 2) / (radius / height))

    ax.plot_wireframe(X, Y, Z)
    ax.invert_zaxis()

    plt.savefig('static/img/cone.png')
    plt.close()


parallelepiped_draw(2.5, 6.5, 8.6)
