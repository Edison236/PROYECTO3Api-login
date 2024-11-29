from databases.db import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False) 
    calories = db.Column(db.Integer, nullable=False)
    inventory_counter = db.Column(db.Integer, nullable=False)
    is_vegetarian = db.Column(db.Boolean, default=False)
    is_healthy = db.Column(db.Boolean, default=False)

def  replenish_ingredient():
    pass