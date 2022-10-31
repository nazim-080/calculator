import os
from pathlib import Path

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from math import sin, radians, cos

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# /********************************************************************
# * Project Name : zadanie2tp
# * File Name : figures_draw.py
# * Programmer : Laypanov Nazim, Volkov Dmitriy, Shuvaev Danila
# * Created : 12 / 10 / 22
# * Last Revision : 22 / 10 / 21
# ********************************************************************/

PATH_IMG = Path.cwd() / 'static' / 'img'

matplotlib.use('TkAgg')


class Draw:

    def __init__(self, projection='2d'):
        fig = plt.figure()
        if projection == '2d':
            self.ax = fig.add_subplot(111)
            self.ax.set_aspect('equal')
        elif projection == '3d':
            self.ax = fig.add_subplot(111, projection='3d')

    @staticmethod
    def square_draw(side):

        x = np.array([0, 0, 0 + side, 0 + side, 0])
        y = np.array([0, 0 + side, 0 + side, 0, 0])

        plt.plot(x, y)
        plt.savefig(PATH_IMG / 'square.png')
        plt.close()

    @staticmethod
    def rectangle_draw(length, width):

        x = np.array([0, 0, 0 + length, 0 + length, 0])
        y = np.array([0, 0 + width, 0 + width, 0, 0])

        plt.plot(x, y)
        plt.savefig(PATH_IMG / 'rectangle.png')
        plt.close()

    @staticmethod
    def triangle_draw(side_a, side_b, angle):

        x = np.array([0, side_a, side_a + cos(radians(180 - angle)) * side_b, 0])
        y = np.array([0, 0, side_b * cos(radians(90 - angle)), 0])

        plt.plot(x, y)
        plt.savefig(PATH_IMG / 'triangle.png')
        plt.close()

    @staticmethod
    def circle_draw(radius):

        theta = np.linspace(0, 2 * np.pi, 150)

        a = radius * np.cos(theta)
        b = radius * np.sin(theta)

        plt.plot(a, b)
        plt.savefig(PATH_IMG / 'circle.png')
        plt.close()

    @staticmethod
    def rhomb_draw(side, angle):

        second_angle = (360 - 2 * angle) / 2

        x = np.array([0, 0 - side * cos(radians(angle)),
                      0, 0 - side * cos(radians(second_angle)), 0])

        y = np.array([0, 0 + side * sin(radians(angle)),
                      (0 + side * sin(radians(angle)) + side * sin(radians(second_angle))),
                      0 + side * sin(radians(angle)), 0])

        plt.plot(x, y)
        plt.savefig(PATH_IMG / 'rhomb.png')
        plt.close()

    @staticmethod
    def trapezoid_draw(upper_base, lower_base, height):
        x = np.array([0, lower_base, lower_base, lower_base - upper_base, 0])
        y = np.array([0, 0, height, height, 0])

        plt.plot(x, y)
        plt.savefig(PATH_IMG / 'trapezoid.png')
        plt.close()

    def sphere_draw(self, radius):

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = radius * np.outer(np.cos(u), np.sin(v))
        y = radius * np.outer(np.sin(u), np.sin(v))
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
        self.ax.plot_surface(x, y, z, color="b")

        plt.savefig(PATH_IMG / 'sphere.png')
        plt.close()

    def cube_draw(self, side):

        v = np.array(
            [[0, 0, 0], [0, side, 0], [side, side, 0], [side, 0, 0], [0, 0, side], [0, side, side], [side, side, side],
             [side, 0, side]])
        self.ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        verts = [[v[0], v[1], v[2], v[3]], [v[0], v[1], v[5], v[4]], [v[1], v[2], v[6], v[5]], [v[2], v[3], v[7], v[6]],
                 [v[0], v[3], v[7], v[4]], [v[4], v[5], v[6], v[7]]]

        self.ax.add_collection3d(Poly3DCollection(verts,
                                                  facecolors='b', edgecolors='b', alpha=.6))
        plt.savefig(PATH_IMG / 'cube.png')
        plt.close()

    def parallelepiped_draw(self, length, width, height):
        self.ax.set_box_aspect(aspect=(length, width, height))

        v = np.array(
            [[0, 0, 0], [0, width, 0], [length, width, 0], [length, 0, 0], [0, 0, height], [0, width, height],
             [length, width, height], [length, 0, height]])
        self.ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        verts = [[v[0], v[1], v[2], v[3]], [v[0], v[1], v[5], v[4]], [v[1], v[2], v[6], v[5]], [v[2], v[3], v[7], v[6]],
                 [v[0], v[3], v[7], v[4]], [v[4], v[5], v[6], v[7]]]

        self.ax.add_collection3d(Poly3DCollection(verts,
                                                  facecolors='b', edgecolors='b', alpha=.6))
        plt.savefig(PATH_IMG / 'parallelepiped.png')
        plt.close()

    def cylinder_draw(self, radius, height):

        z = np.linspace(0, height, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = radius * np.cos(theta_grid)
        y_grid = radius * np.sin(theta_grid)

        x, y, z = x_grid, y_grid, z_grid

        self.ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
        self.ax.plot_surface(x, y, z, color="b")

        plt.savefig(PATH_IMG / 'cylinder.png')
        plt.close()

    def pyramid_draw(self, side, height):

        v = np.array(
            [[-side, -side, -side], [side, -side, -side], [side, side, -side], [-side, side, -side], [0, 0, height]])
        self.ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
                 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

        self.ax.add_collection3d(Poly3DCollection(verts,
                                                  facecolors='b', edgecolors='b', alpha=.8))

        plt.savefig(PATH_IMG / 'pyramid.png')
        plt.close()

    def cone_draw(self, radius, height):

        choose = max(radius, height)

        theta = np.linspace(0, 2 * np.pi, 50)
        r = np.linspace(0, choose, 50)
        T, R = np.meshgrid(theta, r)

        x = R * np.sin(T)
        y = R * np.cos(T)
        z = (np.sqrt(x ** 2 + y ** 2) / (radius / height))

        self.ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
        self.ax.plot_wireframe(x, y, z)
        self.ax.invert_zaxis()

        plt.savefig(PATH_IMG / 'cone.png')
        plt.close()
