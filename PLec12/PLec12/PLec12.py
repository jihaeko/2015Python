import re

#p = re.compile('ab*')
#result = p.match('abbbb')
#print(result)



#pattern = re.compile("d")
#result = pattern.search("dog")
#print(result)
#result2 = pattern.search("dog", 1)
#print(result2)

#result3 = re.search(r"\\", "C:\\test")
#print(result3)


#pattern = re.compile("o")
#result = pattern.match("dog")
#print(result)
#result2 = pattern.match("dog", 1)
#print(result2)


#str = """sample1.
#sample2.
#sample3."""

#pattern = re.compile(".*$", re.S)
#result = pattern.search(str)
#print(result.group())


#str=" abc1234 xyz "
#pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*")
#result = pattern.search(str)
#print(result.group(1))
#print(result.group(2))


#pattern = re.compile("o[gh]")
#result = pattern.fullmatch("dog")
#print(result)
#result = pattern.fullmatch("ogre")
#print(result)
#result = pattern.fullmatch("doggie", 1, 3)
#print(result)



#pattern = re.compile("\W+")
#result = pattern.split('words, words, words.', 2)
#print(result)

#pattern = re.compile("c*")
#result = pattern.split('axbc')
#print(result)

#result = re.sub(r'\W', '', 'a:b:c, d.')
#print(result)



#str= '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)
#print(result.group(1))


##주민등록번호
str = "930312-2035000"
pattern = re.compile("^(\d{6})-(\d{7})$")
result = pattern.fullmatch(str)

if result:
    print(result.group(1))
    print(result.group(2))
