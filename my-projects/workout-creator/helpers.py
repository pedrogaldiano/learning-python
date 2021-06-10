import sqlite3
import random

def check_input(input_routine):
        selected = input_routine
        if selected in ['Full body', 'Push', 'Pull', 'Legs', 'Abductors',
                        'Chest', 'Glutes', 'Triceps','Traps', 'Calves',
                        'Quadriceps', 'Lower back', 'Neck','Middle back',
                        'Lats', 'Shoulders', 'Adductors', 'Abdominals',
                        'Biceps', 'Forearms', 'Hamstrings']:
            return selected
        
        
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
    exercises = [] #[('Full Body Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Lower back', 'Chest', 'Chest',
                   'Hamstrings', 'Quadriceps', 'Calves', 'Shoulders', 
                   'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises
    

def push():
    exercises = [] # [('Push Day','3 sets x 8~12 reps')]
    for target in ['Middle back', 'Middle back', 'Lower back', 'Lower back', 
                   'Lats', 'Biceps', 'Biceps', 'Forearms', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def pull():
    exercises = [] # [('Pull Day','3 sets x 8~12 reps')]
    for target in ['Chest', 'Chest', 'Chest', 'Triceps', 'Triceps', 
                   'Shoulders', 'Shoulders', 'Traps', 'Abdominals']:
        exercises.append((get_exercise(target), target))   
    return exercises


def legs():
    exercises = [] #[('Legs Day','3 sets x 8~12 reps')]
    for target in ['Hamstrings', 'Hamstrings', 'Quadriceps', 'Quadriceps',
                   'Adductors', 'Abductors', 'Glutes', 'Glutes', 'Calves']:
        exercises.append((get_exercise(target), target))
    return exercises


def create_basic_routine(routine):
    exercises = []
    for i in routine:
        user = check_input(i)
        
        if user == 'Full body':
            exercises = [full()]
            
        elif user == 'Push':
            exercises.append(push())
      
        elif user == 'Pull':
            exercises.append(pull())
            
        elif user == 'Legs':
            exercises.append(legs())
      
    return exercises


def create_personalized_routine(routine):
    targets = []
    for (muscle, times) in routine:
        targets += ([muscle] * times)
    
    exercises = []
    temp = []
    for target in targets:
        i = 0
        while True:
            i += 1   
            exercise = get_exercise(target)

            if not (exercise in temp):
                break

            elif i == 8:
                exercise = 'Not found'
                break
            
        temp.append(exercise)    
        exercises.append((exercise, target))
    return [exercises]
        
        
# ls = []    
# for i in range(1000):
#     routine = create_personalized_routine([('Abductors', 8)])   
#     print(routine)
#     ls.append(routine)
# x = sorted(ls)
# print(x)
    
# for i in routine:
#     for k in i:
#         print(k)

# routine = create_basic_routine(['Push', 'Legs', 'Legs', 'Pull'])

# print(routine,'\n\n')
# for i in routine:
#     print(i, '\n\n')

# for days in routine:
#     print(days,'\n')
#     print()
#     for exercises in days:
#         print(exercises)
#     print()