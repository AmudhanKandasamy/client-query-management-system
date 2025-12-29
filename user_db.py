#user_db.py - Run this file only once.
#Import necessary packages
import pymysql
import hashlib
from config import DATABASE_CONFIGURATION

#Function for hashing the password
def hash_password(pw):
    
    #Return hashed password
    return hashlib.sha256(pw.encode()).hexdigest()

#Function to insert user credentials details in the users database
def add_users_credentials():
    conn = pymysql.connect(**DATABASE_CONFIGURATION)
    cursor = conn.cursor()

    users_credentials_to_insert = [
        ("Amy", hash_password("Client1@01#"), "Client"),
        ("Ben", hash_password("Client2@02#"), "Client"),
        ("Tom", hash_password("Support1@01#"), "Support"),
        ("Zen", hash_password("Support2@02#"), "Support")
    ]

    sql = """
        INSERT INTO users (username, hashed_password, role)
        VALUES (%s, %s, %s)
    """

    cursor.executemany(sql, users_credentials_to_insert)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_users_credentials()
    print("User credentials added to database!")