from flask import Flask
from flask_restplus import Api, Resource, fields, abort
import os
import werkzeug
import logging
import json

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords
from File_Handling.CSV_File_Read import csv_file_read
from File_Handling.Get_File_Names import get_file_names
from File_Handling.Move_File import move_file
from Voice_Main import voice_main
from Text_Main import text_main

logger = logging.getLogger(__name__)
# Logging format
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s %(lineno)d %(message)s')

app = Flask(__name__)
api = Api(app)

# Models
new_intent = api.model('new_intent', {'intent_name': fields.String(),'keywords': fields.List(fields.String()), 'created_by': fields.String(), 'description': fields.String()}) 
update_intent = api.model('update_intent', {'intent_name': fields.String(),'keywords': fields.List(fields.String()), 'created_by': fields.String(), 'description': fields.String()})       
#new_intent_file = api.model('new_intent_file', {'intent_name': fields.String(),'created_by': fields.String(), 'description': fields.String()})

# Data parsers
csv_file_upload = api.parser()
csv_file_upload.add_argument('intent_name', type=str, required=True)
csv_file_upload.add_argument('created_by', type=str, required=True)
csv_file_upload.add_argument('description', type=str, required=True)
csv_file_upload.add_argument('csv_file', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='CSV file')

test_file_upload = api.parser()
test_file_upload.add_argument('test_file_upload', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='Text/Wav file')

file_analyse = api.parser()
file_analyse.add_argument('file_name', type=str, required=True)

name_space = api.namespace('', description='Voice Intent Matching')

#######################
# Intent Managemet page
@api.route('/intent')
class Intent(Resource):       # Class inheritance from Resource (Inject all RestPLUS features to this class)
    @api.doc(responses={ 200: 'OK', 500: 'Internal Server Error' })
    def get(self):
        try:
            # Instantiate DB instance
            db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
            records = db_obj.read_data('keywords')
            db_obj.close_connection()
            return records, 200    # No need to jsonify here

        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
    
    @api.doc(responses={ 201: 'OK', 500: 'Internal Server Error' })  
    @api.expect(new_intent)
    def post(self):
        try:
            data = api.payload          # Get data sent through POST (Dictionary data type)
    
            # Values
            intent_name = data['intent_name']
            keywords = data['keywords']
            created_by = data['created_by']
            description = data['description']
        
            # Instantiate DB instance
            db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
            db_obj.insert_data('keywords',intent_name,keywords,description,created_by)
            db_obj.close_connection()

            return {'result' : 'Intent added'}, 201
        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")

# For update and delete intent
@api.route('/intent/<int:intent_id>')
class UpdateAndDelete(Resource):        
    # Class inheritance from Resource (Inject all RestPLUS features to this class)
    @api.doc(responses={ 201: 'OK', 500: 'Internal Server Error' })  
    @api.expect(update_intent)
    def put(self, intent_id):
        try:
            # Get data sent through POST (Dictionary data type)
            data = api.payload   

            # Values
            intent_name = data['intent_name']
            keywords = data['keywords']
            created_by = data['created_by']
            description = data['description']

            # Instantiate DB instance
            db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
            # Update row
            db_obj.update_row('keywords',intent_id,intent_name,keywords,description,created_by)
            db_obj.close_connection()

            return {'result' : 'Intent updated'}

        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not update information", statusCode = "500")

    @api.doc(responses={ 200: 'OK', 500: 'Internal Server Error' })  
    def delete(self, intent_id):
        try:
            # Instantiate DB instance
            db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
            # Remove current row
            db_obj.remove_row('keywords',intent_id)
            db_obj.close_connection()

            return {'result' : 'Intent removed'}
        
        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not delete information", statusCode = "500")

# File upload with keywords
@api.route('/intent/upload')
class Upload(Resource): 
    @api.doc(responses={ 201: 'OK', 500: 'Internal Server Error' })  
    @api.expect(csv_file_upload)
    def post(self):
        try:
            # File upload and read
            args = csv_file_upload.parse_args()
        
            # Values
            intent_name = args['intent_name']
            created_by = args['created_by']
            description = args['description']

            if args['csv_file'].mimetype == 'application/vnd.ms-excel':
            
                #destination = os.path.join(app.config.get('DATA_FOLDER'), 'medias/')
                destination = "/opt/upload-keywords/"
                if not os.path.exists(destination):
                    os.makedirs(destination)
                csv_file = '%s%s' % (destination, 'keywords.csv')
                args['csv_file'].save(csv_file)
        
            # Attributes
            file_location = '/opt/upload-keywords/keywords.csv'
            keywords = csv_file_read(file_location)

            # Instantiate DB instance and add new record
            db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
            db_obj.insert_data('keywords',intent_name,keywords,description,created_by)
            db_obj.close_connection()
            
            return {'status': 'Done'}, 201

        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")

###############
# Analysis page

@api.route('/files/<string:file_type>')
class files(Resource):       # Class inheritance from Resource (Inject all RestPLUS features to this class)
    @api.doc(responses={ 200: 'OK', 500: 'Internal Server Error' })  
    def get(self, file_type):
        try:
            if file_type == "text":
                file_path = '/opt/test-text-files/'
                text_file_names = get_file_names(file_path)
                return text_file_names, 200
            else:  
                file_path = '/opt/test-voice-clips/'
                voice_clip_names = get_file_names(file_path)
                return voice_clip_names, 200    # No need to jsonify here

        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not get information", statusCode = "500")

    @api.doc(responses={ 201: 'OK', 500: 'Internal Server Error' })  
    @api.expect(test_file_upload)
    def post(self, file_type):
        try:
            #args = parsers.file_upload.parse_args()
            args = test_file_upload.parse_args()

            if file_type=='text':
                destination = "/opt/text-files/"
                if not os.path.exists(destination):
                    os.makedirs(destination)
                text_file = '%s%s' % (destination, 'test.txt')
                args['test_file_upload'].save(text_file)

                # Apply analysis
                file_name = 'test.txt'
                text_main(file_name)

                return {'Result': 'Done'}, 201
            
            elif file_type=='voice':
                destination = "/opt/voice-clips/"
                if not os.path.exists(destination):
                    os.makedirs(destination)
                wav_file = '%s%s' % (destination, 'test.wav')
                args['test_file_upload'].save(wav_file)

                # Apply analysis
                file_name = 'test.wav'
                status = voice_main(file_name)
            
                return status, 201
            else:
                return {'Error': '!!'}, 500
            
        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not analyse information", statusCode = "500")

@api.route('/analyse/<string:file_type>')
class Analyse(Resource):       # Class inheritance from Resource (Inject all RestPLUS features to this class)
    @api.doc(responses={ 201: 'OK', 500: 'Internal Server Error' })  
    @api.expect(file_analyse)
    def post(self, file_type):
        try:    
            args = file_analyse.parse_args()
            file_name = args['file_name']

            if file_type=='text':
                # Move file
                current_path = '/opt/test-text-files'
                new_path = '/opt/text-files'
                move_file(current_path,new_path,file_name)

                # Analyse text file
                text_main(file_name)

                return {'Result': 'Done'}, 201
            
            elif file_type=='voice':
                # Move file
                current_path = '/opt/test-voice-clips'
                new_path = '/opt/voice-clips'
                move_file(current_path,new_path,file_name)

                # Analyse text file
                status = voice_main(file_name)
            
                return status, 201
            else:
                return {'Error': '!!'}, 500

        except Exception as e:
            name_space.abort(500, e.__doc__, status = "Could not analyse information", statusCode = "500")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
