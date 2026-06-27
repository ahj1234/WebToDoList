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
        else:
            return """
        <script>
            alert('Username or Password is incorrect');
            window.location.href='/';
        </script>
        """
    elif request.method == "GET":
        return render_template("LoginPage/index.html")

@app.route("/Dashboard", methods=["GET", "POST"])
def Dashboard():
    if request.method == "POST":
        subject = request.form["subject"]
        time_range = request.form["TimeRange"]
        description = request.form["description"]

        Current_List.add_new_task(time_range, subject, description)

    return render_template("Dashboard/index.html", Current_List=Current_List.show())

@app.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    Current_List.rem(int(task_id))
    return redirect("/Dashboard")

if __name__ == "__main__":
    app.run(debug=True)