from flask import Flask, render_template, request
from create_routine import create_routine

def IMC(height, weight):
    imc = weight/(height/100)**2
    
    if imc <= 18.5:
        return 'Underweight'
    elif imc > 18.5 and imc <= 25:
        return 'Health'
    elif imc > 25 and imc <= 30:
        return 'Overweight'
    elif imc > 30 and imc <= 39.9:
        return 'Obese'
    else:
        return 'Extremely Obese'
    


app = Flask(__name__)
GOALS = ['Gain Muscle', 'Lose Fat', 'Strength']

@app.route("/", methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        # user_routine = create_routine(request.form.get('routine'))
        # goal = request.form.get('goal')
        # weight = request.form.get('weight')
        # height = request.form.get('height')
        
        user_routine = create_routine('push/pull/legs')
        goal = 'Gain Muscle'
        weight = 63
        height = 173
        
        # validate = [not (x is None or x == '') for x in [user_routine, goal, weight, height]]
        # if all(validate):
        return render_template('workout.html', routine=user_routine,
                                weight=weight, height=height, goal=goal, imc=IMC(height, weight))
        
    return render_template("index.html", goals=GOALS)


if __name__ == "__main__":  
    app.run()
    