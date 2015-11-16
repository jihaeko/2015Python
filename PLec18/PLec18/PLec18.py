from flask import Flask, url_for, redirect

#the name of the application package
app = Flask(__name__)

@app.route('/hello')     #경로 지정해주는것. 홈페이지의 메인에 해당하는거 접속했을때! 
def hello_world():
    return redirect(url_for('login'))
   

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

