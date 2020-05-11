import logging
import mysql.connector

class MySQL_Results:

    def __init__(self, host, user, password, database):
        logging.info("mysql results constructor")
        
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
        logging.info("show databses function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("SHOW DATABASES;")
        return cursor.fetchall()

    def use_database(self,db_name):
        # Enter to database
        logging.info("entering database function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("USE {};".format(db_name))
        logging.info('database entering is successful')

    def show_tables(self,db_name):
        # Show tabales inside the database
        logging.info("show tables function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('USE {};'.format(db_name))
        cursor.execute('SHOW TABLES;')
        return cursor.fetchall()

    def read_data_from_table(self,db_name,table_name):
        # Read data from a table
        logging.info("read data function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('SELECT * FROM {}.{};'.format(db_name,table_name))
        return cursor.fetchall()

    def create_table(self,db_name,table_name):
        # Creating a new table
        logging.info("create table function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("""CREATE TABLE {}.{} (
                        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        filename VARCHAR(30) NOT NULL,
                        rechargeissue BINARY NOT NULL,
                        networkissue BINARY NOT NULL,
                        serviceissue BINARY NOT NULL,
                        other BINARY NOT NULL);""".format(db_name,table_name))
        logging.info('{} Table creating is successful'.format(table_name))

    def insert_data(self,table_name,file_name,network_issue,recharge_issue,service_issue,other):
        # Entering data to the table
        logging.info("insert data function")
        cursor = self.connection.cursor()
        # Execute the query
        query = """INSERT INTO `{}` (filename,networkissue,rechargeissue,serviceissue,other) VALUES (%s,%s,%s,%s,%s);""".format(table_name)
        val = (file_name,network_issue,recharge_issue,service_issue,other)
        cursor.execute(query, val)
        self.connection.commit()

        logging.info("record is entered successfully")

#dbObj = MySQL_Results('146.148.85.146','root','Omnibis.1234','speech')
#dbObj.create_table('speech','results')
#dbObj.insert_data("results","test3","1","0","0","0")

#print(dbObj.read_data_from_table('anushan','uploaded_contents')[-1])

