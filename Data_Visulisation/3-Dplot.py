import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
ax=plt.axes(projection='3d')
z=np.linspace(0,30,100)
# x=np.linspace(0,30,100)
# y=np.linspace(0,30,100)
# z=x**2+y**2
def zfun(x,y):
    return -y**2
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=zfun(X,Y)




# x=np.sin(z)
# y=np.cos(z)
ax.plot_surface(X,Y,Z)
plt.show()