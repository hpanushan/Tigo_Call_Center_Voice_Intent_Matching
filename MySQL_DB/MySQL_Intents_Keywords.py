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
        cursor.execute("""CREATE TABLE IF NOT EXISTS {}.{} (keywords VARCHAR(30) NOT NULL);""".format(db_name,table_name))
        print('{} Table creating is successful'.format(table_name))

    def insert_data(self,table_name,list_of_records):
        # Entering data to the table
        cursor = self.connection.cursor()
        for record in list_of_records:
            # Execute the query
            query = """INSERT INTO {}(keywords) VALUES ('{}')""".format(table_name,record)
            cursor.execute(query)
            self.connection.commit()

        print("Records are entered successfully")

    def read_column_data(self,table_name):
        # Reading one column from table
        cursor = self.connection.cursor()
        query = """SELECT keywords FROM {};""".format(table_name)
        # Execute the query
        cursor.execute(query)
        data = cursor.fetchall()

        records = []
        for i in data:
            records.append(i[0])
        return records

    def drop_table(self,table_name):
        # Drop existing table from database
        cursor = self.connection.cursor()
        query = """DEOP TABLE IF EXISTS {};""".format(table_name)
        # Execute the query
        cursor.execute(query)
        print("Table is dropped successfully")

    def get_table_names(self):
        # Getting column names in a table
        cursor = self.connection.cursor()
        query = """SHOW TABLES;"""
        # Execute the query
        cursor.execute(query)
        data = list(cursor.fetchall())

        # Remove 'results' value from list
        data.remove(('results',))

        intent_names = []
        for i in data:
            intent_names.append(i[0])
        return intent_names


#dbObj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
#dbObj.insert_data('service_issue',['deactiv','activ','packag'])
#dbObj.create_table('speech','service_issue')
#print(dbObj.read_column_data('service_issue'))
#dbObj.drop_table('keywords')
#print(dbObj.get_table_names())