from peewee import *
import os

# For development, using SQLite
DATABASE = os.getenv('Transactions', 'budget.db')

db = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = db