import socket
from sql import SQL
from gui import GUI
import sys
import os

# Program version is checked with database
program_version = '1.003'

login = os.getlogin()
hostname = socket.gethostname()

# check if login exist in database
# if yes let him go


def log_in():
    try:
        user_id = SQL.read_db(
            f"SELECT user_id FROM Users WHERE login = '{login}';")
        user_id = int(user_id[0][0])
        print('user_id: ', user_id)

        company_id = SQL.read_db(
            f"SELECT company_id FROM Users WHERE login = '{login}';")
        company_id = company_id[0][0]
        print('company_id: ', company_id)

        license_id = SQL.read_db(
            f"SELECT license_id FROM Licenses WHERE company_id = '{company_id}';")
        license_id = license_id[0][0]
        print('license_id: ', license_id)

        license_check = SQL.read_db(
            f"SELECT license_number FROM Licenses WHERE license_id = '{license_id}';")
        license_check = bool(license_check[0][0])
        print('license_check: ', license_check)

        program_version_check = SQL.read_db(
            f"SELECT program_version FROM Licenses WHERE license_id = '{license_id}';")
        program_version_check = program_version_check[0][0]
        print('program_version_check : ', program_version_check)

        if ((license_check == True) and (program_version_check == program_version)):
            insert_LoginLogs = (f"INSERT INTO LoginLogs (log_id, user_id, login_time, login_success, computer_name)" +
                                f"VALUES (default, {user_id}, CURRENT_TIMESTAMP, TRUE , '{hostname}');")
            LoginLogs = SQL.input_db(insert_LoginLogs)
        else:
            GUI.Mbox(
                "Pdm_search", "Error, Brak dostępu do bazy danych. Skontaktuj się ze wsparciem technicznym", 1)
            sys.exit()
    except:
        user_id = os.getlogin()
        insert_LoginLogs = (f"INSERT INTO LoginLogs (log_id, user_id, login_time, login_success, computer_name)" +
                            f"VALUES (default, 3 , CURRENT_TIMESTAMP, FALSE , '{hostname}');")
        LoginLogs = SQL.input_db(insert_LoginLogs)
        GUI.Mbox(
            "Pdm_search", "Error, Brak dostępu do bazy danych. Skontaktuj się ze wsparciem technicznym", 1)
        sys.exit()
