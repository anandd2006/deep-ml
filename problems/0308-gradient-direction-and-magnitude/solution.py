import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    keys = ['magnitude', 'direction', 'descent_direction']
    d = dict.fromkeys(keys)

    g = np.array(gradient, dtype=float)

    mag = 0
    for i in range(len(g)):
        mag += g[i] ** 2

    mag = np.sqrt(mag)

    if mag == 0:
        d['magnitude'] = 0.0
        d['direction'] = np.zeros_like(g)
        d['descent_direction'] = np.zeros_like(g)
        return d

    for i in range(len(g)):
        g[i] /= mag

    d['magnitude'] = mag
    d['direction'] = g.copy()

    g = g * -1
    d['descent_direction'] = g

    return d