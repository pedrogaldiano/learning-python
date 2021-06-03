from flask import Flask, render_template, request
from create_routine import create_routine

app = Flask(__name__)
@app.route("/", methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        user_routine = create_routine(request.form.get('routine'))
        if not user_routine is None:
            
            weight = request.form.get('weight')
            height = request.form.get('height')
            return render_template('workout.html', routine=user_routine,
                                   weight=weight, height=height)
        
    return render_template("index.html")


if __name__ == "__main__":  
    app.run()
    