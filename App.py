from flask import Flask, request
from flask_restful import Resource, Api
import json

from MySQL_DB.MySQL_Intents_Keywords import *

app = Flask(__name__)
api = Api(app)

class Intent(Resource):
    def get(self):
        # Get the current intent names
        # Instantiate DB access object
        db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
        intents = db_obj.get_column_names('keywords')
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

        # Remove existing keywords for given intent
        db_obj.drop_column('keywords',intent_name)

        # Adding a new column
        db_obj.add_new_coulumn('keywords',intent_name)

        # Adding new keywords
        db_obj.insert_data('keywords',intent_name,keywords)

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

        # Create a new column
        db_obj.add_new_coulumn('keywords',intent_name)

        # Add keywords
        db_obj.insert_data('keywords',intent_name,keywords)

        return 1, 201


# Routes
api.add_resource(Intent,'/intent')
api.add_resource(Update,'/update')
api.add_resource(New,'/new')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)