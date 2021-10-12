#!/usr/bin/env python3
"""
N-Body Simulation using Matplotlib.
"""
import random
import math
import json

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import numpy as np

from planet import Body
from scenarios import *

def setupMatplotlib():
    # Setup Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    title = ax.set_title("N-Body Simulation")

    lim = [-3E11,3E11]
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    fig.set_facecolor('black')
    ax.set_facecolor('black') 
    ax.grid(False) 
    ax.w_xaxis.pane.fill = False
    ax.w_yaxis.pane.fill = False
    ax.w_zaxis.pane.fill = False

    return fig, ax, title

def parseConfig(cfg_path):
    with open(cfg_path, 'r') as f:
        cfg = json.load(f)

    return cfg

def update_graph(num, sim_data, graph, title):
    graph._offsets3d = (sim_data[num][0], 
                        sim_data[num][1],
                        sim_data[num][2])
    graph._edgecolor3d = range(len(sim_data[num][0]))
    title.set_text('3D Test, time={}'.format(num))

def simulate(points, tMax, dt):
    print("Starting simulation ...")
    sim_data = []
    velocities = []

    for i in range(int(tMax / dt)):
        sim_data.append(([], [], []))
        velocities.append([])

        for point in points:
            points_filtered = points[:]
            points_filtered.remove(point)

            point.integrateVelocity(points_filtered, dt)
            point.integratePosition(dt)

            sim_data[i][0].append(point.pos[0])
            sim_data[i][1].append(point.pos[1])
            sim_data[i][2].append(point.pos[2])

            velocities[i].append(point.vel[0])
    
    print(f'Simulation complete. Data size: {len(sim_data)},{len(sim_data[0])}')

    return sim_data, velocities

def main():
    cfg = parseConfig('config.json')
    fig, ax, title = setupMatplotlib()

    tMax = cfg['t_max']
    dt = cfg['dt']

    # points = getSpawnPoints(cfg['num_bodies'], cfg['spawn_radius'], cfg['body_mass'])
    # points = fibonacci_sphere(cfg['num_bodies'], cfg['spawn_radius'], cfg['body_mass'])
    points = solar_system()

    x_data, y_data, z_data = [], [], []

    for point in points:
        x_data.append(point.pos[0])
        y_data.append(point.pos[1])
        z_data.append(point.pos[2])

    graph = ax.scatter(x_data, y_data, z_data)
    sim_data, velocities = simulate(points, tMax, dt)

    ani = matplotlib.animation.FuncAnimation(fig, 
                                             update_graph, 
                                             int(tMax / dt), 
                                             fargs=(sim_data, graph, title), 
                                             interval=60, 
                                             blit=False)
    plt.show()

if __name__ == "__main__":
    main()