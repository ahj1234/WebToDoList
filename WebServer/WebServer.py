from WebServer import app
from flask import send_from_directory
from Classes import TO_DO_List

Current_List = TO_DO_List.To_Do()

@app.route("/")
def LoginPage ():
    return send_from_directory('LoginPage' , 'index.html')

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("LoginPage", filename) 

@app.route("/dashboard/")
def Dashboard ():
    return send_from_directory("Dashboard" , 'index.html')

@app.route("/dashboard/<path:filename>")

def dash_files(filename):
    return send_from_directory("Dashboard", filename) 

if __name__ == "__main__":
    app.run()