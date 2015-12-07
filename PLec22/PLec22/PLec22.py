import numpy as np
import math
from matplotlib import pyplot as plt

#plt.plot([1,2,9,15])
#plt.plot([1,2,3,4], [1,4,9,16])

#plt.plot([1,2,3,4], [1,4,9,16], 'r:3')

#t = np.arange(0., 5., 0.2)
#plt.plot(t,t,'r--', t,t**2,'bs', t,t**3,'g^')

#t = np.arange(0., 3., 0.1)
#plt.plot(t, np.cos(t), color="violet", linewidth=2.5, linestyle="-", label="cosine")
#plt.plot(t, np.sin(t), color="blue", linewidth=2.5, linestyle="-", label="sine")
#plt.legend(loc='upper left')



##Create a figure of size 8x6 inches, 80 dots per inch
#plt.figure(figsize=(10,6), dpi=80)
## Create a new subplot from a grid of 1x1 (row, col, viewpos)
#plt.subplot(1,1,1)

#X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
#C, S = np.cos(X), np.sin(X)
#plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
#plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

#plt.xlim(-4.0, 4.0)
#plt.xticks(np.linspace(-4, 4, 9, endpoint=True))




#def f(t):
#    return np.exp(-t)*np.cos(2*np.pi*t)

#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)

#plt.figure(2)
#plt.subplot(211)
#plt.plot(t1, f(t1), 'bo', t2, f(t2),'k')

#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')



#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))




#n = 1024
#X = np.random.normal(0, 1, n)
#Y = np.random.normal(0, 1, n)
#T = np.arctan2(Y,X)

#plt.axes([0.025, 0.025, 0.95, 0.95])
#plt.scatter(X,Y,s=75,c=T,alpha=.5)

#plt.xlim(-1.5, 1.5)
#plt.xticks(())
#plt.ylim(-1.5, 1.5)
#plt.yticks(())



def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2 -y**2)

#n = 256
#x = np.linspace(-3,3,n)
#y = np.linspace(-3,3,n)
#X,Y = np.meshgrid(x,y)

#plt.axes([0.025, 0.025, 0.95, 0.95])

#plt.contourf(X,Y,f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
#C = plt.contour(X,Y,f(X,Y), 8, colors='black', linewidth=.5)
#plt.clabel(C,inline=1, fontsize=10)

n = 10
x = np.linspace(-3,3, 3.5*n)
y = np.linspace(-3,3, 3.0*n)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z,interpolation='nearest', cmap='spring', origin='upper')
plt.colorbar(shrink=.92)



plt.xticks(())
plt.yticks(())

plt.show()




