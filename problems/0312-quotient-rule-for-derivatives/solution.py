import numpy as np

def val(coeffs:list,x:float):
    n=len(coeffs)
    if(n==1):return coeffs[0]
    elif(n==2):return coeffs[0]*x+coeffs[1]
    elif(n==3):return coeffs[0]*x**2+coeffs[1]*x+coeffs[2]

def deri(coeffs:list,x:float):
    n=len(coeffs)
    if(n==1):return 0
    elif(n==2):return coeffs[0]
    elif(n==3):return 2*coeffs[0]*x+coeffs[1]


def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    dg=deri(g_coeffs,x)
    dh=deri(h_coeffs,x)
    g=val(g_coeffs,x)
    h=val(h_coeffs,x)
    df=(dg*h-dh*g)/h**2
    return df