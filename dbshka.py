import sqlite3 as db



with db.connect('games.db') as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS "Customers" (
                    "id_cust"	INTEGER NOT NULL UNIQUE,
                    "name"	TEXT NOT NULL,
                    "surname"	TEXT NOT NULL,
                    "phone"	TEXT NOT NULL,
                    "email"	TEXT NOT NULL,
                    PRIMARY KEY("id_cust" AUTOINCREMENT)
                    );""")
    cur.execute(""" CREATE TABLE IF NOT EXISTS "Games" (
                    "games"	INTEGER NOT NULL UNIQUE,
                    "name"	TEXT NOT NULL UNIQUE,
                    "price"	REAL NOT NULL,
                    "year"	TEXT NOT NULL,
                    "rent_price_d"	REAL NOT NULL,
                    "accessib"	TEXT NOT NULL,
                    "id_studio"	INTEGER NOT NULL,
                    PRIMARY KEY("games" AUTOINCREMENT)
                    );""")
    cur.execute(""" CREATE TABLE IF NOT EXISTS "Order_info" (
                    "id_order"	INTEGER NOT NULL UNIQUE,
                    "start_date"	TEXT NOT NULL,
                    "end_date"	TEXT NOT NULL,
                    "id_game"	INTEGER NOT NULL,
                    "id_cust"	INTEGER NOT NULL,
                    PRIMARY KEY("id_order" AUTOINCREMENT)
                    );""")
    cur.execute(""" CREATE TABLE IF NOT EXISTS "Studios" (
                    "id_studio"	INTEGER NOT NULL UNIQUE,
                    "name"	TEXT NOT NULL UNIQUE,
                    "country"	TEXT NOT NULL,
                    PRIMARY KEY("id_studio" AUTOINCREMENT)
                    );""")
    # cur.execute(""" SELECT name FROM Customers;
    #                 """)
    # customers = cur.fetchall()
    # cur.execute(""" SELECT name FROM Games;
    #                     """)
    # games = cur.fetchall()
    # for i in customers:
    #     print(i)
    # for i in games:
    #     print(i)

    # def addCustomer():
    #     inp = """" INSERT INTO Customers (name, surname, phone, email) VALUES (values[0], values[1], values[2], values[3])"""
    #     cur.execute(inp)
    #     con.commit()

    # cur.execute("""SELECT id_studio FROM Studios""")
    # ids = cur.fetchall()
    # for i in ids:
    #     print(i)
