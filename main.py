##################### Extra Hard Starting Project ######################
import pandas
import datetime
import smtplib, ssl
import random 

mail = ""
password = ""

BIRTHDAY_PERSON = ""
IS_BIRTHDAY = False
# 1. Update the birthdays.csv
birthdays = pandas.read_csv("./birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
for i in birthdays["month"]:
    birthday_date = birthdays["day"]
    birthday_month = birthdays["month"]
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    bday_bool = False
    bmonth_bool = False

    try:
        bday = birthdays[birthdays.day == day]
        bmonth = birthdays[birthdays.month == month]
    except ValueError:
        pass
    else:
        bday_bool = True
        bmonth_bool = True
        if bday_bool and bmonth_bool:
            BIRTHDAY_PERSON = bday.name
            IS_BIRTHDAY = True

if IS_BIRTHDAY:    
        for name in BIRTHDAY_PERSON:
            rand_num = random.randint(1, 3)
            b_name = name
            with open(f"./letter_templates/letter_{rand_num}.txt") as letter:
                content = letter.read()
                b_letter = content.replace("[NAME]", b_name.capitalize())
            
            person = birthdays[birthdays.name == BIRTHDAY_PERSON]
            addrs = person.email
            addrs = addrs.to_string(index=False)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=mail, password=password)
                connection.sendmail(mail, addrs, 
                msg=f"Subject: Happy Birthday!!!\n\n{b_letter}")





