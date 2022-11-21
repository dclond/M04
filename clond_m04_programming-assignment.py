"""
David Clond
SDEV 220 M04 Programming Assignmnet
clond_m04_programming-assignment.py


This application solves the problems for the following 11.1, 11.2, and 16.8
"""

# 11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
import zoo

zoo.hours()


# 11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
import zoo as menagerie

menagerie.hours()


# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As in 16.6, select and print the title column from the book table in alphabetical order.

# 16.4 work
import sqlite3
my_db = sqlite3.connect('books.db')
my_cursor = my_db.cursor()
my_cursor.execute("create table book (title text, author text, year int)")
my_db.commit()

# 16.5 work
import csv
insert_query = 'insert into book values(?, ?, ?)'


with open('books2.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        my_cursor.execute(insert_query, (book['title'], book['author'], book['year']))

my_db.commit()

import sqlalchemy
my_connection = sqlalchemy.create_engine('sqlite:///books.db')
my_query = 'select title from book order by title asc'
my_rows = my_connection.execute(my_query)
for row in my_rows:
    print(row)
