# import psycopg
import mariadb
import sys
from gui import GUI
import pprint

"""# Connecting to DataBase Promatik
hostname = '185.209.248.73'
db_name = 'pdm_search'
db_port = '5432'
db_user = 'postgres'
db_password = 'Zlyziemniak666'
"""

""  # Connecting to DataBase Localhost
hostname = '185.209.248.73'
db_name = 'PDM_SOE'
db_port = '3307'
db_user = 'kwroblewski'
db_password = 'Bazadanych_mdb10!'""


class SQL:

    @staticmethod
    def connection_to_db(db_name):

        try:
            conn = mariadb.connect(
                user="kwroblewski",
                password="Bazadanych_mdb10!",
                host="185.209.248.73",
                port=3307,
                database="PDM_SOE")

            print("connected")
            return conn

        except:
            print("Error connecting to database")

    @staticmethod
    def close_db(my_db):
        # Zamknij połączenie
        my_db.close()

    @staticmethod
    def read_db(read_query):
        my_db = SQL.connection_to_db(db_name)
        # Utwórz kursor, który będzie wykonywał zapytania
        cursor = my_db.cursor()
        # Wykonaj zapytanie
        cursor.execute(read_query)
        # Pobierz wyniki zapytania
        results_from_read_query = cursor.fetchall()
        SQL.close_db(my_db)
        return results_from_read_query

    @staticmethod
    def update_db(update_quarry):
        my_db = SQL.connection_to_db(db_name)
        # Utwórz kursor, który będzie wykonywał zapytania
        cursor = my_db.cursor()
        # Wykonaj zapytanie
        cursor.execute(update_quarry)
        my_db.commit()
        SQL.close_db(my_db)
        return True

    @staticmethod
    def input_db(input_query):
        my_db = SQL.connection_to_db(db_name)
        # Utwórz kursor, który będzie wykonywał zapytania
        cursor = my_db.cursor()
        # Wykonaj zapytanie
        cursor.execute(input_query)
        my_db.commit()
        SQL.close_db(my_db)
        return True

    @staticmethod
    def print_db_results(results_from_query):
        my_db = SQL.connection_to_db(db_name)
        # Wyświetl wyniki
        for row in results_from_query:
            row = str(row).encode('utf-8')
            print(row)
        SQL.close_db(my_db)


SQL.connection_to_db("PDM_SOE")
