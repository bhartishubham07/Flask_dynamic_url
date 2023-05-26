from flask import Flask

FAI = Flask(__name__)

@FAI.route('/Hi')
def Hi():
    return '<center><h1>HI...Good Evening!!!!!!</h1></center'

@FAI.route('/Hello')
def Hello():
    return '<center><h1>Hello...How Are You!!!</h1></center>'

@FAI.route('/Hai')
def Hai():
    return '<center><h1>This is first flask project</h1></center'


@FAI.route('/hey/<name>')
def hey(name):
    return f'<center><h1>Hello...I am {name}</h1></center>'

if __name__ == '__main__':
    FAI.run(debug=True, host='192.168.137.1',port=5007)