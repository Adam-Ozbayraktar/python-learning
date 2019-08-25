import random
import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # creates a tuple of random ints
    random_numbers = [(random.randint(0,100), ) for i in range(100)]

    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")

    c.executemany("INSERT INTO numbers VALUES(?)", random_numbers)

    user_input = ""
    prompt = """
Select operation tha you want to perform [1-6]:
1. Average
2. Max
3. Min
4. Sum
5. Get all operations
6. Exit

"""
    while True:

        user_input = int(input(prompt))

        sql = { 1: "SELECT avg(num) FROM numbers",
                2: "SELECT max(num) FROM numbers",
                3: "SELECT min(num) FROM numbers",
                4: "SELECT sum(num) FROM numbers",}

        if user_input in sql.keys():
            c.execute(sql[user_input])
            print(f"Result: {c.fetchone()[0]}")

        elif user_input == 5:
            for keys, values in sql.items():
                c.execute(values)
                result = c.fetchone()
                print(f"{keys}: {result[0]}")

        else:
            break
