
import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:

    if func_name == 'poly2d':
        x, y = point
        return (float(2*x*y + y**2), float(x**2 + 2*x*y))

    elif func_name == 'exp_sum':
        x, y = point
        return (float(np.exp(x+y)), float(np.exp(x+y)))

    elif func_name == 'product_sin':
        x, y = point
        return (float(np.sin(y)), float(x*np.cos(y)))

    elif func_name == 'poly3d':
        x, y, z = point
        return (float(2*x*y), float(x**2+z**2), float(2*y*z))

    elif func_name == 'squared_error':
        x, y = point
        return (float(2*x-2*y), float(2*y-2*x))

    else:
        raise ValueError("Unknown function name")
