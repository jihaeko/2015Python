##내장함수~~##

#data = [1, 2, 3, 4]
#print(dir(data))

#print(divmod(7,3))

#enumdata = list(enumerate(data))
#print(enumdata)

#print(eval('1+3'))



#def positive(l):
#    return l > 0

#def even(i):
#    return i%2 == 0

#print(list(filter(even, [1,-3,2,0,-5,6,7])))



#a = 3
#print(id(3))
#print(id(a))

#print(int(3.5))



#sum = lambda a, b : a+b
#print(sum(3,4))

#l = [lambda a,b:a+b, lambda a,b:a*b]
#print(l[0](3,4))
#print(l[1](3,4))

#print(list(filter(lambda x: x%2 == 0, [1,-3,2,0,-5,6,7])))



#a = [1,2,3,4]
#b = list(a)
#c = a       #참조라서 동일한 주소값 갖는다

#print(id(a))
#print(id(b))
#print(id(c))

#print(a)
#print(b)
#print(c)



#print(list(map(lambda a:a*2, [1,2,3,4])))



#print(eval(repr("hi".upper())))
#print(eval(str("hi".upper())))




#data = [6, 4, 7, 2, 9, 5, 8, 3, 2, 10, 44, 71, 85, 13]

##data.sort()
##print(data)

#print(sorted(data))
#print(data)



#print(list(zip([1,2,3], [10, 20, 30], [100, 200])))




data = { "홍길동":[80, 70, 60, 92], "김길동":[24, 35, 18, 10], "고길동":[10, 20, 8, 5] }

keys = list(data.keys())
for key in keys: 
    data.get(key).sort()

my_list = sorted(data.items(), key=lambda x: x[1])

print(my_list)

