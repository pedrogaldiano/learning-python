### Workout Creator
#### Generate a workout program by choosing "randomly" the exercises for each muscle group defined by some filters. This approach may help you to avoid injury and to have results more consistently.

------------------------
## IMPORTANT:
I just figured out that the Terms of Use of exrx.net don't allow scrapping or any form of copying its content.  
Because of this, I'm removing the database I have created with its data and the scrapping application I created.
*Sorry, I didn't know it was prohibited.*  
I will get data from an [open source project in git hub from davejt](https://github.com/davejt/exercise). I choose to not use the API since the most crucial part of the data I can get from a CSV file.  
The first and second steps were throw away completely, but I won delete them because they were part of my development process. :)  
------------------------

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

#### Third: Get the data from an open source and delete some things
Get the [exercise database](https://github.com/davejt/exercise) in CSV ==== [OK]  
Delete the database created with the exrx.net data ==== [OK]
Delete the python file with the scrapping application ==== [OK]
I decided to delete everything, most of the files were dependents on the scrapping or database.  
I didn't make sense to keep them.  

#### Fourth: Now I have to create a code that will choose thoose exercises, but HOW?
No idea.. hahahaha  
I must add some filters too...  
Should I create a website? Or an app?  
Probably an website is the best rigth now  
BUT, FIRST I MUST SETUP THE PROGRAM OFFILINE :D (I GUESS, who knows!?")  


##### I want to be able to define some filters like: === [NOT YET]
* Which muscles I will train each day 
* How many exercises I want to do per day
* Which exercises I don't want to do
* Push/Pull/Legs | Antagonists | Push/Pull | ABCD | ABCDE...
* So on...