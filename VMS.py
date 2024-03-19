import mysql.connector
from datetime import datetime

def registration(cursor):
    try:
        name = input("Enter Name:")
        aadhar = int(input("Enter Aadhaar No.:"))

        # Check if the user is already vaccinated for the 1st dose
        already_vaccinated_query = f"SELECT * FROM DOSE_1_COVAXIN WHERE AADHAAR={aadhar} UNION SELECT * FROM DOSE_1_COVISHIELD WHERE AADHAAR={aadhar}"

        cursor.execute(already_vaccinated_query)

        if cursor.fetchone():
            print("You are not eligible for 1st dose registration. You are already vaccinated for the 1st dose.")
            return

        city = input("Enter your city:")
        contactno = int(input("Enter Contact No.:"))
        dose = int(input("Enter dose of vaccination(1 or 2):"))
        vaccine = input("Enter name of vaccine(Covaxin or Covishield):").capitalize()

        sql = ""
        if dose == 1:
            if vaccine == "Covaxin":
                sql = f"INSERT INTO REGISTRATION_COVAXIN (NAME,AADHAAR,CITY,CONTACT_NUMBER,DATE,DOSE) VALUES ('{name}', {aadhar}, '{city}', {contactno}, now(), 1)"
            elif vaccine == "Covishield":
                sql = f"INSERT INTO REGISTRATION_COVISHIELD (NAME,AADHAAR,CITY,CONTACT_NUMBER,DATE,DOSE) VALUES ('{name}', {aadhar}, '{city}', {contactno}, now(), 1)"
            else:
                print("Invalid vaccine name")
                return
        elif dose == 2:
            # Check if the user is eligible for 2nd dose
            eligibility_query = f"SELECT DOSE FROM DOSE_1_COVAXIN WHERE AADHAAR={aadhar} UNION SELECT DOSE FROM DOSE_1_COVISHIELD WHERE AADHAAR={aadhar}"
            cursor.execute(eligibility_query)
            eligible_for_2nd_dose = any(row[0] == 1 for row in cursor.fetchall())

            if not eligible_for_2nd_dose:
                print("You are not eligible for 2nd dose registration. Please get your 1st dose first.")
                return

            # Check if the user is already vaccinated for the 2nd dose
            already_vaccinated_query2 = f"SELECT * FROM DOSE_2_COVAXIN WHERE AADHAAR={aadhar} UNION SELECT * FROM DOSE_2_COVISHIELD WHERE AADHAAR={aadhar}"
            cursor.execute(already_vaccinated_query2)

            if cursor.fetchone():
                print("You are not eligible for 2nd dose registration. You are already vaccinated for the 2nd dose.")
                return

            if vaccine == "Covaxin":
                sql = f"INSERT INTO REGISTRATION_COVAXIN (NAME,AADHAAR,CITY,CONTACT_NUMBER,DATE,DOSE) VALUES ('{name}', {aadhar}, '{city}', {contactno}, now(), 2)"
            elif vaccine == "Covishield":
                sql = f"INSERT INTO REGISTRATION_COVISHIELD (NAME,AADHAAR,CITY,CONTACT_NUMBER,DATE,DOSE) VALUES ('{name}', {aadhar}, '{city}', {contactno}, now(), 2)"
            else:
                print("Invalid vaccine name")
                return
        else:
            print("Enter valid dose for vaccination")
            return

        cursor.execute(sql)
        print(f"Registered for {'1st' if dose == 1 else '2nd'} dose vaccination")

    except mysql.connector.Error as e:
        print("Error: ", e)

def vaccinated(cursor, n):
    try:
        pin = int(input("Enter PIN:"))
        if pin != 1265:
            print("Wrong PIN")
            return
        name = input("Enter Name:")
        aadhar = int(input("Enter Aadhaar No.:"))
        city = input("Enter your city:")
        contactno = int(input("Enter Contact No.:"))
        vaccine = input("Enter name of vaccine(Covaxin or Covishield):").capitalize()

        table_name = ""
        if n == 1 and vaccine == "Covaxin":
            table_name = "DOSE_1_COVAXIN"
        elif n == 1 and vaccine == "Covishield":
            table_name = "DOSE_1_COVISHIELD"
        elif n == 2 and vaccine == "Covaxin":
            table_name = "DOSE_2_COVAXIN"
        elif n == 2 and vaccine == "Covishield":
            table_name = "DOSE_2_COVISHIELD"
        else:
            print("Invalid dose or vaccine")
            return

        sql = f"INSERT INTO {table_name} (NAME,AADHAAR,CITY,CONTACT_NUMBER,DATE) VALUES ('{name}', {aadhar}, '{city}', {contactno}, now())"

        cursor.execute(sql)
        print(f"{name} is vaccinated for {'1st' if n == 1 else '2nd'} dose")

    except mysql.connector.Error as e:
        print("Error: ", e)

def search(cursor, aadhar):
    try:
        sql1 = f"SELECT *, 'Covaxin' AS VACCINE FROM DOSE_1_COVAXIN WHERE AADHAAR={aadhar} UNION SELECT *, 'Covishield' AS VACCINE FROM DOSE_1_COVISHIELD WHERE AADHAAR={aadhar}"

        cursor.execute(sql1)

        found = False

        for row in cursor.fetchall():
            found = True
            print("--------------------------------------------------")
            print("Name:", row[1])
            print("Aadhar No.:", row[2])
            print("City:", row[3])
            print("Contact No.:", row[4])
            print("Dose: 1")
            print("Vaccine:", row[5])
            print("--------------------------------------------------")

        sql2 = f"SELECT *, 'Covaxin' AS VACCINE FROM DOSE_2_COVAXIN WHERE AADHAAR={aadhar} UNION SELECT *, 'Covishield' AS VACCINE FROM DOSE_2_COVISHIELD WHERE AADHAAR={aadhar}"
        cursor.execute(sql2)

        for row in cursor.fetchall():
            found = True
            print("--------------------------------------------------")
            print("Name:", row[1])
            print("Aadhar No.:", row[2])
            print("City:", row[3])
            print("Contact No.:", row[4])
            print("Dose: 2")
            print("Vaccine:", row[5])
            print("--------------------------------------------------")

        if not found:
            print("--------------------------------------------------")
            print("No data found for Aadhaar:", aadhar)
            print("--------------------------------------------------")
    except mysql.connector.Error as e:
        print("--------------------------------------------------")
        print("Error: ", e)
        print("--------------------------------------------------")

try:
    connection = mysql.connector.connect(
        host="HOST",
        user="USERNAME",
        password="PASSWORD",
        database="DATABASE"
    )
    cursor = connection.cursor()

    while True:
        print("_________________________________")
        print("-------Vaccination Centre--------")
        print("_________________________________")
        print("1.Registration for vaccination")
        print("2.Entry of vaccinated person")
        print("3.Search")
        print("0.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            registration(cursor)
        elif choice == 2:
            choice1 = int(input("Enter dose number:"))
            vaccinated(cursor, choice1)
        elif choice == 3:
            aadhar = int(input("Enter Aadhaar Number:"))
            search(cursor, aadhar)
        else:
            print("Invalid Choice")

finally:
    if 'connection' in locals():
        connection.close()
