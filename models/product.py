from databases.db import db
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float, nullable=False)
    profitability = db.Column(db.Float, nullable=False)

    def __init__(self,nombre:str, price:float, calories:int, cost:float, profitability:float ):
        pass


    def calculate_calories():
        pass

    def calculate_cost():
        pass
    
    def calculate_profitability():
        pass
