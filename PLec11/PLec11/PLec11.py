import glob
import os

#os.chdir('c:\\')
#print(glob.glob('*.txt'))



#ndir = nfile = 0

#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#        if depth == 0:
#            prefix = '|--'
#        else:
#            prefix = '|' + ' '*depth + '|--'
#        if os.path.isdir(obj):
#            ndir += 1
#            print(prefix + os.path.basename(obj))
#            traverse(obj, depth+1)
#        elif os.path.isfile(obj):
#            nfile += 1
#            print(prefix + os.path.basename(obj))
#        else:
#            print(prefix + 'unknown object:', obj)

#if __name__ == '__main__':
#    traverse('C:\\Users\\im-21\\Documents\\2015Python', 0)
#    print('\n',ndir,'directories,',nfile, 'files')



#import tempfile

#with tempfile.TemporaryFile('w+', delete=True) as fp:
#    fp.write("Hello!")
#    fp.seek(0)
#    data = fp.read()
#    print(data)
#    print(fp.name)

#if os.path.exists(fp.name):
#    print("존재")
#else:
#    print("안존재")




#import time

#print(time.ctime(time.time()))
#print(time.strftime("%B %dth %A %I:%M", time.localtime()))
#print(time.strftime("%Y-%m-%d %I:%M", time.localtime()))
#print()

#time1 = time.ctime(1234567)
#t = time.strptime(time1)
#print(time1)
#print(t)




#import calendar

#print(calendar.calendar(1993))
#print(calendar.weekday(1993, 3, 12))
#print(calendar.monthrange(2015, 10))



#import random
##data = ['고', '지', '혜']
##random.shuffle(data)
##print(data)
##print(random.choice(data))

#ten = random.sample(range(100), 10)
#random.shuffle(ten)
#print(random.choice(ten))

#data = [('Red', 3), ('Blue', 1), ('Green', 4), ('Yellow', 2)]
##datalist = []
##for val, cnt in data:
##    for i in range(cnt):
##        datalist.append(val)
#datalist = [val for val, cnt in data for i in range(cnt)]

#print(datalist)

#random.shuffle(datalist)
#print(random.choice(datalist))




import webbrowser
url = 'http://google.com'
webbrowser.open_new_tab(url)