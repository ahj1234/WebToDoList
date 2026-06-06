from WebServer import app
from flask import send_from_directory

@app.route("/")

def LoginPage ():
    return send_from_directory('LoginPage' , 'index.html')


app.run()