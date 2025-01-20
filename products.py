class Product:
    def __init__(self, name, price, quantity, promotion=None):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for name, price, or quantity.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if self.quantity > 0 else False
        self.promotion = promotion

    def set_promotion(self, promotion):
        """Sets a promotion for the product."""
        self.promotion = promotion

    def get_price(self, quantity):
        """Returns the price of the product, applying promotion if available."""
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        if self.promotion:
            return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"
        return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot purchase a negative quantity.")
        if quantity > self.quantity:
            raise Exception("Not enough stock to complete the purchase.")
        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, quantity=0, promotion=promotion)
        self.active = True

    def show(self):
        return f"{self.name} - Price: ${self.price} (Non-stocked), Promotion: {self.promotion.name if self.promotion else 'None'}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum, promotion=None):
        super().__init__(name, price, quantity, promotion)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot purchase more than {self.maximum} of this product at a time.")
        return super().buy(quantity)

    def show(self):
        return f"{self.name} - Price: ${self.price}, Max purchase: {self.maximum}, Promotion: {self.promotion.name if self.promotion else 'None'}"
