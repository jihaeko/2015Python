import numpy as np

#data = np.array([[1,2,3], [4,5,6], [7,8,9]])
#data.astype(np.float)

#print(data)

#one = np.ones((3,2))
#print(one)

#i = np.eye((3))
#print(i)

#d = np.diag(np.array([1,2,3,4]))
#print(d)

#data = np.array([[1,2,3,4]])        #[[]]의 형태로 배열이라는걸 알려

#datat = data.T
#print(datat)




#data = np.arange(10, 1, -2, dtype=np.float)[:, np.newaxis]
#print(data)

#data2 = np.arange(35).reshape(5,7)
#print(data2)

#print(np.linspace(1., 4., 6, endpoint=False))



##uniform in [0,1]
#data = np.random.rand(4)
##gaussian
#dataG = np.random.randn(4,4)

#print(data)
#print(dataG)




#from matplotlib import pyplot as plt

#data = np.loadtxt('data.txt')
#print(data)

#year, hares, lynxes, carrots = data.T
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()



#data = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
#print(data[0])
#print(data[-1])
#print(data[0:2])
#print(data[1:4:2])
#print(data[::-1])
#print(data[2][0])
#print(data[2,0])
#print(data[1:4:2, ::3])



#x = np.arange(10, 1, -1)
#print(x)
#print(x[np.array([3,3,1,8])])
#print(x[np.array([[1,1],[2,3]])])

#y = np.arange(35).reshape(5,7)
#print(y)
#print(y[np.array([0,2,4])])
#b = y>20
#print(y[b])



data = np.arange(36).reshape(6,6)
print(data)

mask = np.array(np.array([1,0,1,0,0,1], dtype=bool))
print(data[mask,2])

mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data[mask1, mask2])

mask3 = np.array(np.array([1,0,1,0,0,1], dtype=bool))
print(data[3:, mask3])





