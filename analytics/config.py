import logging
import os
import base64

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_username = os.environ["DB_USERNAME"]

# Get the base64 encoded password from the environment variable
encoded_password = os.environ["DB_PASSWORD"]

# Add padding characters if necessary
# padding_length = 4 - (len(encoded_password) % 4)
# encoded_password += "=" * padding_length

# Decode the password from base64 to bytes
decoded_bytes = base64.b64decode(encoded_password)

# Convert the bytes to a string
cleartext_password = decoded_bytes.decode("utf-8")

# Store the decoded password as db_password
db_password = cleartext_password

db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "postgres")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)
