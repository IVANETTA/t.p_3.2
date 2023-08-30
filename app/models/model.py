# model.py

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, city, state, street, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city
        self.state = state
        self.street = street
        self.zip_code = zip_code

    def serialize(self):
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "city": self.city,
            "state": self.state,
            "street": self.street,
            "zip_code": self.zip_code
        }
