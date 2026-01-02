from peewee import *
from database import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id = IntegerField(unique=True)
    amount = DecimalField(max_digits=10, decimal_places=2)
    category = TextField()
    description = TextField()
    transaction_date = DateField()
    time = DateTimeField(default=datetime.now)