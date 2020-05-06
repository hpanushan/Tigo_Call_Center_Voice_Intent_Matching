from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching
from MySQL_DB.MySQL_Results import MySQL_Results
from Get_File_Names import *
from Move_File import *

def main(file_name):
    print("Running main function.......")
    # Attributes
    current_folder_path = '/opt/voice-clips'
    new_folder_path = '/opt/done'

    file_path = current_folder_path + '/' + file_name

    text = sample_recognize(file_path,file_name)
    print("Text is recieved from API")

    # Getting correct intent from text
    issues = intent_matching(text)
    print("Correct intent for voice clip is received")
    print(issues)

    # Table records
    network_issue = '0'
    recharge_issue = '0'
    service_issue = '0'
    other = '0'

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
    print("Inserting new data into the database....")
    db_obj.insert_data('results',file_name,network_issue,recharge_issue,service_issue,other)

    # Moving the file to done
    move_file(current_folder_path,new_folder_path,file_name)

    return text

    


