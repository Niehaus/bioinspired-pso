"""
Particle Swarm Optimization
author: Barbara Boechat
date: 20/11/2020

"""

import matplotlib.pyplot as plt

from pso import PSO

if __name__ == '__main__':
    diversification_factor = 0.729
    cognitive_factor = 1.49445
    social_factor = 1.49445
    dimension = 2
    cloud_size = 100
    max_iteration = 5
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
    print(
        f'f6(x): {pso.inf_limit} <= xi <= {pso.sup_limit}\n'
        f'The global minimum is located at origin x* = (0,. . .,0), f(x*) = 0\n'
        f'Number of particles: {cloud_size}\n'
        f'Dimension(s): {dimension}\n'
        f'Global Best founded: {pso.f(pso.g_best)}')

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
