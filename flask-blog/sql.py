import sqlite3

# create a new database if the database doesn't exist
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE posts
            (title TEXT, post TEXT)
            """)

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Exellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
