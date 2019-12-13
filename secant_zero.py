from scipy.optimize import newton
from numpy import sin,cos,exp

def f(x):
    return sin(cos(exp(x)))

def der(x):
    return -exp(x)*sin(exp(x))*cos(cos(exp(x)))

p=newton(f,-0.1)
print("zero of sin(cos(exp(x))) for initial guess -0.1 is",p,".")                                                                                                                                                                                                                                                                      
