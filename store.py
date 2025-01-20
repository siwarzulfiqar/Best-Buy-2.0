from typing import List, Tuple
import products


class Store:
    def __init__(self, product_list: List[products.Product]):
        self.products = product_list

    def add_product(self, product: products.Product):
        self.products.append(product)

    def remove_product(self, product: products.Product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[products.Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.get_price(quantity)
                product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available for purchase.")
        return total_price
