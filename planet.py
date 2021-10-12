import math
import numpy as np

G = 6.67 * 10**-11

class Body:
    def __init__(self, initial_pos, initial_vel, mass):
        self.pos = np.array(initial_pos)
        self.vel = np.array(initial_vel)
        self.acc = np.zeros(3)
        self.mass = mass

    def _getAcceleration(self, other_planets):
        acc = np.zeros(3)
        epsilon = 100
        for planet in other_planets:
            r = self.pos - planet.pos
            r_squared = np.dot(r.T, r)

            inc = -((G * planet.mass) / (r_squared + epsilon**2)**(3/2)) * r
            acc += inc

        return acc

    def integrateVelocity(self, other_planets, dt):
        acc = self._getAcceleration(other_planets)
        self.vel += dt * acc

    def integratePosition(self, dt):
        self.pos += dt * self.vel

    def getPosition(self):
        return self.pos