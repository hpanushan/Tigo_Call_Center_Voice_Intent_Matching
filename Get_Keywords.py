import logging

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords

def get_keywords():
    logging.info("get keywords function")
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')

    # Getting current intents
    intents = db_obj.read_column_data('keywords','intent_name')

    keywords = {}

    for intent in intents:
        keywords[intent] = db_obj.read_keywords('keywords',intent)
    db_obj.close_connection()
    
    return keywords
