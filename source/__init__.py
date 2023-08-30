from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#https://discuss.codecademy.com/t/cannot-import-name-from-partially-initialized-module-most-likely-due-to-a-circular-import/530383

app = Flask(__name__)

app.config["DEBUG"] = True

#key_id = os.environ["AWS_ACCESS_KEY_ID"]
#access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
name = os.environ["AWS_NAME_TABLE"]
aws_region = os.environ["AWS_DEFAULT_REGION"]

from source.auth import register

#db.app = app
#db.init_app(app)

app.register_blueprint(register)




        
