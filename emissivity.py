# this function takes as input: Radius of fiber.
# it returns: the emissivity at that radius

def epsilon(R):
    D = 2*R
    if D <= 100 * (10**(-4)):
        return 0.1
    elif 100 * (10**(-4)) < D < 0.2:
        return 62.5078*((D)**3) + 0.0999
    return 0.6
