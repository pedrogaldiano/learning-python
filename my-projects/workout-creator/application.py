from flask import Flask, render_template, request
from helpers import create_basic_routine, create_personalized_routine

predefined_routine = ['Full body', 'Push', 'Pull', 'Legs']

muscles_list = ['Chest', 'Triceps', 'Lats', 'Traps', 'Neck', 'Shoulders', 
                'Middle back', 'Lower back', 'Biceps', 'Forearms',
                'Abdominals', 'Quadriceps', 'Hamstrings', 'Glutes', 
                'Calves', 'Adductors', 'Abductors', 'Aerobic']

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        
        if request.form.get('action') == 'Generate Predefined Workout':
            
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
        
        if request.form.get('action') == "Generate Personalized Workout":
            personalized = []
            
            for muscle in muscles_list:
                muscle_selected = request.form.get(muscle)
                
                if muscle_selected == 'on':
                    number_exercises = int(request.form.get('number_ex'))
                    
                    if number_exercises >= 1 and number_exercises <= 8:
                        personalized.append((muscle_selected, number_exercises))
                        
            if not personalized == []:
                routine = create_personalized_routine(personalized)
                routine_name = request.form.get('routine_name')
                
                return render_template('wokout.html', routine=routine,
                                       routine_name=routine_name)
            
        
    return render_template('index.html', muscles_list=muscles_list, 
                           predefined_routine=predefined_routine)


if __name__ == "__main__":  
    app.run()
    