import mysql.connector

class MySQL_Intents_Keywords:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(host = host,
             user = user,
             password = password,
             database = database,
             auth_plugin='mysql_native_password')

    # Queries for databases
    def show_databases(self):
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("SHOW DATABASES;")
        return cursor.fetchall()

    def use_database(self,db_name):
        # Enter to database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("USE {};".format(db_name))
        print('Database entering is successful')

    def show_tables(self,db_name):
        # Show tabales inside the database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('USE {};'.format(db_name))
        cursor.execute('SHOW TABLES;')
        return cursor.fetchall()

    def read_data_from_table(self,db_name,table_name):
        # Read data from a table
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('SELECT * FROM {}.{};'.format(db_name,table_name))
        return cursor.fetchall()

    def create_table(self,db_name,table_name):
        # Creating a new table
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("""CREATE TABLE {}.{} (
                        recharge_issue VARCHAR(30),
                        network_issue VARCHAR(30),
                        service_issue VARCHAR(30));""".format(db_name,table_name))
        print('{} Table creating is successful'.format(table_name))

    def insert_data(self,table_name,column,list_of_records):
        # Entering data to the table
        cursor = self.connection.cursor()
        for record in list_of_records:
            # Execute the query
            query = """INSERT INTO {}({}) VALUES ('{}')""".format(table_name,column,record)
            cursor.execute(query)
            self.connection.commit()

        print("Records are entered successfully")

    def read_column_data(self,table_name,column):
        # Reading one column from table
        cursor = self.connection.cursor()
        query = """SELECT {} FROM {} WHERE {} IS NOT NULL;""".format(column,table_name,column)
        # Execute the query
        cursor.execute(query)
        return cursor.fetchall()

    def add_new_coulumn(self,table_name,column_name,data_type):
        # Add new column to existing table
        cursor = self.connection.cursor()
        query = """ALTER TABLE {} ADD {} {};""".format(table_name,column_name,data_type)
        # Execute the query
        cursor.execute(query)
        print("New column is added successfully")

    def drop_column(self,table_name,column):
        # Drop existing column from table
        cursor = self.connection.cursor()
        query = """ALTER TABLE {} DROP COLUMN {};""".format(table_name,column)
        # Execute the query
        cursor.execute(query)
        print("Column is dropped successfully")

    def get_column_names(self,table_name):
        # Getting column names in a table
        cursor = self.connection.cursor()
        query = """SHOW COLUMNS FROM {};""".format(table_name)
        # Execute the query
        cursor.execute(query)
        data = cursor.fetchall()

        columns = []
        for i in data:
            columns.append(i[0])
        return columns

#dbObj = MySQL_Results('146.148.85.146','root','Omnibis.1234','speech')
#print(dbObj.get_column_names('keywords'))