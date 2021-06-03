## Workout Creator
My goal is to create an application capable of Generate a workout program by choosing "randomly" the exercises for each muscle group defined by some filters. This approach may help you to avoid injury and to have results more consistently.

------------------------
### IMPORTANT:
At first, I tried to get the data web scrapping the ExRx.net (they have a huge database, with more than 1800 exercises).  
But they prohibit any type of copying or scrapping of their content. So I decided to use the [open source project in git hub from davejt](https://github.com/davejt/exercise).  
I choose to not use the API since the most crucial part of the data I can get from a CSV file.  
 


## Development process:

#### 1°: Get the data from an open source and delete some things
* Get the [exercise database](https://github.com/davejt/exercise) in CSV ==== [OK]  
* Create a SQLite relatioal database with the data from the CSV file ==== [OK]  

#### 2°: Choose the exercises based on something simple
* Create the python program to pick the exercises ==== [OK]  
* You can generate a unique set of exercises within one of thoose routines: Full Body, Push/Pull, and Push/Pull/Legs ==== [OK]  
* I want to add more features to be able to choose the muscles you want to workout, define how many exercises you want to do, change the number of sets and reps per exercise and so on... But, I will keep it simple at first.

#### 3°: Create a web application (so you can actually show everything)
* Use Flask to run the web application ==== [OK]  
* Create the index.html ==== [OK]  
* Create a style.css  ==== [OK]  
* Make it mobile-friendly ==== [OK]  

#### 4°: Create the page where you show the exercises
* Create the workout.html  
* Create a dinamic table  
* Make every exercise name a link to a video of the exercise
* Show the user IMC  
* Allow the user to "save as image" or print the exercises  