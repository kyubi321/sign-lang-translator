from flask import *
from src.video_generator import generate_video
from src.dbconnection import *
import os


app=Flask(__name__)
app.secret_key="vjkg"
import functools

@app.route('/logincode',methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    query="select*from login where username=%s AND password=%s and type='user'"
    val=(username,password)
    res=selectone(query,val)

    if res is None:
        return jsonify({'task':'invalid'})
    else:
        id=res['lid']
        return jsonify({'task':'success','lid':id})

@app.route('/tip',methods=['POST'])
def tip():
    qry="SELECT * FROM `tips`"
    res=selectall(qry)
    return jsonify(res)

@app.route('/texttosign',methods=['POST'])
def texttosign():
    txt=request.form['txt']
    fn=generate_video(txt)
    return jsonify({"fn":fn})


@app.route('/view_material',methods=['post'])
def view_material():
    qry="SELECT * FROM `study materials`"
    RES=selectall(qry)
    print(RES)
    return jsonify(RES)

@app.route('/send_feedback',methods=['post'])
def send_feedback():
    feedback=request.form['feedback']
    uid=request.form['lid']
    qry="INSERT INTO `feedbacks` VALUES(NULL,%s,%s,CURDATE())"
    val=(uid,feedback)
    iud(qry,val)
    return jsonify({'task':'success'})

@app.route('/sign_up',methods=['post'])
def sign_up():
    fname=request.form['fname']
    lname=request.form['lname']
    gender=request.form['gender']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    phone=request.form['phone']
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,gender,place,post,pin,phone,email)
    iud(qry1,val1)

    return ({'task':'success'})











app.run(host='0.0.0.0')