from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching
from MySQL_DB.MySQLClient import MySQLClient
from Get_File_Path import *

def main():
    print("Running main function.......")
    # Pass the recording to Google speech to text API
    #file_path = 'Data/Dual_Channel/WhatsApp Audio 2020-04-16 at 13.26.55.wav'
    #text = sample_recognize(file_path)
    #file_name = 'Recording (12)'

    #folder_name,file_name = get_file_path()
    folder_name = input("Input issue type here :- ")
    file_name = input("Input file name here :- ")
     
    file_path = "Data/Dual_Channel/{}/{}.wav".format(folder_name,file_name)
    text = sample_recognize(file_path,folder_name,file_name)
    print("Text is recieved from API")

    # Getting correct intent from text
    issues = intent_matching(text)
    print("Correct intent for voice clip is received")

    # Creating Database instance
    dbObj = MySQLClient('146.148.85.146','root','Omnibis.1234','speech')

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
    dbObj.insertData('results',file_name,rechargeissue,networkissue,serviceissue,other)

    

if __name__ == "__main__":
    main()

