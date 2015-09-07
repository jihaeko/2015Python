data = ['a', 'b', 'c', ['abcd', 'efg']]
print(data[0])
print(data[-1])
print(data[3][1])

b = [1,2,3]
c = ['life', 'is', 'too', 'short']
print(b+c)
print(b*3)

f = b+c

guests = ['a', 'b', 'c', 'd']
#guests[0] = 'jihae'
#guests[1] = ['jihae1', 'jihae2']
guests[1:2] = ['jihae1', 'jihae2']
print(guests)

guests[1:2] = []
print(guests.index('c'))

#id관리~ insert해보쟝

id = ['jihae', 'minimind', 'choael']
#id.insert(1, '1234')
#id.insert(3, '5678')
#id.insert(5, '1357')

#print(id)

#id.insert(id.index('jihae')+2, ['고지혜', '01047240863'])
#id.insert(id.index('minimind')+2, ['지혜고', '0234420863'])
#id.insert(id.index('choael')+2, ['고쟤', '01000000000'])

#print(id)


#1
nEntries = len(id)
for steps in range(nEntries):
    print(id[steps])

#2
for i in id:
    print(i)
   
#1, #2가 똑같이 출력된다아~ in옆에는 리스트니까

#range란...? 0, 1, 2, 3

for step in range(4):
    print(step)

scores = [85, 62, 63, 45, 98, 23, 75, 55, 91]
#scores.sort()
#print(scores)
#scores.reverse()
#print(scores)

#이것은 상위 다섯개를 뽑는것~~
scores.sort()
scores.reverse()
hot5 = scores[0:5]
print(hot5)

for steps in data:
    if isinstance(steps, list) :    #이거 타입이 list냐???
        for step in steps:          #이중포문 (다차원에 사용한다)
            print(step)             #들여쓰기 주의
    else : 
        print(steps)


#scores.extend([50, 60])        #[10 ,20, 50, 60]
scores.append([50, 60])         #[10, 20, [50, 60]]
print(scores)


#tuple
t2 = (1,)
print(t2)