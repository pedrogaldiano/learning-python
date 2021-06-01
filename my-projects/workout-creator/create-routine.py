import sqlite3
import random


def user_split():
    while True:
        split = input('''Choose your routine: full \
body, push/pull, push/pull/legs\n''')

        if split in ['full body', 'push/pull', 'push/pull/legs']:
            break
            
    return split
        
def get_exercise(force):
    connect = sqlite3.connect('exercises-data.db')
    db = connect.cursor()
    
    db.execute('''SELECT exercise FROM exercises
               INNER JOIN muscles USING (muscle_id)
               WHERE muscle_name = ?''', [force])    
    
    
    exercises = db.fetchall()
    exercise = random.choice(exercises)[0]
    
    db.close()
    return exercise


def full():
    exercises =['\nFULL BODY\n=======================']
    for target in ['middle back', 'lower back', 'chest', 'chest', 'hamstrings', \
              'quadriceps', 'calves', 'shoulders', 'abdominals']:
        exercises.append(get_exercise(target))   
    return exercises
    

def push():
    exercises =['\nPUSH\n=======================']
    for target in ['middle back', 'lower back', 'middle back', 'lower back', 'biceps', \
              'biceps', 'forearms', 'traps', 'abdominals']:
        exercises.append(get_exercise(target))   
    return exercises


def pull():
    exercises =['\nPULL\n=======================']
    for target in ['chest', 'chest', 'chest', 'lats', 'triceps', \
              'triceps', 'shoulders', 'shoulders', 'abdominals']:
        exercises.append(get_exercise(target))   
    return exercises


def legs():
    exercises =['\nLEGS\n=======================']
    for target in ['hamstrings', 'hamstrings', 'quadriceps', 'quadriceps', 'adductors', \
              'abductors', 'glutes', 'glutes', 'calves']:
        exercises.append(get_exercise(target))   
    return exercises


def main():
    split = user_split()
    print(split, '|| 3 x 8~12\n=======================')

    # add images of the muscles you will train each day with this program
    if split == 'full body':
        exercises = full()
        for exercise in exercises:
            print(exercise)
        

    elif split == 'push/pull':
        exercises = push() + pull()
        for exercise in exercises:
           print(exercise)
       
    elif split == 'push/pull/legs':
        exercises = push() + pull() + legs()
        for exercise in exercises:
           print(exercise)
        
        
    
    
if __name__ == '__main__':
    main()