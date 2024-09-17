class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee) or not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Invalid customer, coffee, or price.")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
