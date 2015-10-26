import re
import os
import sys
import glob
import urllib.request


#str = '''Window
#Unix
#Linux
#Solaris'''

#p = re.compile('^.+')
#print(p.findall(str))

#p = re.compile('^.+', re.M)     #멀티라인
#print(p.findall(str))

#p = re.compile('^.+', re.M)
#print(p.search(str))





#m = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Jihae Ko")
#print(m.group('first', 'last'))
#print(m.groups())
#print(m.groupdict())

#print()

#m = re.match(r"(\d+)\.?(\d+)?", "24")
#print(m.groups())
#print(m.groups(0))







##p = re.compile(".+:")
#p = re.compile(".+(?=:)")
#m = p.search("http://google.com")
#print(m.group())





#p = re.compile('.*[.](?!bat$|exe$).*$')
#os.chdir("C:\\")
#print(os.getcwd())
#for i in glob.iglob('*'):
#    if p.match(i):
#        print(i)





#p = re.compile("(?<=abc)def")
#m = p.search("abcdef")
#print(m.group())

#m = re.search('(?<=-)\w+', 'spam-egg')
#print(m.group())






#email = "jihae@navremove_thiser.com"
#m = re.search("remove_this", email)
#print(m.start())
#print(m.end())
#result = email[:m.start()] + email[m.end():]
#print(result)






#def displaymatch(match):
#    if match is None:
#        return None
#    return '<Match: %s, groups=%s>' % (match.group(), match.groups())

#valid = re.compile(r"^[a2-9tjqk]{5}$")
#print(displaymatch(valid.match("akt5q")))
#print(displaymatch(valid.match("akt5e")))
#print(displaymatch(valid.match("akt")))
#print(displaymatch(valid.match("727ak")))





#text = """Ross: McFluff: 834.345.1254: 155 Elm Street
#Ronald: Heathmore: 892.345.3428 436: Finley Avenue
#Frank: Burger: 925.541.7625 662: South Dogwood Way
#Heather: Albrecht: 548.326.4584 919: Park Place"""

#entries = re.split("\n", text)
#result = [re.split(":?", entry, 4) for entry in entries]
#print(result)






with urllib.request.urlopen('http://www.naver.com/') as f:
    #print(f.read())
    #print(f.read(100)) #300byte
    #print(f.read(1000).decode("utf-8")) #encoding
    
    txt = str(f.read())
    title_start = re.search("<title>",txt)
    title_end = re.search("</title_>",txt)
    title = txt[title_start.end():title_end.start()]
    print(title)