import pymysql
import time
import sys
import getpass


# Database connection setup
db = pymysql.connect(host='localhost',
                     port=3308,
                     user='root',
                     passwd='Sennadasilva50',
                     db="season")
# User validation
loop = 'true'
while loop == 'true':
    Auth_user = ['Anthony', 'anthony']
    Password = ['2017']

def login():
    user = input("Please enter your name: ")
    password = input("and your password please...: ")
    if user in Auth_user and password in Password:
        print("Welcome to your F1 application " + user)
        loop = 'false'
    else:
        print("Invalid username/password!")
        print("Access denied!")
cur = db.cursor()
login()

print("Here are the current driver standings: ")
cur.execute("SELECT * from drivers")

for row in cur.fetchall():
    print(row)

current_race = input("Latest race? : ")
count = 0
Updated_races = []
# Check that the race being updated is valid
cur.execute("SELECT * from Updated_races")
data = cur.fetchall()
if data is not None:
    x = data
    Updated_list = []
    Updated_list.append(x)
cur.execute("SELECT * from Results WHERE Race = %s", current_race)
data = cur.fetchone()
if current_race in Updated_list:
    print("The classification for this race has already been captured and cannot be modified!")
else:
    print("Enter the Top 10 finishing positions from the " + current_race + " grand prix ")
    print(Updated_list)

# Record the top 10 finishing positions for a chosen race
    while count < 1:
        driver = input("Enter a driver name: ")
        cur.execute("SELECT * from Drivers WHERE driver = %s", driver)
# Check driver is valid prior to update
        data = cur.fetchone()
        if data is None:
            print("Invalid driver, not part of the 2017 drivers championship!")
            continue
        else:
            position = input("Where did " + driver + " finish? : ")
            if position == '1st':
                cur.execute("UPDATE drivers SET Points = Points + 25 WHERE driver = %s", driver)
                #cur.execute("UPDATE Races SET  = %s", current_race)
            '''if position == '2nd':
                cur.execute("UPDATE drivers SET Points = Points + 18 WHERE driver = %s", driver)
                cur.execute("INSERT into Results (Classification) VALUES (driver + '=' + position) WHERE Race = %s", current_race)
            if position == '3rd':
                cur.execute("UPDATE drivers SET Points = Points + 15 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('3rd') WHERE Race = %s", current_race)
            if position == '4th':
                cur.execute("UPDATE drivers SET Points = Points + 12 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('4th') WHERE Race = %s", current_race)
            if position == '5th':
                cur.execute("UPDATE drivers SET Points = Points + 10 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('5th') WHERE Race = %s", current_race)
            if position == '6th':
                cur.execute("UPDATE drivers SET Points = Points + 8 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('6th') WHERE Race = %s", current_race)
            if position == '7th':
                cur.execute("UPDATE drivers SET Points = Points + 6 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('7th') WHERE Race = %s", current_race)
            if position == '8th':
                cur.execute("UPDATE drivers SET Points = Points + 4 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('8th') WHERE Race = %s", current_race)
            if position == '9th':
                cur.execute("UPDATE drivers SET Points = Points + 2 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('9th') WHERE Race = %s", current_race)
            if position == '10th':
                cur.execute("UPDATE drivers SET Points = Points + 1 WHERE driver = %s", driver)
                # cur.execute("INSERT into Races (Result) VALUES ('10th') WHERE Race = %s", current_race)'''
            count = count + 1
            cur.execute("INSERT into Updated_races (Race) VALUES (%s)", current_race)
            print(Updated_races)


    print("Top 10 finishing positions successfully updated")
    print("Update of ", current_race, " grand prix result complete")
    print("Here are the updated drivers championship standings")
    cur.execute("SELECT * from drivers")

        # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row)
    db.close()
    logout = input("Do you want to log out? Y/N")
    if logout == 'Y' or logout == 'y':
        print("You have successfully logged out")
        time.sleep(2)
        sys.exit()
    login()

login()

