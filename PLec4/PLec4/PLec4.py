#함수

#def sum_and_mul(a,b):
#    return a+b, a*b

#data = sum_and_mul(3,4)
#print(data)
#sum, mul = sum_and_mul(3,4)
#print(sum)
#print(mul)

#def main():
#    printNames(getNames())
#    return

#def getNames():
#    names = ["jihae","minimind", "pipi"]
#    newName = input("Enter last guest : ")
#    names.append(newName)
#    return names

#def printNames(names):
#    for name in names:
#        print(name)
#    return

#main()

#def say_myself(name, old, man=True):
#    print("이름: %s" %name)
#    print("나이: %s" %old)
#    if man:
#        print("남자")
#    else:
#        print("여자")

#say_myself("고지혜", 23)

#coding:cp949 
#인코딩 모드를 cp949로 바꾸는 코드

#import printData

#movies = ["홍길동",["베테랑",["류승완", "황정민", "유아인"], "암살", ["최동훈", "이정재", "전지현"]], "고길동",["베테랑", "암살"]]
#printData.printData(movies)
#print()

import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".\\sample")
#os.system("python setup.py sdist")
os.system("python setup.py install")