# this function takes as input: Radius of fiber.
# it returns: the emissivity at that radius

def epsilon(R):
    D = 2*R
    e = []
    for d in D:
        if d <= 100 * (10**(-4)):
            e.append(0.1)
        elif 100 * (10**(-4)) < d < 0.2:
            e.append(62.5078*((d)**3) + 0.0999)
        e.append(0.6)
    return e
