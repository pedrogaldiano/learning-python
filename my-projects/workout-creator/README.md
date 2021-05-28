### Workout Creator
#### Generate a workout program by choosing "randomly" the exercises for each muscle group defined by some filters. This approach may help you to avoid injury and to have results more consistently.
-------------

##### I want to be able to define some filters like: === [NOT YET]
* Which muscles I will train each day 
* How many exercises I want to do per day
* Which exercises I don't want to do
* Push/Pull/Legs | Antagonists | Push/Pull | ABCD | ABCDE...
* So on...

## Development process:

#### First: I scrap the exrx.net (they have one of the biggest exercise database avaiable for free online (+1400 exercises))
Get all the links to the exercises pages ==== [OK]  
Get all the exercises info ==== [OK]  

#### Second: Create a efficiently SQL database (probably the SQLite is enough)
Store everything in one table ==== [OK]  
MAKE TWO BACKUPS (GIT + LOCAL) ==== [OK]
Clean up the database (took way longer than a expected) ==== [OK]
Find out which collumns could be break in a relational database === [OK]  
Create a relational database === [OK]

#### Third: Now I have to create a code that will choose thoose exercises, but HOW?
No idea.. hahahaha
I must add some filters too...
Should I create a website? Or an app?
Probably an website is the best rigth now
BUT, FIRST I MUST SETUP THE PROGRAM OFFILINE :D (I GUESS, who knows!?")
