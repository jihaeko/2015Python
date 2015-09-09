#a = {'name':'jihae', 'phone':'01047240863', 'birth':'0312'}
#b = list(a.keys())
#print(b)

#b = a.items()
#print(b)

#name = a.get('name')
#print(name)

#print('gender' in a)

#score  = {"홍길동":{"베테랑":5.0, "암살":4.5}, "고지혜":{"베테랑":4.0, "암살":5.0}}
#gildong = score.get("고지혜")
#print(gildong)
##am = score.get("고지혜").get("암살")
#am = score["고지혜"]["암살"]
#print(am)

#answer = input("would you like express shipping?")
#answer = answer.lower()
#if answer == "yes" :
#    print("that will be extra dollar")
#else :
#    print("ok bye...")

#a = [(1,2), (3,4), (5,6)]
#for (first, last) in a:     #이렇게 쌍으로 받아올 수 있다! 리스트 안에 투플 쌍으로 있으니까
#    print(first + last)

##구구단
#for i in range(1,10):
#    for j in range(2, 10):
#        print("%d X %d = %2d  " %(j, i, i*j), end = "")
#    print('')

#그리기

import turtle

#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)

#nsides = 5
#for steps in range(nsides):
#    turtle.forward(100)
#    turtle.right(360/nsides)
#    for moresteps in range(nsides):
#        turtle.forward(50)
#        turtle.right(360/nsides)

#for steps in ['red', 'blue', 'green', 'black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)

prompt = """1. Add
2. Del
3. List
4. Quit
Enter number: """

number = 0

while number != 4:
    print(prompt, end = "")
    number = int(input())
