# import from CSV

import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it  to a variable
    employees = csv.reader(open("employees.csv", newline=''))

    # create a new table called employees
    #c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)
