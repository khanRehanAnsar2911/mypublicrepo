# # from youtube_transcript_api import YouTubeTranscriptApi

# # YouTubeTranscriptApi.get_transcript("xRUxEqD2D5c",languages=['de', 'en'])
# # print(YouTubeTranscriptApi.list_transcripts("xRUxEqD2D5c"))
# # from flask import Flask , render_template,url_for

# # app = Flask(__name__)
# # @app.route("/")
# # def hello():
# #     return render_template("index.html")
# # @app.route("/home.html")
# # def hellorun():
# #     print(url_for('static',filename='style.css'))
# #     return render_template("home.html")
# import mysql.connector 

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Reh@n2911",
#     database = "geeksforgeeks"
# )
 
# # Printing the connection object 
# # print(mydb)

# cursor = mydb.cursor()
# # cursor.execute("CREATE DATABASE geeksforgeeks")
# #cursor.execute("CREATE TABLE gfg (name VARCHAR(255), user_name VARCHAR(255))")
# query="select * from gfg where user_name='muhammadrayaankhan2911@gmail.com'"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# # mydb.commit()
# # cursor.execute("select * from gfg")
# # for x in cursor:
# #     print(x)
# mydb.close()
# # for x in cursor:
# #   print(x)
import mysql.connector 
from markupsafe import escape
from flask import Flask ,request,render_template,url_for,redirect

app=Flask(__name__)
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Reh@n2911",
    database = "mywebsitedb"
)
cursor = mydb.cursor()
@app.route("/")
def run():
    return render_template("index.html")

@app.route("/Home")
def run1():
    return render_template("home.html")
@app.route("/About")
def run2():
    return render_template("About.html")
@app.route("/Service")
def run3():
    return render_template("service.html")
@app.route("/Contact")
def run4():
    return render_template("contactUs.html")
@app.route("/Forget")
def run5():
    return render_template("forgetpassword.html")
@app.route("/register",methods=["GET","POST"])
def run6():
     if request.method =="POST":
         username=escape(request.form["username"])
         email=escape(request.form["email"])
         password=escape(request.form["password"])
        #  print(password,username,email)
         query="INSERT INTO REGISTER (username,Email,Password) values (%s,%s,%s)"
         val=(username,email,password)
         cursor.execute(query,val)
         mydb.commit()
         return "data succesfully inserted"
     else:
        return ""
@app.route("/login",methods=["GET","POST"])
def run7():
    if request.method == "GET":
        return "go further"
    else:
        return "stop"
     
          



    



