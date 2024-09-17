class Customer:
    _customers = [] 

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = [] 
        Customer._customers.append(self)  

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
      
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
       
        if not isinstance(coffee, Coffee) or not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Invalid coffee or price.")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee.")
        best_customer = None
        max_spent = 0
        for customer in cls._customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                best_customer = customer
        return best_customer
