from flask import *
from src.dbconnection import *
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key="vjkg"

import functools


def login_required(func):
	@functools.wraps(func)
	def secure_function():
		if "lid" not in session:
			return render_template('login_index.html')
		return func()
	return secure_function




@app.route('/logout')
@login_required
def logout():
	session.clear()
	return redirect('/')

@app.route('/')
def first():
    return render_template("login_index.html")


@app.route('/admin_home')
@login_required
def admin_home():
    return render_template("admin_index.html")




@app.route('/view_users')
@login_required
def view_users():
    qry="SELECT * FROM `user`"
    res=selectall(qry)
    return render_template("view users.html",val=res)




@app.route('/manage_tips')
@login_required
def manage_tips():
    qry = "SELECT * FROM `tips`"
    res = selectall(qry)
    return render_template("manageTips.html",val=res)

@app.route('/delete_tips')
@login_required
def delete_tips():
    id = request.args.get('id')
    qry="DELETE FROM tips WHERE id=%s"
    iud(qry,id)
    return ''' <script>alert("tip deleted");window.location="/manage_tips"</script>'''

@app.route('/add_tips',methods=['post'])
@login_required
def add_tips():

    return render_template("add tips.html")

@app.route('/insert_tips',methods=['post'])
@login_required
def insert_tips():
    tip=request.form['textfield']
    qry="INSERT INTO tips VALUES(NULL,%s,CURDATE())"
    value=(tip)
    iud(qry,value)
    return ''' <script>alert("tip inserted");window.location="/manage_tips"</script>'''



@app.route('/manage_study_materials')
@login_required
def manage_study_material():
    qry = "SELECT * FROM `study materials`"
    res = selectall(qry)
    return render_template("manage studymaterials.html",val=res)


@app.route('/delete_study_materials')
@login_required
def delete_study_materials():
    qry="DELETE FROM `study materials` WHERE id=%s"
    id = request.args.get('id')
    iud(qry,id)
    return ''' <script>alert("study material deleted");window.location="/manage_study_materials"</script>"'''

@app.route('/insert_study_material',methods=['post'])
@login_required
def insert_study_material():
    head=request.form['textfield']
    file=request.files['file']
    fname = secure_filename(file.filename)
    file.save(os.path.join('static/uploads',fname))
    qry="INSERT INTO `study materials` VALUES(NULL,%s,%s)"
    val=(head,fname)
    iud(qry,val)
    return ''' <script>alert("study material added");window.location="/manage_study_materials"</script>"'''



@app.route('/add_study_material',methods=['post','get'])
@login_required
def add_study_material():

    return render_template("add studymaterial.html")


@app.route('/view_user_feedbacks')
@login_required
def view_user_feedbacks():
    qry = "SELECT feedbacks.*,user.firstname,lastname FROM feedbacks JOIN USER ON feedbacks.user_id=user.login_id"
    res = selectall(qry)
    return render_template("view userfeedbacks.html",val=res)


@app.route('/logincode',methods=['post'])
def logincode():
    username=request.form['uname']
    password=request.form['pwrd']
    query="select*from login where username=%s AND password=%s"
    val=(username,password)
    S=selectone(query,val)
    if S is None:
        return '''<script>alert("invalid username or password");window.location='/'</script>'''
    else:
        session['lid']=S['lid']
        return redirect('/admin_home')





app.run(debug=True,port=1234)



