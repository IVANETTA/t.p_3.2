
from flask import Flask, jsonify, request
from config import Config
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación FLask."""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
   
    @app.route('/')
    def hello_world():
        return 'Bienvenidos!'

    
    #Ejercicio 1.5
    @app.route('/customers/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        data = request.json
        query="DELETE FROM sales.customers WHERE customer_id = %s"
        params= customer_id,
        result= DatabaseConnection.fetch_one(query, params)        
        return jsonify(), 204
        


        
    return app