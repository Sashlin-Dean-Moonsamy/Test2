# Import Modules
import sqlite3
import pandas as pd

# Create connection and cursor
connection = sqlite3.connect("database.db", check_same_thread=False)
cursor = connection.cursor()


# Def function that creates new table if not exists
def create_table(name):
    cursor.execute(f"Create Table if Not Exists {name}("
                   f"id_num TEXT UNIQUE PRIMARY KEY,"
                   f"name Text NOT NUll,"
                   f"surname TEXT NOT NULL,"
                   f"initials TEXT NOT NULL,"
                   f"age TEXT NOT NULL,"
                   f"date_of_birth TEXT NOT NULL)")

    connection.commit()


# Create Function to refactor ID Number From database
def refactor(id_num):
    while len(id_num) < 13:
        id_num = "0" + id_num

    return id_num


# Def function that reads from db and return html table
def read_db(name):
    cursor.execute(f"SELECT * FROM {name}")

    results = cursor.fetchall()
    table = ""

    for item in results:

        table += f"<tr>" \
                 f"<th>{refactor(item[0])}</th>" \
                 f"<th>{item[1]}</th>" \
                 f"<th>{item[2]}</th>" \
                 f"<th>{item[3]}</th>" \
                 f"<th>{item[4]}</th>" \
                 f"<th>{item[-1]}</th>" \
                 f"</tr>"

    return table


# Def function that inserts into
def insert_db(directory, name):
    if "." in name:
        name = name[:-4]

    df = pd.read_csv(f"{directory}")
    create_table(name)

    for i in range(len(df)):
        id_num = df["ID"][i]
        rec_name = df["Name"][i]
        surname = df["Surname"][i]
        initials = df["Initials"][i]
        age = df["Age"][i]
        date_of_birth = df["Date Of Birth"][i]

        cursor.execute(f"""INSERT INTO {name}(
                        id_num,
                        name,
                        surname,
                        initials,
                        age,
                        date_of_birth
                        )
                        VALUES(
                        '{id_num}',
                        '{rec_name}',
                        '{surname}',
                        '{initials}',
                        '{age}',
                        '{date_of_birth}'
                        );
                        """
                       )
        connection.commit()

    return read_db(name)
