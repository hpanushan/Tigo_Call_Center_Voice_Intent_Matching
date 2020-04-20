import mysql.connector

class MySQLClient:

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

    def converByteStringToString(self,byteString):
        return byteString.decode("utf-8")

    # Queries for databases
    def showDatabases(self):
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("SHOW DATABASES;")
        return cursor.fetchall()

    def useDatabase(self,dbName):
        # Enter to database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("USE {};".format(dbName))
        print('Database entering is successful')

    def showTables(self,dbName):
        # Show tabales inside the database
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('USE {};'.format(dbName))
        cursor.execute('SHOW TABLES;')
        return cursor.fetchall()

    def readDataFromTable(self,dbName,tableName):
        # Read data from a table
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute('SELECT * FROM {}.{};'.format(dbName,tableName))
        return cursor.fetchall()

    def createTable(self,dbName,tableName):
        # Creating a new table
        cursor = self.connection.cursor()
        # Execute the query
        cursor.execute("""CREATE TABLE {}.{} (
                        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        filename VARCHAR(30) NOT NULL,
                        rechargeissue BINARY NOT NULL,
                        networkissue BINARY NOT NULL,
                        serviceissue BINARY NOT NULL,
                        other BINARY NOT NULL);""".format(dbName,tableName))
        print('{} Table creating is successful'.format(tableName))

    def insertData(self,tableName,filename,rechargeissue,networkissue,serviceissue,other):
        # Entering data to the table
        cursor = self.connection.cursor()
        # Execute the query
        query = """INSERT INTO `{}` (filename,rechargeissue,networkissue,serviceissue,other) VALUES (%s,%s,%s,%s,%s)""".format(tableName)
        val = (filename,rechargeissue,networkissue,serviceissue,other)

        self.connection.commit()
        cursor.execute(query,val)
        print("Record is entered successfully")

#dbObj = MySQLClient('146.148.85.146','root','Omnibis.1234','speech')
#dbObj.createTable('speech','results')
#dbObj.insertData("results","test3","1","0","0","0")

#print(dbObj.readDataFromTable('anushan','uploaded_contents')[-1])

