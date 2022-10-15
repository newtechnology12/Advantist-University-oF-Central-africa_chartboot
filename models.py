from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from uuid import uuid4
from flask_migrate import upgrade


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# FLASK_APP=microblog.py




class User(db.Model):
    '''
    Table user
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(106), nullable=False, unique=False)
    is_active = db.Column(db.Boolean)
    token = db.Column(db.String(32), nullable=False, unique=False)

    def __init__(self):
        self.is_active = False
        self.token = str(uuid4()).replace('-', '')

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    manager.run()
