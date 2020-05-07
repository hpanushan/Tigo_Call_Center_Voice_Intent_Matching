from flask import Flask, render_template, url_for, request

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords
from Create_Table_Name import create_table_name
from Get_File_Names import get_file_names

app = Flask(__name__)

@app.route('/')
def main():
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()
    #intent_names = ['add','adada','dadd']
    return render_template('index.html',intents=intent_names)

@app.route('/update')
def update():
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()
    #intent_names = ['add','adada','dadd']
    return render_template('update.html',intents=intent_names)

@app.route('/new')
def new():
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()
    #intent_names = ['add','adada','dadd']
    return render_template('new.html',intents=intent_names)

@app.route('/execute')
def execute():
    # Attributes
    path1 = "/opt/test-voice-clips"
    path2 = "/opt/voice-clips"

    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()
    #intent_names = ['add','adada','dadd']

    test_voice_clips = get_file_names(path1)
    voice_clips = get_file_names(path2)

    return render_template('execute.html',intents=intent_names, test_voice_clips=test_voice_clips, voice_clips=voice_clips)

@app.route('/new_submit', methods=['POST'])
def new_submit():
    intent_name = request.form['intentname']
    keywords = request.form['keywords']

    # Cleaning the keywords text
    keywords = keywords.replace(" ", "")

    # Convert the keywords string into a list of keywords
    keywords = keywords.split(',')
    
    # Creating the table name
    table_name = create_table_name(intent_name)

    # Creating database instance
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')

    # Adding new intent to databse
    db_obj.create_table('speech',table_name)
    db_obj.insert_data(table_name,keywords)

    return render_template('new.html')

@app.route('/update_submit', methods=['POST'])
def update_submit():
    intent_name = request.form['intentname']
    keywords = request.form['keywords']

    # Cleaning the keywords text
    keywords = keywords.replace(" ", "")

    # Convert the keywords string into a list of keywords
    keywords = keywords.split(',')
    
    # Creating the table name
    table_name = create_table_name(intent_name)

    # Creating database instance
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')

    # Drop existing intent table
    db_obj.drop_table(table_name)

    # Updating the intent table by creating a new one
    db_obj.create_table('speech',table_name)
    db_obj.insert_data(table_name,keywords)

    return render_template('update.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
