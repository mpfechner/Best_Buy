from products import Product
from store import Store


def start(store: Store):
    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def list_products(store: Store):
    print("\nAvailable products:")
    for p in store.get_all_products():
        print(p.show())

def show_total_quantity(store: Store):
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")

def make_order(store: Store):
    shopping_list = []
    products = store.get_all_products()

    print("\nEnter the number of the product and quantity to order.")
    for i, p in enumerate(products):
        print(f"{i + 1}. {p.show()}")

    while True:
        try:
            prod_input = input("Product number (or press Enter to finish): ").strip()
            if not prod_input:
                break
            index = int(prod_input) - 1
            if index < 0 or index >= len(products):
                print("Invalid product number.")
                continue
            quantity = int(input("Quantity: "))
            shopping_list.append((products[index], quantity))
        except Exception as e:
            print(f"Invalid input: {e}")

    try:
        total_price = store.order(shopping_list)
        print(f"\nOrder placed. Total cost: {total_price} dollars.")
    except Exception as e:
        print(f"Error placing order: {e}")



def main():
    product_list = [
        Product("MacBook Air M2", 1450, 100),
        Product("Bose QuietComfort Earbuds", 250, 500),
        Product("Google Pixel 7", 500, 250),
    ]
    store = Store(product_list)
    start(store)


if __name__ == "__main__":
    main()

