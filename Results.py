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

    user = input("Please enter your name: ")
    password = input("and your password please...: ")
    if user in Auth_user and password in Password:
        print("Welcome to your F1 application " + user)
        loop = 'false'
    else:
        print("Invalid username/password!")
        print("Access denied!")
cur = db.cursor()

print("Here are the season results to date: ")
cur.execute("SELECT * from results")

for row in cur.fetchall():
    print(row)

current_race = input("Latest race? : ")
count = 0



# print all the first cell of all the rows
for row in cur.fetchall():
    print(row)

db.close()

