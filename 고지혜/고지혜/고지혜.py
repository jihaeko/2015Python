import os
import sys
import time

class MidTest:
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def question1(self):
        print("1) 학번 :" + self.num + ", 이름 : " + self.name)

    def question2(self, inputData, num):
        result = []
        sortedData = sorted(data.items(), key=lambda x: x[1])

        print("2) ", end = "")
        for steps in range(num):
            result.append(sortedData[(steps+1)*(-1)])
        print(result)

    def question3(self, inputFileName):
        fileName = "score\\"+inputFileName

        if os.path.exists(fileName):
            os.remove(fileName)

        with open(fileName, "w") as wholeFile:
            for(path, dir, files) in os.walk('.'):
                if path == '.\\score':
                    for name in files:
                        subname = "score\\"+name
                        myfile = open(subname, "r")
                        while True:
                            content = myfile.readline()
                            if not content: 
                                wholeFile.write("\n")
                                break
                            wholeFile.write(content)
                        myfile.close()

            print("3) "+inputFileName+"생성이 완료되었습니다.")

    def question4(self, inputFileName):
        fileName = "score\\"+inputFileName
        print("4) ", end = "")

        try:
            with open(fileName, "r") as myFile:
                tempsum = 0
                tempname = ""
                for content in myFile:
                    try:
                        (name, kor, eng, math) = content.strip().split(',', 3)
                    except:
                        pass
                    sum = int(kor) + int(eng) + int(math)
                    if sum > tempsum:
                        tempsum = sum
                        tempname = name
                top = (tempname, tempsum)
                print(top)
                    
                    
        except FileNotFoundError:
            error = sys.exc_info()[0:2]
            print(error)
   
    @staticmethod
    def question5():
        print("5) Current Time : ", end="")
        print(time.strftime("%Y.%m.%d. %I:%M:%S", time.localtime()))




#1)
jihae = MidTest("201311193", "고지혜")
jihae.question1()

#2)
data = {"명량":4.5, "베테랑":4.0, "암살":4.6, "마션":4.3}
jihae.question2(data, 2)

#3)
jihae.question3("question3.txt")

#4)
jihae.question4("question3.txt")

#5)
MidTest.question5()