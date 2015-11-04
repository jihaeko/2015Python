import sqlite3

#연결
con = sqlite3.connect("test.db")
con.isolation_level = None

cur = con.cursor()


##테이블 생성
#dropsql = '''drop table if exists phonebook;'''
#cur.execute(dropsql)

#sql = '''create table if not exists
#phonebook(name text, phoneNum text);'''
#cur.execute(sql)


##삽입
#insertsql = '''insert into phonebook 
#values('jihae', '010-4724-0863');'''
#cur.execute(insertsql)

#name = 'minimind'
#phoneNum = '010-2345-4564'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phoneNum))

#name = 'Daemunja'
#phoneNum = '010-1234-5678'
#insertsql = '''insert into phonebook
#values(:inputName, :inputNum);'''
#cur.execute(insertsql, {"inputNum":phoneNum, "inputName":name})

##iterator 삽입
#insertsql = '''insert into phonebook values(?,?);'''
#datalist = (('pipi525', '010-4839-0293'), ('1qkqk', '010-0000-0000'))
#cur.executemany(insertsql, datalist)

##generator
#def dataGenerator():
#    datalist = (('pipi525', '010-4839-0293'), ('1qkqk', '010-0000-0000'))
#    for item in datalist:
#        yield item

#cur.executemany(insertsql, dataGenerator())

#cur.execute("insert into phonebook(phoneNum) values ('010-6500-0863');")



##사용자 지정 정렬 방식
#def OrderFunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) - (s1 < s2) #앞에가 크면 음수 같으면 0
#                                 #뒤에가 크면 양수

#con.create_collation('myordering', OrderFunc)

##select
#selectsql = '''select * from phonebook order by name collate myordering;'''
#cur.execute(selectsql)
##print(cur.fetchall())
#for row in cur:
#    print(row)



##count
#cur.execute("select count(*) from phonebook;")
#print(cur.fetchone()[0])

#cur.execute("select count(name) from phonebook;")
#print(cur.fetchone()[0])





#user table

sql = '''create table if not exists
user(name text, age int);'''
cur.execute(sql)

##iterator 삽입
#insertsql = '''insert into user values(?,?);'''
#datalist = (('jihae', 23), ('pipi', 22), ('jj', 25), ('hoo', 23))
#cur.executemany(insertsql, datalist)



class Average:
    def __init__(self):
        self.sum = 0;
        self.cnt = 0;

    def step(self, value):
        self.sum += value
        self.cnt += 1

    def finalize(self):
        return self.sum/self.cnt

con.create_aggregate("avg", 1, Average)



#select
selectsql = '''select avg(age) from user;'''
cur.execute(selectsql)
#print(cur.fetchall())
for row in cur:
    print(row[0])










