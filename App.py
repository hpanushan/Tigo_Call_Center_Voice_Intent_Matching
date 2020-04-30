from flask import Flask, request
from flask_restful import Resource, Api
import json

from MySQL_DB.MySQL_Intents_Keywords import *

app = Flask(__name__)
api = Api(app)

class Intent(Resource):
    def get(self):
        # Get the current intents
        db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
        intents = db_obj.get_column_names('keywords')
        return {"keywords":intents}, 200

    def post(self):
        # Getting Post data
        post_json = request.get_json()

        # Convert JSON into Dictionary
        post_dict = json.loads(post_json)

        # Key values of post data
        user_input = post_dict['user_input']
        options = post_dict['options']

        return 1, 201

# Routes
api.add_resource(Intent,'/intent')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5000',debug=True)