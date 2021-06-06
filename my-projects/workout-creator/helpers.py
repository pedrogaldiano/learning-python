import sqlite3
import random

def IMC(height, weight):
    imc =int(weight)/(int(height)/100)**2
    
    if imc <= 18.5:
        return 'Underweight'
    elif imc > 18.5 and imc <= 25:
        return 'Healthy'
    elif imc > 25 and imc <= 30:
        return 'Overweight'
    elif imc > 30 and imc <= 39.9:
        return 'Obese'
    else:
        return 'Extremely Obese'

def user_input(input_routine):
        split = input_routine
        if split in ['full body', 'push/pull', 'push/pull/legs']:
            return split
        
        
        
def get_exercise(force):
    connect = sqlite3.connect('database/exercises-data.db')
    db = connect.cursor()
    
    db.execute('''SELECT exercise muscle_name FROM exercises
               INNER JOIN muscles USING (muscle_id)
               WHERE muscle_name = ?''', [force])    
    
    
    exercises = db.fetchall()
    exercise = random.choice(exercises)[0]
    
    db.close()
    return exercise


def full():
    exercises =[('Full Body Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Lower back', 'Chest', 'Chest', 'Hamstrings',
              'Quadriceps', 'Calves', 'Shoulders', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises
    

def push():
    exercises = [('Push Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Middle back', 'Lower back', 'Lower back', 
                   'Lats', 'Biceps', 'Biceps', 'Forearms', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def pull():
    exercises = [('Pull Day','3 sets x 8~12 reps')]
    for target in ['Chest', 'Chest', 'Chest', 'Triceps', 'Triceps', 
                   'Shoulders', 'Shoulders', 'Traps', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def legs():
    exercises = [('Legs Day','3 sets x 8~12 reps')]
    for target in ['Hamstrings', 'Hamstrings', 'Quadriceps', 'Quadriceps',
                   'Adductors', 'Abductors', 'Glutes', 'Glutes', 'Calves']:
        exercises.append((get_exercise(target), target))
    return exercises


def create_routine(routine):
    user_routine = user_input(routine)

    # add images of the muscles you will train each day with this program
    if user_routine == 'full body':
        exercises = [full()]
        return exercises
        
    elif user_routine == 'push/pull':
        exercises = [push()]+ [pull()]
        return exercises
  
    elif user_routine == 'push/pull/legs':
        exercises = [push()] + [pull()] + [legs()]
        return exercises
    
    else:
        return None

# routine = (create_routine('push/pull/legs'))
# print(routine)

# for days in routine:
#     print(days,'\n')
#     print()
#     for exercises in days:
#         print(exercises)
#     print()