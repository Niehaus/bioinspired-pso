"""
Particle Swarm Optimization
author: Barbara Boechat
date: 20/11/2020

"""

import matplotlib.pyplot as plt
import csv
import sys
import os
from pso import PSO

if __name__ == '__main__':
    # diversification_factor = 0.729
    # cognitive_factor = 1.49445
    # social_factor = 1.49445
    diversification_factor = float(sys.argv[1])
    cognitive_factor = float(sys.argv[5])
    social_factor = float(sys.argv[5])
    dimension = int(sys.argv[2])
    cloud_size = int(sys.argv[3])
    max_iteration = int(sys.argv[4])
    k = 0
    scatter_x = []
    scatter_y = []

    pso = PSO(dimension, diversification_factor, cognitive_factor, social_factor, [-10, 10])
    cloud_particles = pso.initialize_cloud_particles(cloud_size)
    topology = pso.set_topology(cloud_particles)

    for i, particle in enumerate(cloud_particles, start=0):
        particle.initialize_coordinates(pso.sup_limit, pso.inf_limit)
        particle.neighbors = topology[i]
        pso.best_neighbor(cloud_particles, particle)
    #     scatter_x.append(particle.x[0])
    #     scatter_y.append(particle.x[1])
    #
    # plt.plot(scatter_x, scatter_y, 'o', color='orange', label='Initial Cloud')
    # plt.legend()
    dict_iter = {}
    vector_iter = []
    while k < max_iteration:
        for i, particle in enumerate(cloud_particles, start=0):
            vector_iter.append(particle.x[:])
            if pso.f(particle.x) < pso.f(particle.p_best):
                particle.p_best = particle.x[:]
                if pso.f(particle.x) < pso.f(pso.g_best):
                    pso.g_best = particle.x[:]
            for j in range(particle.dimension):
                pij = particle.p_best[j]
                gj = pso.g_best[j]
                xij = particle.x[j]
                particle.velocity[j] = pso.calculate_velocity(pij, gj, xij)
            particle.update_velocity()
        dict_iter[k] = vector_iter
        vector_iter = []
        k += 1
    best_fitness = pso.f(pso.g_best)
    print(
        f'f6(x): {pso.inf_limit} <= xi <= {pso.sup_limit}\n'
        f'The global minimum is located at origin x* = (0,. . .,0), f(x*) = 0\n'
        f'Number of particles: {cloud_size}\n'
        f'Dimension(s): {dimension}\n'
        f'Global Best founded: {best_fitness}')

    file = 'results2.csv'
    fieldnames = ['dim', 'cloud_size', 'max_iter', 'd_fact', 'c1_c2', 'profit']
    if os.path.isfile(file):
        with open(file, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {'dim': dimension, 'cloud_size': cloud_size, 'max_iter': max_iteration,
                 'd_fact': diversification_factor, 'c1_c2': social_factor, 'profit': best_fitness})
    else:
        with open(file, 'a+', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {'dim': dimension, 'cloud_size': cloud_size, 'max_iter': max_iteration,
                 'd_fact': diversification_factor, 'c1_c2': social_factor, 'profit': best_fitness})
    # color = ['tab:purple', 'tab:green', 'tab:red', 'tab:blue', 'tab:orange']
    # # color = ['indianred','firebrick', 'brown', 'maroon', 'darkred']
    # for item in dict_iter:
    #     for coord in dict_iter[item]:
    #         # print('x:', coord[0], 'y:', coord[1])
    #         scatter_x.append(coord[0])
    #         scatter_y.append(coord[1])
    #     plt.plot(scatter_x, scatter_y, 'o', color=color[item], label=item)
    #     plt.legend()
    #     scatter_x = []
    #     scatter_y = []

    # scatter_x = []
    # scatter_y = []
    # for particle in cloud_particles:
    #     scatter_x.append(particle.x[0])
    #     scatter_y.append(particle.x[1])
    #
    # plt.plot(scatter_x, scatter_y, 'o', label='Final Cloud')
    # plt.legend()
    #
    # plt.plot(pso.g_best[0], pso.g_best[1], 'o', color='red', label='Global Best')
    # plt.legend()

    plt.savefig('scatter.png')
