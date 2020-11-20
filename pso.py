import math


class PSO:
    def __init__(self, diversification_factor, cognitive_factor, social_factor):
        self.w = diversification_factor
        self.c1 = cognitive_factor
        self.c2 = social_factor
        self.topology = {}
        self.g_best = math.inf

    def set_topology(self, selected_topology):
        pass

    def update_velocity(self):
        pass

    @staticmethod
    def check_limits(inf_limit, sup_limit, xi):
        if xi >= sup_limit:
            return sup_limit
        elif xi <= inf_limit:
            return inf_limit
        else:
            return xi

    def f(self, selected_f, x):
        """
            10 - Beale Function (2 dimension?)
            interval = −4.5≤ xi ≤4.5
            minimum = x∗= (3,0.5), f(x∗) = 0.

            7 - Alpine 2 Function
            interval = 0≤ xi ≤ 10.
            minimum =  x∗= (7.917· · ·7.917), f(x∗) = 2.808D ~= 174.617174...
        """
        if selected_f == 10:
            for i in range(2):
                x[i] = self.check_limits(-4.5, 4.5, x[i])
            return (1.5 - x[0] + (x[0] * x[1])) ** 2 + \
                   (2.25 - x[0] + (x[0] * x[1] ** 2)) ** 2 + \
                   (2.625 - x[0] + (x[0] * x[1] ** 3)) ** 2
        elif selected_f == 7:
            fo = 1
            for xi in x:
                xi = self.check_limits(0, 10, xi)
                fo *= math.sqrt(xi) * math.sin(xi)
            return fo


class Particle:
    def __init__(self, dimension):
        self.x = [] * dimension  # coordinates
        self.velocity = [] * dimension
        self.p_best = [] * dimension  # Best known pos of particle
        self.fitness = 0
        self.best_neighbor = -1
