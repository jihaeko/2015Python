#fileName = "jihae.txt"
#with open(fileName, "r") as myFile:
#    #myFile.write("201311193 고지혜\n")
#    #myFile.write("201311196 김륜하\n")
#    #myFile.write("201311200 김예찬\n")

#    #while True:
#    #    content = myFile.readline()
#    #    if not content : break
#    #    print(content)

#    for line in myFile:     #기본 단위가 라인
#        print(line)


#파이썬에서 제공하는 라이브러리 피클!
#투플을 그대로 파일에! 파일을 그대로 투플에! 
#dump-파일에 저장 / load-파일에서읽어옴 (wb, rb)
import pickle

fileName = "파일입출력예제2.txt"
fileChan = "Chandler.txt"

roles = []

with open(fileName, "r") as myFile, open(fileChan, "wb") as chanFile:
    for content in myFile:
        (role, etc) = content.strip().split(":", 1)
        #if role == "Chandler" :
        #    chanFile.write(content)
        roles.append(role)
    pickle.dump(roles, chanFile)
    
with open(fileChan, "rb") as chanFile:
    result = pickle.load(chanFile)

print(roles)
print(result)

#help(str.split)


