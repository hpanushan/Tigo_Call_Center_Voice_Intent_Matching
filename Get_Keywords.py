import logging

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords

def get_keywords():
    logging.info("get keywords function")
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')

    # Getting current intents
    intents = db_obj.get_table_names()

    keywords = {}

    for intent in intents:
        keywords[intent] = db_obj.read_column_data(intent)

    return keywords
