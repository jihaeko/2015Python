def printData(data, cnt=0):
    for item in data:
        if isinstance(item, list):
            printData(item, cnt+1) #���!!!!!
        else:
            print("\t"*cnt, end="")
            print(item)

#isinstance�� ��µ� list�ȿ� list�� ����̳� ��������� �𸥴ٸ�??? ���������������������