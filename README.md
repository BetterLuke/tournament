# Tournament database

Tournament Results Database

In this assignment a Python module that uses a PostgreSQL database to keep track of players and matches in a game. Where the tournament system used is a Swiss System for pairing up players

#This project has two parts:

The database schema is contained in tournament.sql. It contains two tables and three views.

The tournament.py file contains the python code that uses the sql database and tables.

The tournament_test.py ensures that the rules of the Swiss system work by 'passing' the criteria.

#Dependecies:

- Virtualbox - https://www.virtualbox.org/wiki/Downloads
- Vagrant - https://www.vagrantup.com/downloads.html
- Clone the Vagrant VM from Udacity - http://github.com/udacity/fullstack-nanodegree-vm

#Run the program

- Navigate to the Vagrant VM that you downloaded from Udacity's github
- Use vagrant up to start the vagrant vm then run the command vagrant ssh to login
- Create a copy of the tournament folder in the vagrant folder
- Run psql -f tournament.sql
- Run python tournament_test.py
