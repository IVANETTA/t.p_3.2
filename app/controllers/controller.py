# controller.py
from model import Customer

class CustomerController:
    def __init__(self):
        # Simulamos una lista de clientes
        self.customers = [
            Customer(1, "Debra", "Burks", "debra.burks@yahoo.com", "Orchard Park", "NY", "9273 Thorne Ave.", "14127"),
            Customer(2, "Kasha", "Todd", "kasha.todd@yahoo.com", "Campbell", "CA", "910 Vine Street", "95008")
        ]

    def get_customers(self, state=None):
        if state:
            filtered_customers = [customer for customer in self.customers if customer.state == state]
            return filtered_customers
        else:
            return self.customers

    def get_total_customers(self, state=None):
        if state:
            filtered_customers = [customer for customer in self.customers if customer.state == state]
            return len(filtered_customers)
        else:
            return len(self.customers)
