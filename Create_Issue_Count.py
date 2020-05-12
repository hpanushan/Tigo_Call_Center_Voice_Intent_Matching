import logging

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords

def create_issue_count():
    logging.info("creating issue count fucntion")
    # Keywords
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    issues = db_obj.get_table_names()

    db_obj.close_connection()

    counts = {}
    for i in issues:
        counts[i] = 0

    return counts

