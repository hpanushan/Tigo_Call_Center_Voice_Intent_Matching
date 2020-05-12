import logging
from flask import Flask, render_template, url_for, request

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords
from Create_Table_Name import create_table_name
from Get_File_Names import get_file_names
from Move_File import move_file
from Main import main

logger = logging.getLogger(__name__)
# Logging format
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s %(lineno)d %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    logger.info('main route')
    # Attributes
    old_path = "/opt/voice-clips"
    new_path = "/opt/test-voice-clips"

    # Clear voice-clips folder
    file_names_in_voice_clips = get_file_names(old_path)
    for file in file_names_in_voice_clips:
        move_file(old_path,new_path,file)

    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    #intent_names = ['add','adada','dadd']
    return render_template('index.html',intents=intent_names)

@app.route('/update')
def update():
    logger.info('updating intent route')
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    #intent_names = ['add','adada','dadd']
    return render_template('update.html',intents=intent_names)

@app.route('/new')
def new():
    logger.info('creating new intent route')
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    #intent_names = ['add','adada','dadd']
    return render_template('new.html',intents=intent_names)

@app.route('/execute')
def execute():
    logger.info('executing route')
    # Attributes
    path1 = "/opt/test-voice-clips"
    path2 = "/opt/voice-clips"

    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    #intent_names = ['add','adada','dadd']

    test_voice_clips = get_file_names(path1)
    voice_clips = get_file_names(path2)

    return render_template('execute.html',intents=intent_names, test_voice_clips=test_voice_clips, voice_clips=voice_clips)

@app.route('/new_submit', methods=['POST'])
def new_submit():
    logger.info('new submit route')
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

    # Getting current stored intents
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    return render_template('submitted_intent.html',intents=intent_names)

@app.route('/update_submit', methods=['POST'])
def update_submit():
    logger.info('update submit route')
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

    # Getting current stored intents
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    return render_template('submitted_intent.html',intents=intent_names)

@app.route('/execute_submit', methods=['POST'])
def execute_submit():
    logger.info('execute submit route')
    # Attributes
    old_path = "/opt/test-voice-clips"
    new_path = "/opt/voice-clips"

    # Getting selected file name
    file_name = request.form['duallistbox_demo1[]']
    
    # Move the selected file to voice clips folder
    move_file(old_path,new_path,file_name)

    # Running main application to process 
    main(file_name)

    # Getting current stored intents
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    intent_names = db_obj.get_table_names()

    db_obj.close_connection()

    return render_template('executed.html',intents=intent_names)


if __name__ == '__main__':
    # Attributes
    app.run(host="0.0.0.0",port="5000",debug=True)
    
