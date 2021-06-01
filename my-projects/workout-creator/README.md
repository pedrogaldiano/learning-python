## Workout Creator
My goal is to create an application capable of Generate a workout program by choosing "randomly" the exercises for each muscle group defined by some filters. This approach may help you to avoid injury and to have results more consistently.

------------------------
### IMPORTANT:
I just figured out that the Terms of Use of exrx.net don't allow scrapping or any form of copying its content.  Because of this, I'm removing the database I have created with its data and the scrapping application I created.

Sorry, I didn't know it was prohibited.  
I will get data from an [open source project in git hub from davejt](https://github.com/davejt/exercise). I choose to not use the API since the most crucial part of the data I can get from a CSV file.  

I'm throwing away all my work so far, and I won't hide this because were part of my development process. :)  


## Development process:

#### 1°: I scrap the exrx.net (they have one of the biggest exercise database avaiable for free online (+1400 exercises))
* Get all the links to the exercises pages ==== [OK]  
* Get all the exercises info ==== [OK]  

#### 2º: Create an efficiently SQL database (probably the SQLite is enough)
* Store everything in one table ==== [OK]  
* MAKE TWO BACKUPS (GIT + LOCAL) ==== [OK]  
* Clean up the database (took way longer than a expected) ==== [OK]  
* Find out which collumns could be break in a relational database === [OK]  
* Create a relational database === [OK]  

#### 3°: Get the data from an open source and delete some things
* Get the [exercise database](https://github.com/davejt/exercise) in CSV ==== [OK]  
* Delete the database created with the exrx.net data ==== [OK]  
* Delete the python file with the scrapping application ==== [OK]  
* I decided to delete everything, most of the files were dependents on the scrapping or database, so it didn't make sense to keep any of them.  
* Create a SQLite database with the data from the CSV file ==== [OK]  

#### 4°: Choose the exercises based on something simple
* You can generate a unique set of exercises within one of thoose routines: Full Body, Push/Pull, and Push/Pull/Legs ==== [OK]  
* I want to add more features to be able to choose the muscles you want to workout, define how many exercises you want to do, change the number of sets and reps per exercise and so on... But, I will keep it simple at first.

#### 5°: Create a web application (so you can actually show everything)
* Create the html page (all in one page)  
* Create a css file
* Add photos showing the muscle groups you are going to workout  
* Create hiperlinks from the name of the exercise to the you tube so you can search this particular exercise  
* Use Flask (how? I'm not sure, rewatch CS50 Flask class)  
*