"""
Particle Swarm Optimization
author: Barbara Boechat
date: 20/11/2020

"""

from pso import PSO

if __name__ == '__main__':
    diversification_factor = 0.729
    cognitive_factor = 1.49445
    social_factor = 1.49445
    dimension = 5

    max_iteration = 100
    k = 0

    pso = PSO(dimension, diversification_factor, cognitive_factor, social_factor, [-10, 10])
    cloud_particles = pso.initialize_cloud_particles(cloud_size=100)
    topology = pso.set_topology(cloud_particles)
    for i, particle in enumerate(cloud_particles, start=0):
        particle.initialize_coordinates(pso.sup_limit, pso.inf_limit)
        particle.neighbors = topology[i]
        pso.best_neighbor(cloud_particles, particle)

    print('antes', pso.g_best, pso.f(pso.g_best))
    while k < max_iteration:
        for i, particle in enumerate(cloud_particles, start=0):
            # print('antes', particle.x)
            if pso.f(particle.x) < pso.f(particle.p_best):
                particle.p_best = particle.x[:]
                if pso.f(particle.x) < pso.f(pso.g_best):
                    pso.g_best = particle.x[:]
            for j in range(particle.dimension):
                pij = particle.p_best[j]
                gj = pso.g_best[j]
                xij = particle.x[j]
                # print(pij, gj, xij)
                particle.velocity[j] = pso.calculate_velocity(pij, gj, xij)
                # print(pso.calculate_velocity(pij, gj, xij))
            # print(particle.velocity)
            particle.update_velocity()
            # print(particle.velocity)
            # print('depois', particle.x)
            # print('\n')
        k += 1
    print(pso.g_best)
    print(pso.f(pso.g_best))

    # for particle in cloud_particles:

# print(pso.calculate_velocity(10, 5, 3))
# print(cloud_particles[0].x, pso.f(cloud_particles[0].x))
# print(pso.g_best, pso.f(pso.g_best))
