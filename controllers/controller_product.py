from flask import Blueprint, render_template, request, jsonify
from shared.shared_functions import json_response, is_integer
from models.product import Product
from databases.db import db

product_bp = Blueprint('product', __name__, url_prefix = '/product')

@product_bp.route('/get_products', methods=['GET'])
def get_product():
    list_produts = Product.query.all()
    response = [{
        'id': product.id, 
        'name': product.name, 
        'price': product.price, 
        'calories': product.calories,
        'profitability': product.profitability 
    } for product in list_produts]
    return json_response(response, "success", None)
    

@product_bp.route('/get_product/<value>', methods = ['GET'])
def get_product_id(value):
    if is_integer(value):
        show_product = Product.query.filter(Product.id == value).all()
    else:
        show_product = Product.query.filter(Product.name == value).all()
    response = [{
        'id': product.id, 
        'name': product.name, 
        'price': product.price, 
        'calories': product.calories, 
        'cost': product.cost, 
        'profitability': product.profitability   
    } for product in show_product]
    return json_response(response, "success", None)

@product_bp.route('/get_product/calories/<int:id>', methods = ['GET'])
def get_product_calories(id):
    try:
        show_product = Product.query.filter(Product.id == id).first()
        if show_product != None:
            print(show_product)
            response = {'calories': show_product.calories }
            return json_response(response, "success", None)
        else:           
            return json_response(None , "error", f"No se encuentra el producto con id: {id}" )
            
    except Exception as e:
        return json_response(None, "error", f"Se produjo un error inesperado: {e}") 

@product_bp.route('/get_product/profitability/<int:id>', methods = ['GET'])
def get_product_profitability(id):
    try:
        show_product = Product.query.filter(Product.id == id).first()
        if show_product != None:
            response = {'profitability': show_product.profitability }
            return json_response(response, "success", None)
        else:            
            return json_response(None, "error", f"No se encuentra el producto con id: {id}") 
            
    except Exception as e:        
        return json_response(None, "error", f"Se produjo un error inesperado: {e}") 

@product_bp.route('/get_product/cost/<int:id>', methods = ['GET'])
def get_product_cost(id):
    try:
        show_product = Product.query.filter(Product.id == id).first()
        if show_product != None:
            response = {'cost': show_product.cost }
            return json_response(response, "success", None)
        else:            
            return json_response(None, "error", f"No se encuentra el producto con id: {id}" ) 
            
    except Exception as e:        
        return json_response(None, "error", f"Se produjo un error inesperado: {e}")