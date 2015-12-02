import numpy as np
from matplotlib import pyplot as plt

#data = np.array([0, 10, 20, 30, 40, 50]).T
#print(data.shape)

#data = np.array([[0, 10, 20, 30, 40, 50]]).T
#data = data + [0, 1, 2, 3, 4, 5]

#print(data)




#mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
#print(mileposts[:, np.newaxis])
#distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
#print(distance_array)




#x,y = np.arange(5), np.arange(5)[:,np.newaxis]
#print(x,y)
#distance = np.sqrt(x**2 + y**2)
#print(distance)

##plt.pcolor(distance)
##plt.colorbar()
##plt.show()




#x,y = np.ogrid[0:5, 0:5]
#print(x)
#print(y)

#print(x+y)

#x,y = np.mgrid[0:5, 0:5]
#print(x)
#print(y)





#a = np.array([[1,2,3], [4,5,6]])
#print(a)
#print(a.ravel())
#print(a.T)
#print(a.T.ravel())

#b = a.ravel()
#b = b.reshape((3,-1))
#print(b)



#z = np.array([1,2,3])
#print(z)
#print(z[:, np.newaxis])
#print(z[np.newaxis, :])

#a = np.arange(4)
#a.resize((8,))
#print(a)





#a = np.array([[4,3,5], [1,2,1]])
#a.sort(axis=0)
#b = np.sort(a, axis=1)

#print(a)
#print(b)

#a = np.array([4,3,1,2])
#j = np.argsort(a)
#j_max = np.argmax(a)
#j_min = np.argmin(a)

#print(j)
#print(a[j_max])
#print(a[j_min])




#p = np.poly1d([3,2,-1])
#print(p(1))
#print(p.roots)
#print(p.order)

#p = np.polynomial.Polynomial([-1,2,3])

#print(p)
#print(p(1))




#x = np.linspace(0, 1, 20)
#y = np.cos(x) + 0.3*np.random.rand(20)
#p = np.poly1d(np.polyfit(x,y,3))
#t = np.linspace(0, 1, 200)

#plt.plot(x,y,'o',t,p(t),'-')
#plt.show()




#x = np.linspace(-1, 1, 2000)
#y = np.cos(x) + 0.3*np.random.rand(2000)
#p = np.polynomial.Chebyshev.fit(x,y,90)
#t = np.linspace(-1, 1, 200)

#plt.plot(x,y,'r.')
#plt.plot(t, p(t), 'k-', lw=3)
#plt.show()




#img = plt.imread('test.png')
#cutImg = img[200:500, :600]
#print(cutImg.shape, cutImg.dtype)
#plt.imshow(cutImg)
#plt.show()