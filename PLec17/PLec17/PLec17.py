import sqlite3 as sqlite
from werkzeug import check_password_hash, generate_password_hash


def init_db():
    db = sqlite.connect("test.db")
    #with open('schema.sql') as f:
    #    db.cursor().executescript(f.read())
    #    db.commit()

    sql = '''
    drop table if exists user;
    '''
    db.cursor().execute(sql)

    sql = '''
    create table user(
    user_no integer primary key autoincrement,
    userid string not null,
    username string not null,
    userpw string not null
    );
    '''
    db.cursor().execute(sql)

def get_db():
    db = sqlite.connect("test.db")
    return db

def register():
    db = get_db()
    cur = db.cursor()

    print("☆☆☆☆☆회원가입☆☆☆☆☆")
    id = input("아이디:")
    name = input("이름:")
    pw = input("비밀번호:")

    pw = generate_password_hash(pw)


    sql = "select count(*) from user where userid =?"
    #sql = "select * from user where userid =?"
    cur.execute(sql, [id])

    if cur.fetchone()[0] != 0 :
        print("이미 있는 아이디 입니다.")
        return
    #if cur.fetchone() != None :
    #    print("이미 있는 아이디 입니다.")
    #    return

    else:
        sql = "insert into user(userid, username, userpw) values(?,?,?)"
        cur.execute(sql, [id, name, pw])

        db.commit()
        print("가입 완료")


    db.close()

def login():
    db = get_db()
    cur = db.cursor()

    print("☆☆☆☆☆로그인☆☆☆☆☆")
    id = input("아이디:")
    pw = input("비밀번호:")


    sql = "select * from user where userid =?"
    cur.execute(sql, [id])

    result = cur.fetchone()

    if result == None :
        print("없는 아이디 입니다.\n")
        return
    else:
        if check_password_hash(result[3],pw) :
            print("로그인 완료")
            print(result[2]+"님 환영합니다.\n")
        else:
            print("비밀번호 오류\n")


#init_db()

#register()
#register()


db = get_db()
cur = db.cursor()
selectsql = '''select * from user'''
cur.execute(selectsql)
for row in cur:
    print(row)
    
while(True):
    login()