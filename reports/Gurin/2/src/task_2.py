class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def get_info(self):
        return f"ID: {self.id}\nName: {self.name}\nEmail: {self.email}"

    def __str__(self):
        return f"User ID: {self.id}, Name: {self.name}, Email: {self.email}"


class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.blacklist = []

    def add_product(self, product_item, products):
        products.append(product_item)

    def register_sale(self, sale_item, sales):
        sales.append(sale_item)

    def blacklist_customer(self, customer_item):
        if customer_item not in self.blacklist:
            self.blacklist.append(customer_item)

    def __str__(self):
        return f"Admin ID: {self.id}, Name: {self.name}, Email: {self.email}, " f"Blacklist: {len(self.blacklist)}"


class Customer(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.orders = []

    def place_order(self, order_item):
        self.orders.append(order_item)

    def pay_order(self, order_item):
        order_item.status = "Paid"

    def __str__(self):
        return f"Customer ID: {self.id}, Name: {self.name}, Email: {self.email}, " f"Orders: {len(self.orders)}"


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}, " f"Quantity: {self.quantity}"


class Order:
    def __init__(self, order_id, customer, products):
        self.id = order_id
        self.customer = customer
        self.products = products
        self.total_price = sum(p.price for p in products)
        self.status = "Unpaid"

    def pay(self):
        self.status = "Paid"

    def __str__(self):
        products_str = "\n".join([str(p) for p in self.products])
        return (
            f"Order ID: {self.id}, Customer: {self.customer.name}\n"
            f"Products:\n{products_str}\n"
            f"Total Price: {self.total_price}, Status: {self.status}"
        )


class Sale:
    def __init__(self, sale_id, order, date):
        self.id = sale_id
        self.order = order
        self.date = date

    def __str__(self):
        return f"Sale ID: {self.id}, Order ID: {self.order.id}, Date: {self.date}"


if __name__ == "__main__":
    admin = Admin(1, "Admin", "admin@example.com")
    customer_my = Customer(2, "Customer", "customer@example.com")

    product1 = Product(1, "Laptop", 1000.0, 10)
    product2 = Product(2, "Phone", 500.0, 20)

    products_list = []
    admin.add_product(product1, products_list)
    admin.add_product(product2, products_list)

    order_my = Order(1, customer_my, [product1, product2])
    customer_my.place_order(order_my)

    customer_my.pay_order(order_my)

    sale = Sale(1, order_my, "2025-02-22")
    sales_list = []
    admin.register_sale(sale, sales_list)

    admin.blacklist_customer(customer_my)

    print("Admin:", admin)
    print("Customer:", customer_my)
    print("Products List:")
    for product_for in products_list:
        print(product_for)
    print("Customer Orders:")
    for order_item_for in customer_my.orders:
        print(order_item_for)
    print("Sales List:")
    for sale_item_for in sales_list:
        print(sale_item_for)
    print("Admin Blacklist:")
    for customer_item_for in admin.blacklist:
        print(customer_item_for)
