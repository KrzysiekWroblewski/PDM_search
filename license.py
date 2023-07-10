import mysql.connector
import pyodbc
import sys
from gui import GUI

# Connecting to DataBase
db_name = "sql_armory_app"


def connection_to_db(db_name):
    endpoint = 'kwdatabase-2.cgqntnxhba1n.us-east-1.rds.amazonaws.com'
    port = '1433'
    db_name = 'PDM_Search'
    db_user = 'Admin'
    db_password = 'pdm_search'

    conn_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server={endpoint},{port};Database={db_name};UID={db_user};PWD={db_password}"
    conn = pyodbc.connect(conn_str)

    """cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)"""

    return conn


def close_db(my_db):
    # Zamknij połączenie
    my_db.close()


def read_db(read_query):
    my_db = connection_to_db(db_name)
    # Utwórz kursor, który będzie wykonywał zapytania
    cursor = my_db.cursor()
    # Wykonaj zapytanie
    cursor.execute(read_query)
    # Pobierz wyniki zapytania
    results_from_read_query = cursor.fetchall()
    close_db(my_db)
    return results_from_read_query


def update_db(update_quarry):
    my_db = connection_to_db(db_name)
    # Utwórz kursor, który będzie wykonywał zapytania
    cursor = my_db.cursor()
    # Wykonaj zapytanie
    cursor.execute(update_quarry)
    my_db.commit()
    close_db(my_db)
    return True


def input_db(input_query):
    my_db = connection_to_db(db_name)
    # Utwórz kursor, który będzie wykonywał zapytania
    cursor = my_db.cursor()
    # Wykonaj zapytanie
    cursor.execute(input_query)
    my_db.commit()
    close_db(my_db)
    return True


def print_db_results(results_from_query):
    my_db = connection_to_db(db_name)
    # Wyświetl wyniki
    for row in results_from_query:
        row = str(row).encode('utf-8')
        print(row)
    close_db(my_db)


def log_in():
    license = read_db(
        "SELECT license FROM company WHERE company_name = 'Promatik';")
    license = license[0][0]

    if license == "8Ay6sfV70E":
        pass
    else:
        GUI.Mbox("Pdm_search", "Error", 1)
        sys.exit()
