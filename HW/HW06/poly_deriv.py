"""poly_deriv.py -- evaluating the first derivative of given polynomial at x"""
def polynomial_derivative(coef, x):
    """
    Compute the derivative of a polynomial fit at a given point based on 
    an array of polynomial coefficients as input

    Parameters
    ----------
    coef : 1D numpy array
        Coefficients of a polynomial.
    x : float
        x value to be evaluated.

    Returns
    -------
    p : float
        the evaluated derivative of polynomial with given coefficients at x

    """
    
    if (not (coef.size > 0) ):
        raise ValueError("Coefficient array must have at least one element")
        
    p = 0.0
    for i in range(1, coef.size):   # start at 1 because the derivative of the first coefficient is zero, and thusly irrelevant
        p += (coef[i]*i) * x**(i-1) # why i-1? it's the derivative
    
    return p
    