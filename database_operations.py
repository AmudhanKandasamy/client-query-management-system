#database_operations.py
#Import necessary packages
import pymysql
import pandas as pd
from datetime import datetime
from config import DATABASE_CONFIGURATION

#Function for database connection
def get_connection():
    return pymysql.connect(**DATABASE_CONFIGURATION)

#Function for login check
def login_user(username, hashed_pw):
    try:
        print(f"[DEBUG] login_user: {username}")
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT role
            FROM users
            WHERE username = %s AND hashed_password = %s
        """
        cursor.execute(sql, (username, hashed_pw))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result[0] if result else None

    except Exception as e:
        print(f"[ERROR] login_user: {e}")
        return None


#Function to facilitate the client to insert query
def insert_query(mail_id, mobile_number, query_heading, query_description):
    try:
        print(f"[DEBUG] insert_query: {mail_id}")
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO queries
            (mail_id, mobile_number, query_heading, query_description, status, query_created_time)
            VALUES (%s, %s, %s, %s, 'Open', %s)
        """

        cursor.execute(
            sql,
            (mail_id, mobile_number, query_heading, query_description, datetime.now())
        )

        conn.commit()
        cursor.close()
        conn.close()

        print("[DEBUG] insert_query: Success")

    except Exception as e:
        print(f"[ERROR] insert_query: {e}")
        raise


#Function to fetch all the queries
def fetch_all_queries():
    try:
        print("[DEBUG] fetch_all_queries")
        conn = get_connection()

        df = pd.read_sql(
            "SELECT * FROM queries ORDER BY query_id DESC",
            conn
        )

        conn.close()
        return df

    except Exception as e:
        print(f"[ERROR] fetch_all_queries: {e}")
        return pd.DataFrame()


#Function to mark queries as closed
def mark_as_closed(query_id):
    try:
        print(f"[DEBUG] mark_as_closed: {query_id}")
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE queries
            SET status = 'Closed',
                query_closed_time = %s
            WHERE query_id = %s
        """

        cursor.execute(sql, (datetime.now(), query_id))
        conn.commit()

        cursor.close()
        conn.close()

        print("[DEBUG] mark_as_closed: Success")

    except Exception as e:
        print(f"[ERROR] mark_as_closed: {e}")
        raise
