import logging

def create_table_name(text):
    # Lowercasing and splitting the text
    logging.info('creating table name function')
    text = text.lower()

    text = text.split()
    table_name = text[0]
    for i in text[1:]:
        table_name = table_name + "_" + i

    logging.info("table name - " + table_name)
    return table_name



