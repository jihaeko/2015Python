import os
import sys
import pickle

#os.system("python test.py a b c")
#print(sys.path)




#class Student:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#    def show(self):
#        print(self.name, " : ", self.age)


#s1 = Student("jihae", 23)
##s1.show()

#f = open("student.txt", 'wb')
#pickle.dump(s1, f)
#f.close()

#rf = open("student.txt", 'rb')
#data = pickle.load(rf)

#print(data)
#data.show()

#rf.close()



#print(os.environ)
#os.chdir('..')
#print(os.getcwd())

#os.startfile('student.txt')

#print(list(os.walk("..")))

#현재 디렉토리에 sample이란 디렉토리 만들고 
#현재 디렉토리 안, 그 하위 디렉토리 안의 txt는 모두 이 sample디렉토리에 복사

import shutil

if os.path.exists("sample"):
    pass
else:
    os.mkdir("sample")

for (path, dir, files) in os.walk('.'):
    for filename in files:
        (name, txt) = os.path.splitext(filename)
        if txt == '.txt':
            dirname = "sample\\" + filename
            f = open(dirname, 'w+')
            shutil.copy(filename, dirname)


