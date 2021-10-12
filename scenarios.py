from planet import Body

def getSpawnPoints(num_bodies, spawn_radius, mass):
    points = []

    for i in range(num_bodies):
        rand_x = random.uniform(-spawn_radius,spawn_radius)
        rand_y = random.uniform(-spawn_radius,spawn_radius)
        rand_z = random.uniform(-spawn_radius,spawn_radius)

        pos = [rand_x, rand_y, rand_z]
        vel = [0,0,0]
        points.append(Body(pos, vel, mass))

    return points

def fibonacci_sphere(num_bodies, spawn_radius, mass):
    points = []
    indices = np.arange(0, num_bodies, dtype=float) + 0.5

    phi = np.arccos(1 - 2 * indices/num_bodies)
    theta = np.pi * (1 + 5**0.5) * indices

    x, y, z = np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)

    for i in range(len(x)):
        vel = [random.randrange(-1,1) / 1e8 for i in range(3)]
        zero_vel = [0,0,0]
        pos = [spawn_radius*x[i], spawn_radius*y[i], spawn_radius*z[i]]
        points.append(Body(pos, vel, mass))

    return points

def solar_system():
    data = [[1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+4, 5.9740e+24], #Earth
            [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+4, 6.4190e+23], #Mars
            [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+4, 3.3020e+23], #Mercury
            [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+0, 1.9890e+30], #Sun
            [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+4, 4.8690e+24]] #Venus

    planets = []

    for row in data:
        pos = [row[0], row[1], 0]
        vel = [row[2], row[3], 0]
        mass = row[4]
        planets.append(Body(pos, vel, mass))

    return planets