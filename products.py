class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product parameters.")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def show(self) -> str:
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        if not self._active:
            raise Exception("Product is not active.")
        if quantity > self._quantity:
            raise Exception("Not enough stock.")
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        return self._price * quantity

