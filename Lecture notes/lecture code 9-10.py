
def cel2fahren(C):
    """
    Converts Celcius to Fahrenheit
    
    Input:
        Temperature in Celsius
    Output:
        Temperature in Fahrenheit
        
    Convert the given temperature from Celsius
    to Fahrenheit
    """
    
    F = C*(9./5.) + 32.0    
    print(F)
    return F

F_100 = cel2fahren(100.0)
temp = 60.0
F_60 = cel2fahren(temp)


a = -200.0
b = 30.0

if (a > 0.0):
    comp1 = 0.234
    
    
# comparing floating point number to integer
c = 200.0 + a

tol = 1.e-12        # use tolerance values when comparing floating points
if (abs(c) < tol):   # equivalent to if (c == 0)
    comp3 = 20.0