#all imports
from itertools import count
import mysql.connector 
import json
from markupsafe import escape
from flask import Flask ,request,render_template,url_for,redirect
from flask import session
from flask.json import jsonify
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
#flask app created
app=Flask(__name__)
app.secret_key =os.urandom(24)
#database connection
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "Kh@n2911",
database = "mywebsitedb"
)
cursor = mydb.cursor(buffered=True)
#random otp password generator to verify user
otp=random.randint(0000,9999)
#email server setting
sender_email="demo22669@gmail.com"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,"nmyd piwk yurj bgeg")

#first page of website
@app.route("/")
def index():
     if 'user_id' in session:
      return redirect("/Home")
     else:
        return render_template("index.html")

#home page serving
@app.route("/Home")
def home():
    if 'user_id' in session:
      return render_template("home.html")
    else:
        return redirect("/")

#about page serving
@app.route("/About")
def about():
    if 'user_id' in session:
     return render_template("About.html")

#service page serving
@app.route("/Service")
def service():
    if 'user_id' in session:
     return render_template("service.html")

#contactus page serving
@app.route("/Contact",methods=["GET","POST"])
def contact():
    if 'user_id' in session:
        if request.method=="POST":
            name=escape(request.form["name"])
            email=escape(request.form["email"])
            message=escape(request.form["message"])
            query="insert into messagedb (name,email,message) values(%s,%s,%s)"
            val=(name,email,message)
            cursor.execute(query,val)
            mydb.commit()
            pass
        return render_template("contactUs.html")

#forget password page serving
@app.route("/Forget")
def forget():
    return render_template("forgetpassword.html")

#forget password page given email verification and redirecting to change password page
@app.route("/forgetverify",methods=["GET","POST"])
def forgetverify():
       email=request.form["email"]
       session["email"]=email
       message = MIMEMultipart('alternative')
       message['From'] = sender_email
       message['To'] = email
       message['Subject'] = 'password reset link'
       html = """\
            <html>
            <body>
                <p>Hi,<br>
                This is a password reset link if you request to change password click on below link else report to us</p>
                <p><a href="http://127.0.0.1:5000/changePass">Send Email Using Python</a></p>
                <p> Feel free to <strong>let us know</strong> What else we can add for you!</p>
            </body>
            </html>
            """
       part2 = MIMEText(html, "html")
       message.attach(part2)
       server.send_message(message)
       return "Email send succesfully"

#register page serving and otp sending to legitimate users
@app.route("/register",methods=["GET","POST"])
def register():
     if request.method =="POST":
         username=escape(request.form["username"])
         email=escape(request.form["email"])
         password=escape(request.form["password"])
         session["username"]=username
         session["email"]=email
         session["password"]=password
         server.sendmail(sender_email,email,str(otp))
         return redirect("/otp")

#otp verification if user enter correct otp he/she will get redirected to homepage
@app.route("/verify",methods=["GET","POST"])
def verify():
    userotp=escape(request.form["otp"])
    if userotp==str(otp):
         query="INSERT INTO users (username,Email,Password) values (%s,%s,%s)"
         val=(session['username'],session['email'],session['password'])
         cursor.execute(query,val)
         mydb.commit()
         return render_template("home.html")
    else:
        session.pop("username")
        session.pop("email")
        session.pop("password")
        return render_template("index.html",msg="code is incorrect please try again")

#login page serving
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
       email=request.form["emaill"]
       password=request.form["passwordl"]
     
       query="select * from users where email = %s and password = %s "
       val=(email,password,)
       cursor.execute(query,val)
       users=cursor.fetchall()
       print(users)
       if len(users) > 0:
          session['user_id']=users[0][0]
          return redirect("/Home")
       else:
          return redirect("/")

#logout endpoint
@app.route("/logout")
def logout():
    session.pop('user_id')
    return redirect("/")

#change password route
@app.route("/changePass",methods=["GET","POST"])
def changePass():
    if request.method=="GET":
         return render_template("changePass.html")
    else:
        if 'email' in session:
            password =request.form["password"]
            query="update users set password = %s where email = %s"
            val=[password,session["email"]]
            cursor.execute(query,val)
            mydb.commit()
            return redirect("/")
        else:
            return redirect("/Forget")

#otp page endpoint where user enter otp and get further verified
@app.route("/otp")
def run11():
    return render_template("otp.html")
         
       
    

