from flask import Flask, render_template, request
from helpers import create_basic_routine, create_personalized_routine

predefined_routine = ['Full body', 'Push', 'Pull', 'Legs']
app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        
        if request.form.get('action') == 'Generate Predefined Workout':
            sets = request.form.get('sets')
            reps = request.form.get('reps')
            
            routine_selected = []
            for selected in predefined_routine:
                if request.form.get(selected) == 'on':
                    routine_selected.append(selected)
                
                user_routine = create_basic_routine(routine_selected)
                routine = zip(routine_selected, user_routine)
                
                sets = request.form.get('sets')
                reps = request.form.get('reps')

            if not (user_routine == [] or sets is None or reps is None):
                return render_template('workout.html', routine=routine, 
                                       sets=sets, reps=reps)
            else:
                pass
        
        
    return render_template("index.html")


if __name__ == "__main__":  
    app.run()
    