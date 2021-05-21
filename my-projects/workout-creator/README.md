# Workout Creator

## Generate a workout program by choosing "randomly" the exercises for each muscle group.
## This approach may help you to avoid injury and to have results more consistently.

### I want to be able to define some filters like: === [NOT YET]
Markup : * Which muscles I will train each day 
         * How many exercises I want to do per day
         * Which exercises I don't want to do
         * So on...

## Development process:

### First: I scrap the exrx.net (they have one of the biggest exercise database avaiable for free online (+1800 exercises))
####        Get all the links to the exercises pages ==== [OK]
####        Get all the exercises info

### Second: Create a efficiently SQL database (probably the SQLite is enough)