# import libraries
import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
import pdb


# load file from .env file
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


# establish cursor and connection
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)


# create a new table
query = """
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived bool,
    pclass int,
    name varchar,
    sex varchar,
    age int,
    sib_spouse_count int,
    parent_child_count int,
    fare float8
);
"""


# import dataframe
df = pd.read_csv('/home/andronik/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', delimiter=',')
results = df.values.tolist()


# loop over and actually insert all the results
for result in results:
    insert_results = f"""
    INSERT INTO passengers
    (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare)
    VALUES ({bool(result[0])},{result[1]}, '{result[2]}', '{result[3]}', {result[4]}, {result[5]}, {result[6]}, {result[7]})
    """
    curs = connection.cursor()
    print(insert_results)
    curs.execute(insert_results)
    connection.commit()
