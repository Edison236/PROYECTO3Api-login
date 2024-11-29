from flask import Blueprint, render_template, request, jsonify
from models.ingredient import Ingredient
from shared.shared_functions import json_response, is_integer
from databases.db import db

ingredient_bp = Blueprint('ingredients', __name__, url_prefix= '/ingredient')

@ingredient_bp.route('/get_ingredients', methods = ['GET'])
def get_ingredients():
    list_ingredients = Ingredient.query.all()
    response = [{
        'id': ingredient.id,
        'name': ingredient.name,
        'price': ingredient.price,
        'calories': ingredient.calories,
        'inventory_counter': ingredient.inventory_counter,
        'is_vegetarian': ingredient.es_vegetarian,
        'is_healthy': ingredient.es_healthy
    } for ingredient in list_ingredients]
    return json_response(response, "success", None)

@ingredient_bp.route('/get_ingredients/value', methods = ['GET'])
def get_ingredient(value):
    try:
        if is_integer(value, int):
            ingredient = Ingredient.query.filter(Ingredient.id == value).first
        else:
            ingredient = Ingredient.query.filter(Ingredient.name == value).first
        if ingredient != None:
            response = [{
                'id': ingredient.id,
                'name': ingredient.name,
                'price': ingredient.price,
                'calories': ingredient.calories,
                'inventory_counter': ingredient.inventory_counter,
                'is_vegetarian': ingredient.es_vegetarian,
                'is_healthy': ingredient.es_healthy
            }]
            return json_response(response, "success", None)
        else:
            return json_response(None, "error", f"No se encuentra el ingrediente" )
            
    except Exception as e:
        return json_response(None, "error", f"Se produjo un error inesperado: {e}")
    
@ingredient_bp.route('/get_ingredients/healthy/<int:id>', methods = ['GET'])
def get_ingredient_healthy(id):
    try:
        ingredient = Ingredient.query.filter(Ingredient.id == id).first
        if ingredient != None:
            response = [{
                'is_healthy': ingredient.es_healthy
            }]
            return json_response(response, "success", None)
        else:
            return json_response(None, "error", f"No se encuentra el ingrediente con el id: {id}")
            
    except Exception as e:
        return json_response(None, "error", f"Se produjo un error inesperado: {e}")

