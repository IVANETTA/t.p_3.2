
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
    
    #Ejercicio1
    @app.route('/customers/<int:customer_id>', methods = ['GET'])
    def get_customer(customer_id):
        query="SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s"
        params= customer_id,
        result= DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
                "id":result[0],
                "first_name":result[1],
                "last_name":result[2],
                "email":result[3],
                "phone":result[4],
                "street":result[5],
                "city":result[6],
                "state":result[7],
                "zip_code":result[8]
            }, 200
        return {"msg":"Customer not found"}, 404
    
    #Ejercicio1.2
    @app.route('/customers', methods=['GET'])
    def get_customers():
        query="SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s"
        state = request.args.get('state')

        if state:
            cursor.execute(f"SELECT * FROM sales.customers WHERE state = '{state}'")
        else:
            cursor.execute("SELECT * FROM sales.customers")


        customers = []
        for customer_data in customers_data:
            customer = {
                "city": customer_data.city,
                "customer_id": customer_data.customer_id,
                "email": customer_data.email,
                "first_name": customer_data.first_name,
                "last_name": customer_data.last_name,
                "phone": customer_data.phone,
                "state": customer_data.state,
                "street": customer_data.street,
                "zip_code": customer_data.zip_code
            }
            customers.append(customer)

    response_data = {
        "customers": customers,
        "total": len(customers)
    }

    return jsonify(response_data), 200
    
    #Ejercicio1.4
    @app.route('/customers/<int:customer_id>', methods = ['PUT'])
    def update_customer(customer_id):
        data = request.json  
        
        if "email" in data and "phone" in data:
            query = "UPDATE sales.customers SET email = %s, phone = %s WHERE customer_id = %s"
            params = data["email"], data["phone"], customer_id  
            
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return {"msg": "Customer updated"}, 200
        return {"msg": "Invalid data or Customer not found"}, 400
    
    #Ejercicio 1.5
    @app.route('/customers/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        data = request.json
        query="DELETE FROM sales.customers WHERE customer_id = %s"
        params= customer_id,
        result= DatabaseConnection.fetch_one(query, params)        
        return jsonify(), 204
        


        
    return app