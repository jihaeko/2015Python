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




#data = np.arange(36).reshape(6,6)
#print(data)

#mask = np.array(np.array([1,0,1,0,0,1], dtype=bool))
#print(data[mask,2])

#mask1 = np.array([0,1,2,3,4])
#mask2 = np.array([1,2,3,4,5])
#print(data[mask1, mask2])

#mask3 = np.array(np.array([1,0,1,0,0,1], dtype=bool))
#print(data[3:, mask3])




#li = [1, 2, 3, 4, 5, 6]
#li2 = li*2
#print(li2)

#data = np.array([[1,2,3], [4,5,6], [7,8,9]])
#i = np.eye((3))
#print(data*2)
#print(data-2)
#print(data*data)  #각 원소별로 곱셈..!
#print(data*i)
#print(data.dot(data))  #행렬의 곱셈 .
#print(data.dot(i))




#a = np.array([1,2,3,4])
#b = np.array([4,2,2,4])
#c = np.array([1,2,3,4])
#print(a == b)
#print(a > b)

#print(np.array_equal(a,b))
#print(np.array_equal(a,c))




#a = np.array([1,1,0,0], dtype=bool)
#b = np.array([1,0,1,0], dtype=bool)
#print(np.logical_or(a,b))
#print(np.logical_and(a,b))
#print(np.all([True, True, False]))
#print(np.any([True, True, False]))

#a = np.array([1,2.71,1])
#print(np.sin(a))
#print(np.log(a))
#print(np.exp(a))




#a = np.triu(np.ones((3,3)), 0)
#print(a)
#print(a.T)



#x = np.array([1,2,3,4])
#print(np.sum(x))

#x = np.array([[1,1],[2,2]])
#print(x.sum())
#print(x.sum(axis=0))   #columns
#print(x.sum(axis=1))   #rows

#print(x[1,:].sum())




#x = np.array([[1,2,3], [4,5,6], [7,8,9]])
#print(x.min())
#print(x.max())
#print(x.argmin())
#print(x.argmax())




#x = np.array([[1,2,3,1,2]])
#y = np.array([[1,2,3], [5,6,1]])
#print(x.mean())
#print(np.median(x))
#print(np.median(y))
#print(x.std())




#from matplotlib import pyplot as plt

#data = np.loadtxt('data.txt')
##print(data)

#year, hares, lynxes, carrots = data.T
##plt.plot(year, hares, year, lynxes, year, carrots)
##plt.show()


##년도별 평균
#m = np.mean(data, axis=0)
#print(m)
#print()
##년도별 표준편차
#print(hares.std())
#print(lynxes.std())
#print(carrots.std())
#print()
##가장 개체수가 많았던 년도수
#hy = hares.argmax()
#print(int(year[hy]))
#print(hares.max())

#ly = lynxes.argmax()
#print(int(year[ly]))
#print(lynxes.max())

#cy = carrots.argmax()
#print(int(year[cy]))
#print(carrots.max())


