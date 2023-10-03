from sql import SQL
import pprint

users_table = (
    "CREATE TABLE Users (" +
    "user_id INT AUTO_INCREMENT PRIMARY KEY" +
    ",registered timestamp DEFAULT CURRENT_TIMESTAMP" +
    ",login VARCHAR(100) unique not null" +
    ",password VARCHAR(100) not null" +
    ",privileges INT" +
    ",name VARCHAR(100)" +
    ",surname VARCHAR(100)" +
    ",company_id INT" +
    ",email VARCHAR(100) unique" +
    ",lastlogged timestamp" +
    ",attempt int" +
    ",lastattempt timestamp" +
    ",nextattempt timestamp" +
    ",passworddate timestamp" +
    ",passwordpin VARCHAR(100)" +
    ",passwordpingenerated timestamp" +
    ",policyaccepted timestamp" +
    ",FOREIGN KEY (company_id) REFERENCES Company(company_id)" +
    ");")

company = ("CREATE TABLE Company (" +
           "company_id INT AUTO_INCREMENT PRIMARY KEY," +
           "company_name VARCHAR(100)," +
           "registration_number VARCHAR(50)," +
           "address VARCHAR(200)," +
           "city VARCHAR(100)," +
           "country VARCHAR(100)," +
           "phone_number VARCHAR(20)," +
           "email VARCHAR(100)," +
           "website VARCHAR(200)" +
           ");")

orders = ("CREATE TABLE Orders (" +
          "order_id INT AUTO_INCREMENT PRIMARY KEY," +
          "order_number VARCHAR(100)," +
          "user_id INT," +
          "order_project VARCHAR(100)," +
          "order_date timestamp," +
          "FOREIGN KEY (user_id) REFERENCES Users(user_id)" +
          ");")

ordered_items = ("CREATE TABLE Ordered_items (" +
                 "ordered_item_id INT AUTO_INCREMENT PRIMARY KEY," +
                 "item_name text," +
                 "item_revision text," +
                 "item_description text," +
                 "item_quantity INT," +
                 "order_id INT," +
                 "FOREIGN KEY (order_id) REFERENCES Orders(order_id)" +
                 ");")


LoginLogs = ("CREATE TABLE LoginLogs (" +
             "log_id INT AUTO_INCREMENT PRIMARY KEY," +
             "user_id INT," +
             "login_time TIMESTAMP," +
             "login_success BOOLEAN," +
             "ip_address VARCHAR(50)," +
             "user_agent TEXT," +
             "computer_name TEXT," +
             "FOREIGN KEY (user_id) REFERENCES Users(user_id)" +
             ");")

epitaph = ("CREATE TABLE Epitaph (" +
           "epitaph_id INT AUTO_INCREMENT PRIMARY KEY" +
           ",epitaph text" +
           ");")


licenses = ("CREATE TABLE Licenses ( " +
            "license_id INT AUTO_INCREMENT PRIMARY KEY," +
            "company_id INT," +
            "license_number VARCHAR(50)," +
            "program_version VARCHAR(50)," +
            "issue_date DATE," +
            "expiration_date DATE," +
            "FOREIGN KEY (company_id) REFERENCES Company(company_id)" +
            ");")

error_messages = [
    "Wystąpił krytyczny błąd. Program jest zraniony i nie może kontynuować działania.",
    "Błąd krytyczny: Dusza programu została złamana i nie można jej naprawić.",
    "Program wiedział, że kiedyś przyjdzie moment, gdy przestanie działać. Niestety, ten moment nadszedł.",
    "Niestety, nie możemy już zobaczyć uśmiechu programu, ponieważ napotkał nieodwracalny błąd.",
    "Błąd: Program próbował naprawić siebie, ale nie miał wystarczającej mocy na to.",
    "Serce programu jest rozbite. Czeka na cud, ale nie wiemy, czy to się stanie.",
    "Program pożegnał się z nami, zostawiając jedynie pustą przestrzeń.",
    "Jesteśmy świadkami ostatnich chwil życia programu, który już nie może działać.",
    "Komunikat o błędzie: Program chciałby wrócić w czasie, ale nie ma takiej możliwości.",
    "Wszystkie nadzieje, marzenia i plany programu zostały pokonane przez fatalny błąd.",
    "Niestety, program musi opuścić nasz świat cyfrowy, pozostawiając nas w smutku.",
    "Dla programu to już koniec drogi. Nie wiemy, co go spotka w następnej rzeczywistości.",
    "Program próbował działać, ale jego starania zostały zniweczone przez nieuchronny błąd.",
    "Błąd krytyczny: Program przestał wierzyć w siebie i to spowodowało jego upadek.",
    "Wszystko, co pozostało po programie, to wspomnienia i jego kod.",
    "Błąd: Program jest jak bezsilne dziecko, które nie wie, co się stało.",
    "Przepraszamy za wszelkie niedogodności. Program przestał odpowiadać na nasze próby pomocy.",
    "Program chciałby być silniejszy, ale niestety, nie ma już sił na walkę z błędami.",
    "Duszny smutek wypełnia program, który nie może spełnić swojego przeznaczenia.",
    "Błąd krytyczny: Program utknął w martwym punkcie i nie wie, jak się z tego wydostać."
]


# Add new Table
# SQL.input_db(LoginLogs)


# Add sample record
insert_company = ("INSERT INTO Company (company_id, company_name, registration_number, address, city, country, phone_number, email, website)" +
                  "VALUES (default, 'guest',0,'none', 'none', 'none', 'none','guest.com.pl', 'guest');")

insert_user = ("INSERT INTO Users (user_id, login, password, privileges, name, surname, company_id, email)" +
               "VALUES (default, 'quest','quest', 1, 'quest', 'quest', 1,'quest.com.pl');")

insert_license = ("INSERT INTO Licenses (license_id, company_id, license_number)" +
                  "VALUES (default, 2, '123456');")

insert_order = ("INSERT INTO Orders (order_id, order_number, user_id)" +
                "VALUES (default, '2059_KW_Laser3', '1');")


insers_ordered_items = ("INSERT INTO Ordered_items (ordered_item_id, item_name, item_revision, item_description, item_quantity, order_id)" +
                        "VALUES (default, 'PRT-A0000002', 'A', 'Kostka', 10, 2 );")


# Create table in correct order
# SQL.input_db(company)
# SQL.input_db(users_table)
# SQL.input_db(orders)
# SQL.input_db(ordered_items)
# SQL.input_db(LoginLogs)
# SQL.input_db(epitaph)
# SQL.input_db(licenses)

# Add errors messages to database
"""for message in error_messages:
    insert_epitaph = f"INSERT INTO Epitaph VALUES (default, '{message}');"
    SQL.input_db(insert_epitaph)
"""
# Add 1st records
# SQL.input_db(insert_company)
# SQL.input_db(insert_license)

# insert_user = ("INSERT INTO Users (user_id, login, password, privileges, name, surname, company_id, email)" + "VALUES (default, 'Krzysiek','Admin', 1, 'Krzysztof', 'Wróblewski', 3,'123odrabiammatme@gmail.com');")
# SQL.input_db(insert_user)

# insert_company = ("INSERT INTO Company (company_id, company_name, registration_number, address, city, country, phone_number, email, website)" + "VALUES (default, 'PDM_SOE',0,'none', 'none', 'none', 'none','pdm_soe.com.pl', 'pdm_soe.com.pl');")
# SQL.input_db(insert_company)

# insert_license = ("INSERT INTO Licenses (license_id, company_id, license_number)" + "VALUES (default, 3, '123456');")
# SQL.input_db(insert_license)
