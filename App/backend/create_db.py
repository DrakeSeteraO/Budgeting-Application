from database import db
from model import Transaction

def create_tables():
    """Create all tables in the database"""
    with db:
        db.create_tables([Transaction])
    print("Database tables created successfully!")

def drop_tables():
    """Drop all tables (use with caution!)"""
    with db:
        db.drop_tables([Transaction])
    print("Database tables dropped!")

if __name__ == '__main__':
    create_tables()