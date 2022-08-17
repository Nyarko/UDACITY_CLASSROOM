from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:66Oh!6My!6@localhost:5432/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World! Again!"