from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self._products = products

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self._products)

    def get_all_products(self) -> List[Product]:
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
