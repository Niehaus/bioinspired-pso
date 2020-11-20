"""
Particle Swarm Optimization
author: Barbara Boechat
date: 20/11/2020

"""

from pso import PSO

if __name__ == '__main__':
    diversification_factor = 0
    cognitive_factor = 0
    social_factor = 0

    pso = PSO(diversification_factor, cognitive_factor, social_factor)
    print(pso.f(7, [7.917, 7.917, 7.917, 7.917, 7.917]))


