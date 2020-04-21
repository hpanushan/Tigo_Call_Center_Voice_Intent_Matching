from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching
from MySQL_DB.MySQLClient import MySQLClient
from Get_File_Path import *
from Get_File_Name import *
from Move_File import *

def main():
    print("Running main function.......")
    # Attributes
    current_folder_path = 'C:/Users/Anushan Temp/Desktop/New folder (2)/voice-clips'
    new_folder_path = 'C:/Users/Anushan Temp/Desktop/New folder (2)/done'

    try:
        new_file_name = get_file_name(current_folder_path)

        file_path = current_folder_path + '/' + new_file_name

        text = sample_recognize(file_path,new_file_name)
        print("Text is recieved from API")

        # Getting correct intent from text
        issues = intent_matching(text)
        print("Correct intent for voice clip is received")
        print(issues)
        # Creating Database instance
        #dbObj = MySQLClient('146.148.85.146','root','Omnibis.1234','speech')

        # Table records
        rechargeissue = '0'
        networkissue = '0'
        serviceissue = '0'
        other = '0'


        if issues[0] == 'recharge_issue':
            rechargeissue = '1'
        elif issues[0] == 'network_faiulre':
            networkissue = '1'
        elif issues[0] == 'service_failure':
            serviceissue = '1'
        else:
            other = '1'

        # Inserting new data
        print("Inserting new data into the database....")
        #dbObj.insertData('results',get_new_file_name,rechargeissue,networkissue,serviceissue,other)

        # Moving the file to done
        move_file(current_folder_path,new_folder_path,new_file_name)

    except:
        print("No files")
    

if __name__ == "__main__":
    main()

