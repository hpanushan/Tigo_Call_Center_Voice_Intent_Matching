from flask import Flask, request
from flask_restful import Resource, Api
import json

from MySQL_DB.MySQL_Intents_Keywords import *
from Get_File_Names import get_file_names

app = Flask(__name__)
api = Api(app)

class Intents(Resource):
    def get(self):
        # Get the current intent names
        # Instantiate DB access object
        db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
        intents = db_obj.get_table_names()
        return {"keywords":intents}, 200


class Update(Resource):
    def post(self):
        # Getting Post data
        post_json = request.get_json()

        # Convert JSON into Dictionary
        post_dict = json.loads(post_json)

        # Key values of post data
        intent_name = post_dict['intent_name']
        keywords = post_dict['keywords']

        # Instantiate DB access object
        db_obj = MySQL_Intents_Keywords('146.148.85.146', 'root', 'Omnibis.1234', 'speech')

        # Remove existing keywords table for given intent
        db_obj.drop_table(intent_name)

        # Create a new table for the intent
        db_obj.create_table('speech',intent_name)

        # Adding new keywords
        db_obj.insert_data(intent_name,keywords)

        return 1, 201

class New(Resource):
    def post(self):
        # Getting Post data
        post_json = request.get_json()

        # Convert JSON into Dictionary
        post_dict = json.loads(post_json)

        # Key values of post data
        intent_name = post_dict['intent_name']
        keywords = post_dict['keywords']

        # Instantiate DB access object
        db_obj = MySQL_Intents_Keywords('146.148.85.146', 'root', 'Omnibis.1234', 'speech')

        # Create a new table for new intent
        db_obj.create_table('speech',intent_name)

        # Add keywords
        db_obj.insert_data(intent_name,keywords)

        return 1, 201

class Execute(Resource):
    def get(self):
        # Get the file names in test_voice_clips and voice_clips folder
        # Check the files inside the test-voice-clips folder
        path1 = "/opt/test-voice-clips"
        files_in_test_voice_clips = get_file_names(path1)

        # Check the files inside the voice-clips folder
        path2 = "/opt/voice-clips"
        files_in_voice_clips = get_file_names(path2)

        return {"test-voice-clips": files_in_test_voice_clips, "voice-clips": files_in_voice_clips}, 200


# Routes
api.add_resource(Intents,'/intents')
api.add_resource(Update,'/update')
api.add_resource(New,'/new')
api.add_resource(Execute,'/execute')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)