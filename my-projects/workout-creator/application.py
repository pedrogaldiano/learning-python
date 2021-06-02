from flask import Flask, render_template, request
from create_routine import create_routine

app = Flask(__name__)
@app.route("/", methods = ['POST','GET'])



def index():
    if request.method == 'POST':
        return render_template('workout.html', test=create_routine())
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
    
    