from flask import Flask, render_template, request, redirect,jsonify
import string    
import random

#from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    return 'hello you'


@app.route('/home', methods=['GET','POST'])
def render_page():
    return render_template('index.html')


@app.route('/save', methods=['GET','POST'])
def save_fun():
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    print("The randomly generated string is : " + str(ran)) # print the random data  
    f=open('abcd.txt','w+')
    f.write(ran)
    f.close()
    return "done"
    
if __name__ == '__main__':     
    app.run(debug=True, host='0.0.0.0',port=9000)