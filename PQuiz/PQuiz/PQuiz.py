import re

def checkPW(input):
    p = re.compile(".{8,13}")
    if p.match(input):
        p2 = re.compile("\w+[!@#$%^&*]+")
        p3 = re.compile("[!@#$%^&*]+\w+")
        if p2.match(input) or p3.match(input):
            return True
        else:
            print("비밀번호는 알파벳, 숫자, 특수문자가 모두 포함되어야함")
            return False

    else:
        print("비밀번호는 8자리 이상 13자리 이하여야함")
        return False


result = checkPW("12345678901")
print(result)




