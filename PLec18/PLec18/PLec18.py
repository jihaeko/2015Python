from flask import Flask, url_for, redirect, render_template

#the name of the application package
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<title>/<name>')     #경로 지정해주는것. 홈페이지의 메인에 해당하는거 접속했을때! 
def hello_world(title = None, name=None):
    data1 = [dict(href="http://www.naver.com", caption="네이버"), dict(href="http://www.google.com", caption="구글")]
    data2 = {
        'title' : title,
        'name' : name
        }
    #return render_template('hello.html', items=data, name=name)
    return render_template('hello.html', items=data1, **data2)

@app.route('/')   
def main(title = None, name=None):
    data1 = [dict(href="http://www.naver.com", caption="네이버"), dict(href="http://www.google.com", caption="구글")]
    data2 = {
        'title' : title,
        'name' : name
        }
    return render_template('main.html', items=data1, **data2)
    

@app.route('/profile/<username>')
def get_profile(username):
    return 'Profile: '+username

@app.route('/login')
def login():
    return 'log in'

if __name__ == '__main__':
    #app.run()

    app.debug = True        #개발할 때만 이렇게
    app.run(host='203.252.166.39', port=5000)

