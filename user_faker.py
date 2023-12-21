from faker import Faker
import psycopg2
from psycopg2 import sql

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="playground",
    user="admin",
    password="admin",
    host="127.0.0.1",
    port="5432"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table if it doesn't exist
table_creation_query = """
CREATE TABLE IF NOT EXISTS user_data (
    name VARCHAR(50),
    family VARCHAR(50),
    email VARCHAR(100),
    age INT,
    phone_number VARCHAR(15)
);
"""
cursor.execute(table_creation_query)
conn.commit()

# Generate and insert 200 random records
fake = Faker()
for _ in range(200):
    name = fake.first_name()
    family = fake.last_name()
    email = fake.email()
    age = fake.random_int(min=18, max=99)
    phone_number = fake.phone_number()[:15]

    insert_query = sql.SQL("INSERT INTO user_data (name, family, email, age, phone_number) VALUES (%s, %s, %s, %s, %s);")
    cursor.execute(insert_query, (name, family, email, age, phone_number))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data generation and insertion complete.")
