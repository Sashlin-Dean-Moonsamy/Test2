# Import Modules
import datetime
import csv
import random

# Create lists to store names and surnames
names = ["Bruce", "Clark", "louis", "Stephen", "Peter",
         "Tony", "Scarlet", "Diana", "Harley", "Steve",
         "Walter", "Olivia", "Selina", "Christiano", "Itachi",
         "Anakin", "Luke", "lea", "Harry", "jeff"]

surnames = ["Wayne", "Kent", "Lane", "Strange", "Parker",
            "Stark", "Johansen", "Ross", "Quinn", "Rodgers",
            "Bishop", "Dunham", "Kyle", "Ronaldo", "Uchiha",
            "Skywalker", "Kenobe", "Green", "Potter", "Dean"]


# Def function that generates an appropriate date of birth and ID
def dob_and_id(year_of_birth):
    month_of_birth = f"{random.randint(1, 13):02d}"
    day_of_birth = f"{random.randint(1, 32):02d}"

    if month_of_birth == "02" and int(day_of_birth) > 28:
        day_of_birth = "28"

    elif month_of_birth[-1] == "02" and year_of_birth % 4 == 0:
        day_of_birth = "29"

    elif int(month_of_birth) % 2 == 0 and day_of_birth == "31":
        day_of_birth = 30

    date_of_birth = str(year_of_birth) + "-" + str(month_of_birth) + "-" + str(day_of_birth)
    id_num = date_of_birth[2:].replace("-", "") + str(random.randint(1000000, 9999999))

    if len(id_num) != 13:
        return dob_and_id(year_of_birth)

    return date_of_birth, id_num


# Def function to validate record
def is_valid(random_record, list_of_records):
    if random_record in list_of_records:
        return False

    return True


# Def function that generates csv file
def gen_csv(random_count):
    with open("output/output.csv", "w", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Surname", "Initials", "Age", "Date Of Birth"])
        list_of_records = []

        for i in range(random_count):
            record = gen_record(list_of_records)
            list_of_records.append(record)
            writer.writerow(record)

        return "File Successfully Generated"


# Def function that generates a single record
def gen_record(list_of_records):
    current_date = str(datetime.date.today())
    current_year = int(current_date[0:4])
    year_of_birth = random.randint(1950, current_year)
    date_of_birth, id_num = dob_and_id(year_of_birth)
    age = str(current_year - year_of_birth)
    name = random.choice(names)
    surname = random.choice(surnames)

    random_record = [id_num, name, surname, (name[0] + surname[0]), str(age), date_of_birth]

    if is_valid(random_record, list_of_records):
        return random_record

    return gen_record(list_of_records)
