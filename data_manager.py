from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor 
        WHERE last_name ilike %s
        ORDER BY first_name"""
    cursor.execute(query, (last_name,))
    return cursor.fetchall()

@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city ilike %s
        ORDER BY first_name;"""
    print(f"{query=}")
    cursor.execute(query, (city,))
    return cursor.fetchall()

@database_common.connection_handler
def get_applicant_data_by_name(cursor: RealDictCursor, name: str) -> list:
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name ilike %s
        OR last_name ilike %s
        ORDER BY first_name;"""
    cursor.execute(query, (name, name,))
    return cursor.fetchall()
    
@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor: RealDictCursor, email: str) -> list:
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email ilike %s
        ORDER BY first_name; """
    mail = f'%{email}'
    cursor.execute(query, (mail,))
    return cursor.fetchall()
