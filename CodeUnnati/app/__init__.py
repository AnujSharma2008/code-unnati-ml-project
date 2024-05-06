from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import routes module to register routes with the app
from app import routes