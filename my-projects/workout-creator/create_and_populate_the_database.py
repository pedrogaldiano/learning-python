# Create a sqlite database from the exercises.csv
# When I make a search I want to be able to group by muscle
# In order to optimize the search

# To be honest I don't think the performance gain with a relational database
# will be noticed with a database this small. But, I thought that doing it
# would be a nice learning method

import sqlite3

# Create the database
def create_db(db):
    try:                
        db.execute('''CREATE TABLE exercises(
        exercise TEXT UNIQUE NOT NULL, 
        muscle_id INTEGER, 
        FOREIGN KEY (muscle_id) REFERENCES muscles)''')
        
        db.execute(''' CREATE TABLE muscles(
        muscle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        muscle_name TEXT UNIQUE NOT NULL)''')
        
        print('Database created')
    except:
        print('Database has already been created')


# Store all the exercises in a table
def exercises_db(csv_file, db):
    with open(csv_file, 'r') as csv:
        for line in csv:
            items = line.replace('\n','').split(',')
            
            db.execute('SELECT muscle_id FROM muscles WHERE muscle_name = ?', [items[1].lstrip()])
            muscle_id = db.fetchone()
            if not muscle_id is None:
                try:
                    db.execute("INSERT INTO exercises(exercise, muscle_id) VALUES (?, ?)", (items[0], muscle_id[0]))
                except:
                    pass
    print('Exercises added')
    
    
# Store all the muscles in a table 
def muscles_db(csv_file, db):
    muscles = []
    
    with open(csv_file, 'r') as csv:
        for line in csv:
            items = line.replace('\n','').split(',')
            muscles.append(items[1])

    muscles_unique = set(muscles)
    for muscle_unique in muscles_unique:
        if muscle_unique == '' or muscle_unique == ' ': 
            continue
        db.execute("INSERT INTO muscles (muscle_name) VALUES (?)", [muscle_unique.lstrip()])
    
    print('Muscles added')


def main():
    csv_file = 'exercises.csv'
    
    connect = sqlite3.connect('exercises-data.db')
    db = connect.cursor()
    
    create_db(db)
    muscles_db(csv_file, db)
    exercises_db(csv_file, db)
    
    connect.commit()
    connect.close()


if __name__ == '__main__':
    main()