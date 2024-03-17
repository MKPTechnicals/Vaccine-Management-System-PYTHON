# Vaccination Center Management System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-blue.svg)](https://www.mysql.com/)

This Python script facilitates the management of a vaccination center. It allows registration for vaccination, entry of vaccinated individuals, and searching vaccination records by Aadhaar number.

## Features

- **Registration**: Users can register for vaccination by providing their details such as name, Aadhaar number, city, contact number, dose number, and vaccine type (Covaxin or Covishield).
- **Vaccination Entry**: Authorized personnel can record the entry of vaccinated individuals by providing necessary details including name, Aadhaar number, city, contact number, and vaccine type.
- **Search**: Allows searching vaccination records by Aadhaar number to retrieve information about the doses administered to the individual.

## Setup

1. Install Python if not already installed.
2. Install the required `mysql.connector` module using pip: `pip install mysql-connector-python`.
3. Replace placeholder database credentials with your actual database details in the script.
4. Execute the script in a Python environment.

## Personal Information Replacement

To ensure the security of your personal information and database credentials, follow these steps to replace the placeholder values with your actual data:

1. **Database Credentials:**
   - Open the script and locate the database connection section.
   - Replace `"HOST"`, `"USERNAME"`, `"PASSWORD"`, and `"DATABASE"` with your actual database hostname, username, password, and database name respectively.

2. **PIN Code (Optional):**
   - If you want to change the PIN code required for certain operations, locate the PIN verification section.
   - Update the PIN value (currently set to `1265`) with your desired PIN code.

3. **Execution:**
   - Once all personal information is replaced, save the changes to the script.
   - Execute the script in your Python environment.

By following these steps, you can safely manage and operate the vaccination center management system with your own database and PIN code.

## Creating Database Tables

Before using the script, make sure to create the necessary tables in your MySQL database with the following schema:

```sql
CREATE TABLE DOSE_1_COVAXIN (
    CITY VARCHAR(50) NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    DATE DATETIME NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    AADHAAR BIGINT NOT NULL
);

CREATE TABLE DOSE_1_COVISHIELD (
    NAME VARCHAR(50) NOT NULL,
    DATE DATETIME NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    AADHAAR BIGINT NOT NULL
);

CREATE TABLE DOSE_2_COVAXIN (
    AADHAAR BIGINT NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    DATE DATETIME NOT NULL,
    NAME VARCHAR(50) NOT NULL
);

CREATE TABLE DOSE_2_COVISHIELD (
    CITY VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    DATE DATETIME NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    AADHAAR BIGINT NOT NULL
);

CREATE TABLE REGISTRATION_COVAXIN (
    AADHAAR BIGINT NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    DATE DATETIME NOT NULL,
    DOSE INT NOT NULL,
    NAME VARCHAR(50) NOT NULL
);

CREATE TABLE REGISTRATION_COVISHIELD (
    AADHAAR BIGINT NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    CONTACT_NUMBER BIGINT NOT NULL,
    DATE DATETIME NOT NULL,
    DOSE INT NOT NULL,
    NAME VARCHAR(50) NOT NULL
);
```

Execute these SQL statements in your MySQL database to create the necessary tables. Ensure that the table names, field names, and data types match the provided schema.

By following these steps, you can safely manage and operate the vaccination center management system with your own database and PIN code.

## Usage

1. Run the script.
2. Select the desired option:
   - Register for vaccination (Option 1)
   - Record vaccination entry (Option 2)
   - Search vaccination records (Option 3)
   - Exit (Option 0)

## Authors

- [@mkptechnicals](https://www.github.com/MKPTechnicals)
