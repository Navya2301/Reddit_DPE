# we need to install config parser

import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf')) # join the path of current file with /config/config.conf

SECRET = parser.get('api_keys','reddit_secret_key')
CLIENT_ID = parser.get('api_keys','reddit_client_id')


DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_user')
DATABASE_PASSWORD = parser.get('database', 'database_password')


INPUT_PATH = parser.get('file_paths','input_path')
OUTPUT_PATH = parser.get('file_paths','output_path')



AWS_ACCESS_KEY_ID = parser.get('aws','aws_access_key_id')
AWS_SECRET_ACCESS_KEY = parser.get('aws','aws_secret_access_key')
AWS_SESSION_TOKEN = parser.get('aws','aws_session_token')
AWS_REGION = parser.get('aws','aws_region')
AWS_BUCKET_NAME = parser.get('aws','aws_bucket_name')



BATCH_SIZE = parser.get('etl_settings', 'batch_size')
ERROR_HANDLING 
LOG_LEVEL 