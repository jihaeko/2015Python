import sqlite3
from flask import Flask, request, session, g, url_for, redirect, \
    render_template, abort, flash

from contextlib import closing

#configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key'  #세션사용, 세션의 안전성 보장
USERNAME = 'admin'
PASSWORD = 'admin'

#the name of the application package
app = Flask(__name__)
app.config.from_object(__name__)    #app.config는 플라스크 설정과 관련된 딕셔너리 객체
                                    #from_object함수는 대문자로 설정된 값들을 config에 추가

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#def init_db():
#    db = connect_db()
#    with open('schema.sql') as f:
#        db.cursor().executescript(f.read())
#    db.commit()

def init_db():
    with closing(connect_db()) as db:  #디비를 알아서 닫아준당.
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db() #g:flask의 전역 클래스 인스턴스

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    #cursor객체를 생성한 후에 질의를 수행함. 걍 db.execute해도!
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title = row[0], text=row[1]) for row in cur.fetchall()]
    #print(entries)
    return render_template('show_entries.html', entries=entries)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)  #HTTPException
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    #app.run()
    init_db()

    app.debug = True        #개발할 때만 이렇게
    app.run(host='203.252.166.39', port=5000)
