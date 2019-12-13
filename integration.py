from numpy import linspace,exp,trapz
from scipy.integrate import simps,romberg,fixed_quad

x=linspace(0,1)
y=exp(x)

a=trapz(y,x)
print("trapezoidal rule:",a,".")

b=simps(y,x)
print("simpson rule:",b,".")

c=romberg(lambda x:exp(x),0,1)
print("romberg mathod:",c,".")

d=fixed_quad(lambda x:exp(x),0,1,n=5)
print("gaussian quadrature method:",d,".")
