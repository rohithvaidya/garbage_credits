from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import make_response
from flask.ext.httpauth import HTTPBasicAuth
import pickle,json

from flask import Flask, session, redirect, url_for, escape, request

class user:
    def __init__(self):
        self.u = ""
        self.p = ""
        self.tasks=[]
        self.credits=0


ob=user()

app = Flask(__name__)
auth = HTTPBasicAuth()


try:
    f=open("credits.txt","r")
    credits=int(f.read())
    f.close()
    with open("users.txt", "rb") as f:
        l=pickle.load(f)
    print "No of users --- >",len(l)
    print "Current credit cost /kg---- >",credits
    f.close()

except:
    print "No users"
    l=[]
    credits = 0


@app.route('/login', methods=['GET'])
@auth.login_required
def login():
    return "Login success"


#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



#Admin methods
@app.route('/sort_by_loc/<string:task_id>', methods=['GET'])
def get_task(task_id):
    d={}
    task = [task for task in ob.tasks if task['loc_id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/get_credit', methods=['GET'])
def c():
    f=open("credits.txt","r")
    a=f.read()
    return "Credit cost /kg ---- > "+a



@app.route('/set_credit/<string:cr>')
def set(cr):
    f=open("credits.txt","w")
    f.write(cr)
    f.close()
    return "Set\n"



@app.route('/remove')
def rem():
    f=open("credits.txt","w")
    f.close()
    return "Removed\n"





#Adding the entry
@app.route('/add', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json:
        abort(400)
    task = {
        'user_name':request.json['user_name'],
        'v_id': request.json['v_id'],
        'weight': request.json['weight'],
        'loc_id': request.json['loc_id']
    }
    ob.tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/show', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': ob.tasks})


@auth.get_password
def get_password(username):
    with open("users.txt", "rb") as f:
        l=pickle.load(f)
    print "No of users --- >",len(l)
    f.close()
    for i in l:
        if i.u == username:
            ob = i
            return i.p
    return None



#Registration
@app.route('/register/<string:uname>/<string:pas>')
def register(uname,pas):
    i = user()
    i.u = uname
    i.p = pas
    l.append(i)
    with open("users.txt", "wb") as f:
        pickle.dump(l,f)
    f.close()
    return "Registered successfully\n"




@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run(debug=True)
