import numpy as np
from scipy.interpolate import splev,splrep,InterpolatedUnivariateSpline,lagrange
import matplotlib.pyplot as pl

x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]

x_new=np.linspace(0,5,40)

a=InterpolatedUnivariateSpline(x,y)
b=splrep(x,y,k=2)
c=splrep(x,y,k=3)
d=lagrange(x,y)

y_new_1=a(x_new)
y_new_2=splev(x_new,b)
y_new_3=splev(x_new,c)
y_new_4=d(x_new)

print("lagrange polynomial is",d,".")

pl.plot(x,y,"k*",x_new,y_new_1,"c-",x_new,y_new_2,"m--",x_new,y_new_3,"g--",x_new,y_new_4,"b--")
pl.legend(['given data','linear spline','quadratic spline','cubic spline','lagrange interpolation'])
pl.show()
