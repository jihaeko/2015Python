# print("Here are the numbers!" + \
#    " The first is {0:d} The Second is {0:4d}".format(7,8))

print("한글")

#salary = input("please enter your salary: ")
#bonus = input("please enter your bonus: ")
#payCheck = float(salary) + float(bonus)
#print(round(payCheck,1))

#print(type(payCheck))   #타입체크

print("""야
야
야
야
야""")   #여러줄 출력

#여러줄
#주석
#처리는 ctrl+k+c
#해제는 ctrl+u

name="kojihae"
print(name[0])
print(name[-2])

info = "201311193kojihae"
sid = info[:9]
sname = info[9:]
print(sid + "\n" + sname)

a = "I eat %-10s apples." % "five"
print(a)

print("error is %d%%" %98)

print("{0:=^10}".format("hi"))  #공백 채우기

a = ","
b = a.join('abcd')
print(b)        #??

answer = input("종료할까요? ")
print(answer.lower())