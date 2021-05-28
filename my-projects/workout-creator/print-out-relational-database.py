import sqlite3

cnn = sqlite3.connect('exercises-relational-database.db')
c = cnn.cursor()

show_all_data = '''
SELECT
exercise_name, u.utility, m.mechanic, 
f.force, t.target, s.synergist

FROM exercises e

INNER JOIN utilities u
    ON e.utility_id = u.id
INNER JOIN mechanics m
    ON e.mechanic_id = m.id
INNER JOIN forces f
    ON e.force_id = f.id
INNER JOIN targets t 
    ON e.target_id = t.id
INNER JOIN synergists s
    ON e.synergist_id = s.id
'''

c.execute(show_all_data)
items = c.fetchall()
for item in items:
    print(item)
print(len(items))

cnn.close()