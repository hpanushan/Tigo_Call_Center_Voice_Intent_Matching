
def create_table_name(text):
    # Lowercasing and splitting the text
    text = text.lower()

    text = text.split()
    table_name = text[0]
    for i in text[1:]:
        table_name = table_name + "_" + i

    return table_name



