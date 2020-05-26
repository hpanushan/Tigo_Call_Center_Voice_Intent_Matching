import logging
import json
import mysql.connector

class MySQL_Intents_Keywords:

    def __init__(self, host, user, password, database):
        logging.info("mysql intents keywords constructor")

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(host = host,
             user = user,
             password = password,
             database = database,
             auth_plugin='mysql_native_password')

    def close_connection(self):
        # Closing databse connection
        logging.info("db connection closing function")
        self.connection.close()

    # Queries for databases
    def show_databases(self):
        logging.info("show databses function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("SHOW DATABASES;")
        return cursor.fetchall()

    def use_database(self,db_name):
        # Enter to database
        logging.info("use databse function")
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

    def create_table(self,db_name,table_name):
        # Creating a new table
        logging.info("create table function")
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("""CREATE TABLE IF NOT EXISTS {}.{} (intent_id INT NOT NULL AUTO_INCREMENT, intent_name VARCHAR(30), keywords json, 
                        description VARCHAR(100) ,created_by VARCHAR(30), 
                        created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (intent_id));""".format(db_name,table_name))
        logging.info('{} Table creating is successful'.format(table_name))

    def insert_data(self,table_name,intent_name,keywords,description,created_by):
        # Entering data to the table
        logging.info("insert data function")
        cursor = self.connection.cursor()
        
        # Convert list to JSON array
        json_array = json.dumps(keywords)

        # Execute the query
        query = """INSERT INTO `{}` (intent_name,keywords,description,created_by) VALUES (%s,%s,%s,%s)""".format(table_name)
        val = (intent_name,json_array,description,created_by)
        cursor.execute(query, val)
        self.connection.commit()

        logging.info("record is entered successfully")

    def read_data(self,table_name):
        # Reading one column from table
        logging.info("show databses function")
        cursor = self.connection.cursor()
        query = """SELECT * FROM {};""".format(table_name)
        # Execute the query
        cursor.execute(query)

        records = cursor.fetchall()

        # Convert list of tuples into list of lists
        list_of_lists = [list(elem) for elem in records]

        for row in list_of_lists:
            row[-1] = json.dumps(row[-1], indent=4, sort_keys=True, default=str)
        
        return list_of_lists

    def remove_row(self,table_name,intent_id):
        # Remove row from table
        logging.info("remove row function")
        cursor = self.connection.cursor()
        query = """DELETE FROM {} WHERE intent_id={};""".format(table_name,intent_id)

        # Execute the query
        cursor.execute(query)

        self.connection.commit()
        logging.info("Row is removed successfully")

    def update_row(self,table_name,intent_id,intent_name,keywords,description,created_by):
        # Update row
        logging.info("update row function")
        cursor = self.connection.cursor()

        # Convert list to JSON array
        json_array = json.dumps(keywords)
        
        query = """UPDATE `{}` SET intent_name=%s ,keywords=%s, description=%s, created_by=%s WHERE intent_id={};""".format(table_name,intent_id)
        val = (intent_name,json_array,description,created_by)

        # Execute the query
        cursor.execute(query, val)

        self.connection.commit()
        logging.info("Row is updated successfully")


    def drop_table(self,table_name):
        # Drop existing table from database
        logging.info("dropping a table function")
        cursor = self.connection.cursor()
        query = """DROP TABLE IF EXISTS {};""".format(table_name)
        # Execute the query
        cursor.execute(query)
        logging.info("Table is dropped successfully")

    def read_column_data(self,table_name,column_name):
        # Read one column from table
        logging.info("read one column function")
        cursor = self.connection.cursor()
        query = """SELECT {} FROM {};""".format(column_name,table_name)
        # Execute the query
        cursor.execute(query)

        records = cursor.fetchall()

        data = []
        for i in records:
            data.append(i[0])
        return data

    def read_keywords(self,table_name,intent_name):
        # Read keywords for specific intent
        logging.info("read keywords function")
        cursor = self.connection.cursor()
        query = """SELECT keywords FROM {} WHERE intent_name='{}';""".format(table_name,intent_name)
        
        # Execute the query
        cursor.execute(query)

        records = cursor.fetchall()

        # Convert JSON array to list
        keywords = json.loads(records[0][0])
        return keywords

#dbObj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
#dbObj.insert_data('keywords','test',["11","12"],'lolsss','anushan')
#print(dbObj.read_data('keywords'))
#dbObj.create_table('speech','keywords')
#dbObj.create_table('speech','recharge_issue')
#print(dbObj.read_data('keywords'))
#print(dbObj.read_column_data('service_issue'))
#dbObj.drop_table('keywords')
#print(dbObj.get_table_names())

#print(dbObj.read_column_data('keywords','intent_name'))
#print(dbObj.read_keywords('keywords','mageee'))
