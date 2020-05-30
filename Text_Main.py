import logging
from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize

from Intent_Matching import intent_matching
from MySQL_DB.MySQL_Results import MySQL_Results
from File_Handling.Move_File import move_file
from File_Handling.TXT_File_Read import txt_file_read

def text_main(file_name):
    logging.info("main function")
    # Attributes
    current_folder_path = '/opt/text-files'
    new_folder_path = '/opt/done'
    logging.info("current folder path - " + current_folder_path)
    logging.info("new folder path - " + new_folder_path)

    file_path = current_folder_path + '/' + file_name
    
    text = txt_file_read(file_path)

    logging.info("text is received from text file")

    # Getting correct intent from text
    issues = intent_matching(text)
    logging.info("intents are received for clip")
    logging.info("matched intent - " + issues[0])

    # Table records
    network_issue = '0'
    recharge_issue = '0'
    service_issue = '0'
    other = '0'

    logging.info("preparing row data in binary table")
    if issues[0] == 'network_issue':
        network_issue = '1'
    elif issues[0] == 'recharge_issue':
        recharge_issue = '1'
    elif issues[0] == 'service_issue':
        service_issue = '1'
    else:
        other = '1'

    # Creating Database instance
    db_obj = MySQL_Results('146.148.85.146', 'root', 'Omnibis.1234', 'speech')
    # Inserting new data
    db_obj.insert_data('results',file_name,network_issue,recharge_issue,service_issue,other)

    db_obj.close_connection()

    # Moving the file to done
    move_file(current_folder_path,new_folder_path,file_name)
        

    
    

    

    


