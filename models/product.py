from databases.db import db
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    profitability = db.Column(db.Float, nullable=False)

    def __init__(self,name:str, price:float, calories:int, profitability:float ):
        pass


    def calculate_calories():
        pass

    def calculate_cost():
        pass
    
    def calculate_profitability():
        pass

    def insert_data_products_default():
        if not Product.query.first():
            product = [
                Product(name= 'Helado de Vainilla', price = '3000', calories = '210', profitability = '275.0')
                # Product(name = 'Helado de Chocolate', price='3500', calories='204',profitability='250.0'),
                # Product(name = 'Helado de Fresa', price='3200', calories='150',profitability='255.6'),
                # Product(name = 'Dulce de Leche', price='3800', calories='300',profitability='216.7'),
                # Product(name = 'Helado de Oreo', price='4000', calories='250',profitability='263.6'),
                # Product(name = 'Gelato de Pistacho', price='4500', calories='220',profitability='200.0'),
                # Product(name = 'Banano Split', price='5000', calories='350',profitability='150.0'),
                # Product(name = 'Paleta de Fruta', price='2500', calories='100',profitability='525.0'),
                # Product(name = 'Vaso de Helado de Fresa y Oreo', price='1000', calories='280',profitability='177.8'),
                # Product(name = 'Vaso con tres sabores', price='1200', calories='230',profitability='187.8')
                ]
            db.session.bulk_save_objects(product)  # Inserta múltiples registros
            db.session.commit()            
