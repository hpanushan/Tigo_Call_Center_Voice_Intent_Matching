from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching
from MySQL_DB.MySQLClient import MySQLClient

def main():
    
    # Pass the recording to Google speech to text API
    #file_path = 'Data/Dual_Channel/WhatsApp Audio 2020-04-16 at 13.26.55.wav'
    #text = sample_recognize(file_path)
    file_name = 'Recording (12)'

    file_path = "Data/Dual_Channel/Service_Failure/{}.wav".format(file_name)
    text = sample_recognize(file_path)
    
    # Getting correct intent from text
    issues = intent_matching(text)

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
    dbObj.insertData('results',file_name,rechargeissue,networkissue,serviceissue,other)

    

if __name__ == "__main__":
    main()

