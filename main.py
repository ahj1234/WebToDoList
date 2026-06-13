# from flask import send_from_directory
from Classes import TO_DO_List
from flask import Flask
from flask import render_template


app = Flask(__name__)

Current_List = TO_DO_List.To_Do()

@app.route("/")
def LoginPage ():
    return render_template("LoginPage/index.html")

@app.route("/Dashboard")
def Dashboard ():
    return render_template("/Dashboard/index.html")


def main(debug=True):
    return app.run()
    

if __name__ == "__main__" :
    try :
        main()
    except Exception as _ :
        print (f"an error has been occured : {_}")
    