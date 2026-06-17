from Classes import TO_DO_List
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

Current_List = TO_DO_List.To_Do()

user = "test"
passw = "1234"

@app.route("/", methods=["GET", "POST"])
def LoginPage():

    if request.method == "POST":

        if request.form["user"] == user and request.form["passw"] == passw:
            return redirect("/Dashboard")

        else :
            return """
        <script>
            alert('Username or Password is incorrect');
            window.location.href='/';
        </script>
        """
    elif request.method == "GET":
        return render_template("LoginPage/index.html")
    else :
        pass

@app.route("/Dashboard")
def Dashboard():
    return render_template("Dashboard/index.html")

if __name__ == "__main__":
    app.run(debug=True)