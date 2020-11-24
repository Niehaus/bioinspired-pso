import math
import random

import matplotlib.pyplot as plt
import networkx as nx


class PSO:
    def __init__(self, dimension, diversification_factor, cognitive_factor, social_factor, limits):
        self.w = diversification_factor
        self.c1 = cognitive_factor
        self.c2 = social_factor
        self.topology = {}
        self.dimension = dimension
        self.inf_limit = limits[0]
        self.sup_limit = limits[1]
        self.g_best = [self.sup_limit] * dimension

    def initialize_cloud_particles(self, cloud_size):
        cloud_of_particles = []
        for _ in range(cloud_size):
            cloud_of_particles.append(Particle(self.dimension))
            cloud_of_particles[-1].initialize_coordinates(self.inf_limit, self.sup_limit)
        return cloud_of_particles

    def set_topology(self, cloud_particles):
        for i in range(len(cloud_particles)):
            if i - 1 == -1:
                vizinhos = [len(cloud_particles) - 1, i + 1]
            elif i + 1 >= len(cloud_particles):
                vizinhos = [i - 1, 0]
            else:
                vizinhos = [i - 1, i + 1]
            self.topology[i] = vizinhos
        # plot_topology(self.topology, len(cloud_particles))
        return self.topology

    def best_neighbor(self, cloud_particles, particle):
        best_fo = math.inf
        best_neighbor_x = []

        for neighbor in particle.neighbors:
            if self.f(cloud_particles[neighbor].x) < best_fo:
                best_fo = self.f(cloud_particles[neighbor].x)
                best_neighbor_x = cloud_particles[neighbor].x
        particle.p_best = best_neighbor_x

    def calculate_velocity(self, pij, gj, xij):
        vij = 1
        r1 = random.random()
        r2 = random.random()

        vij += self.w * vij
        vij += self.c1 * r1 * (pij - xij)
        vij += self.c2 * r2 * (gj - xij)

        vij = self.check_limits(vij)

        return vij

    def check_limits(self, xi):
        if xi >= self.sup_limit:
            return self.sup_limit
        elif xi <= self.inf_limit:
            return self.inf_limit
        else:
            return xi

    def f(self, x):
        """
        7 - Alpine 2 Function
        interval = 0≤ xi ≤ 10.
        minimum =  x∗= (7.917· · ·7.917), f(x∗) = 2.808D ~= 174.617174...
        """
        fo = 0
        for xi in x:
            xi = self.check_limits(xi)
            fo += abs(xi * math.sin(xi) + 0.1 * xi)
        return fo


class Particle:
    def __init__(self, dimension):
        self.dimension = dimension
        self.x = [0] * dimension  # coordinates
        self.velocity = [0] * dimension
        self.p_best = [-math.inf] * dimension  # Best known pos of particle
        self.fitness = 0
        self.neighbors = []

    def initialize_coordinates(self, inf_limit, sup_limit):
        for i in range(self.dimension):
            self.x[i] = random.uniform(inf_limit, sup_limit)

    def update_velocity(self):
        for i in range(self.dimension):
            self.x[i] = self.x[i] + self.velocity[i]


def plot_topology(topology, count_nodes):
    graph_edges = []
    for i in range(count_nodes):
        for edge in topology[i]:
            if tuple([edge, i]) not in graph_edges:
                graph_edges.append(tuple([i, edge]))

    topology_graph = nx.Graph()
    topology_graph.add_edges_from(graph_edges)

    options = {
        'with_labels': True,
        'font_weight': 'bold',
        'width': 3
    }
    # print(list(topology_graph.edges))
    nx.draw_spectral(topology_graph, **options)
    plt.savefig('topology.png')
    print("Topology Fig Save in: topology.png")


def plot_scatter(x, y, label, color):
    scatter_plot = plt.plot(x, y, 'o', color=color, label=label)

    return scatter_plot
