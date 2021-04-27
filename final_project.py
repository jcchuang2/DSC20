"""
DSC 20 Final Project
Name: Joshua Chuang
PID:  A16233072
"""
from util import Stack, Queue
from datetime import datetime


def doctest():
    """
    ------------------------ PRODUCT TEST ------------------------

    >>> p1 = Product("iphone",399)
    >>> p2 = Special_Product("macbook air",999)
    >>> p3 = Limited_Product("free iphone", 0, 10)
    >>> p1, p2, p3
    (PRODUCT <0>, PRODUCT <1>, PRODUCT <2>)
    >>> print(p1)
    <0> iphone - 399$
    >>> print(p2)
    <1> macbook air - 999$ (special)
    >>> print(p3)
    <2> free iphone - 0$ (10 left)

    ------------------------ WAREHOUSE TEST ------------------------

    >>> wh = Warehouse()
    >>> st = Store(wh)
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> print(wh)
    Warehouse with 3 products
    >>> print(wh.get_product(1))
    <1> macbook air - 999$ (special)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <0> iphone - 399$
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (10 left)
    ============================
    >>> wh.export_product(3)
    >>> wh.export_product(2)
    PRODUCT <2>
    >>> wh.remove_product(0)
    True
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (9 left)
    ============================
    >>> st.view_products(sort = True)
    ============================
    <ID> Product - Price
    <2> free iphone - 0$ (9 left)
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.remove_product(0)
    False
    >>> [wh.export_product(2) for i in range(9)]
    [PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>,\
 PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>]
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.show_log()
    Product <0> imported - 2020-11-26 07:09:17.709522
    Product <1> imported - 2020-11-26 07:09:17.709584
    Product <2> imported - 2020-11-26 07:09:17.709612
    Product <2> exported - 2020-11-26 07:09:17.709745
    Product <0> removed  - 2020-11-26 07:09:17.709776
    Product <2> exported - 2020-11-26 07:09:17.709886
    Product <2> exported - 2020-11-26 07:09:17.709893
    Product <2> exported - 2020-11-26 07:09:17.709897
    Product <2> exported - 2020-11-26 07:09:17.709901
    Product <2> exported - 2020-11-26 07:09:17.709905
    Product <2> exported - 2020-11-26 07:09:17.709909
    Product <2> exported - 2020-11-26 07:09:17.709913
    Product <2> exported - 2020-11-26 07:09:17.709916
    Product <2> exported - 2020-11-26 07:09:17.709920
    Product <2> removed  - 2020-11-26 07:09:17.709924

    ------------------------ USER TEST ------------------------

    >>> u1 = User( 'Jerry', st)
    >>> u2 = Premium_User( 'FYX', st)
    >>> u1
    USER<0>
    >>> u2
    USER<1>
    >>> print(u1)
    standard user: Jerry - 0$
    >>> u2.add_balance(2000)
    >>> print(u2)
    premium user: FYX - 2000$

    >>> wh.import_product(p1)
    >>> u1 = User("A",st)
    >>> u1.add_cart(0)
    >>> u1.add_cart(0)
    >>> u1.view_cart()
    (front) <0> iphone - 399$ -- <0> iphone - 399$ (rear)
    >>> u1.checkout()
    STORE: Not enough money QQ
    []
    >>> u1.add_balance(1000)
    >>> u1.checkout()
    STORE: A ordered iphone. A has 562$ left.
    STORE: A ordered iphone. A has 124$ left.
    [PRODUCT <0>, PRODUCT <0>]
    >>> p4 = Limited_Product("Ipad", 600, 5)
    >>> wh.import_product(p4)
    >>> u2.buy_all(3)
    STORE: FYX ordered Ipad. FYX has 1400$ left.
    STORE: FYX ordered Ipad. FYX has 800$ left.
    STORE: FYX ordered Ipad. FYX has 200$ left.
    STORE: Not enough money QQ
    [PRODUCT <3>, PRODUCT <3>, PRODUCT <3>]

    ------------------- HISTORY / UNDO TEST -------------------

    >>> u1.view_history()
    (bottom) <0> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903632 -- \
<1> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903658 (top)
    >>> u1.undo_purchase()
    STORE: A refunded iphone. A has 523$ left.

    -------------------------- EC TEST ------------------------
    >>> p1 = Product("A",20)
    >>> p2 = Special_Product("B",7)
    >>> p3 = Limited_Product("C", 1, 2)
    >>> wh = Warehouse()
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> st = Store(wh)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <4> A - 20$
    <5> B - 7$ (special)
    <6> C - 1$ (2 left)
    ============================
    >>> st.so_rich(45)
    1
    >>> st.so_rich(61)
    0
    >>> st.so_rich_recursive(45)
    1
    >>> st.so_rich_recursive(61)
    0
    """
    pass


#######################################################################
#                               PRODUCT                               #
#######################################################################
class Product:
    """ A class that creates a product instance """

    ##### Part 1.1 #####
    product_counter = 0

    def __init__(self, name, price):
        """ A constructor that builds the product instance """
        # YOUR CODE GOES HERE #
        self.name = name
        self.price = price
        self.id = Product.product_counter
        Product.product_counter += 1

    def __str__(self):
        """ Returns string representation of instance """
        # YOUR CODE GOES HERE #
        return "<{}> {} - {}$".format(self.id, self.name, self.price)

    def __repr__(self):
        """ Returns object representation of instance """
        # YOUR CODE GOES HERE #
        return "PRODUCT <{}>".format(self.id)


class Limited_Product(Product):
    """ A class of product with limited offerings """

    ##### Part 1.2 #####
    def __init__(self, name, price, amount):
        """ A constructor that builds the limited product instance """
        # YOUR CODE GOES HERE #
        super().__init__(name, price)
        self.amount = amount

    def __str__(self):
        """ Returns string representation of instance """
        # YOUR CODE GOES HERE #
        return "<{}> {} - {}$ ({} left)".format(
            self.id, self.name, self.price, self.amount)


class Special_Product(Product):
    """ A class of product that sells only to premium users """

    ##### Part 1.3 #####
    def __init__(self, name, price, description="special"):
        """ A constructor that builds the special product instance """
        # YOUR CODE GOES HERE #
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        """ Returns string representation of instance """
        # YOUR CODE GOES HERE #
        return "<{}> {} - {}$ ({})".format(
            self.id, self.name, self.price, self.description)


#######################################################################
#                              WAREHOUSE                              #
#######################################################################


class Warehouse:
    """ A class that creates a warehouse containing products """

    ##### Part 2 #####
    def __init__(self):
        """ A constructor that builds the warehouse instance """
        # YOUR CODE GOES HERE #
        self.inventory = {}
        self.log = []

    def __str__(self):
        """ Returns a string representation of the instance """
        # YOUR CODE GOES HERE #
        return "Warehouse with {} products".format(len(self.inventory))

    def get_product(self, product_id):
        """
        Returns product instance corresponding to product_id if contained
        in the warehouse
        """
        # YOUR CODE GOES HERE #
        try:
            return self.inventory[product_id]
        except KeyError:
            return None

    def list_products(self):
        """ Returns a list of product instances in the inventory """
        # YOUR CODE GOES HERE #
        return list(self.inventory.values())

    def remove_product(self, product_id):
        """ Remove product instance from inventory """
        # YOUR CODE GOES HERE #
        try:
            del self.inventory[product_id]
            self.log.append(
                "Product <{}> removed  - {}"
                .format(product_id, datetime.now()))
            return True
        except KeyError:
            return False

    def import_product(self, product):
        """ Import product instance to inventory """
        # YOUR CODE GOES HERE #
        if product.id not in self.inventory.keys():
            self.inventory[product.id] = product
            self.log.append(
                "Product <{}> imported - {}"
                .format(product.id, datetime.now()))

    def export_product(self, product_id):
        """ Export product instance from inventory """
        # YOUR CODE GOES HERE #
        try:
            product_instance = self.inventory[product_id]
        except KeyError:
            return None
        else:
            self.log.append(
                "Product <{}> exported - {}"
                .format(product_id, datetime.now()))
            if isinstance(product_instance, Limited_Product):
                product_instance.amount -= 1
                if product_instance.amount == 0:
                    self.remove_product(product_id)
            return product_instance

    def size(self):
        """ Returns the number of products stored in the inventory """
        # YOUR CODE GOES HERE #
        return len(self.inventory)

    def show_log(self):
        """ Prints the log strings stored in the warehouse log """
        # YOUR CODE GOES HERE #
        for i in self.log:
            print(i)


#######################################################################
#                               HISTORY                               #
#######################################################################
class History:
    """ A class that contains purchase history records """

    ##### Part 3 #####
    history_counter = 0

    def __init__(self, product, user):
        """ A constructor that builds the history instance """
        self.product = product
        self.user = user
        self.id = History.history_counter
        self.time = datetime.now()
        History.history_counter += 1

    def __str__(self):
        """ Returns string representation of history instance """
        # YOUR CODE GOES HERE #
        return "<{}> {} bought {} at {}".format(
            self.id, self.user.id, self.product, self.time)

    def __repr__(self):
        """ Returns object representation of history instance """
        # YOUR CODE GOES HERE #
        return "HISTORY<{}> - {}".format(self.id, self.time)


#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """ A class that creates users """

    ##### Part 4.1 #####
    user_counter = 0

    def __init__(self, name, store):
        """ A constructor that builds a user instance """
        # YOUR CODE GOES HERE #
        self.name = name
        self.store = store
        self.balance = 0
        self.id = User.user_counter
        self.purchase_history = Stack()
        self.cart = Queue()
        self.store.add_user(self)
        User.user_counter += 1

    def __str__(self):
        """ Returns string representation of user instance """
        # YOUR CODE GOES HERE #
        return "standard user: {} - {}$".format(self.name, self.balance)

    def __repr__(self):
        """ Returns object representation of user instance """
        # YOUR CODE GOES HERE #
        return "USER<{}>".format(self.id)

    def set_name(self, new_name):
        """ Changes username """
        # YOUR CODE GOES HERE #
        self.name = new_name

    def get_name(self):
        """ Returns username """
        # YOUR CODE GOES HERE #
        return self.name

    def set_balance(self, amount):
        """ Sets the balance to amount """
        # YOUR CODE GOES HERE #
        self.balance = amount

    def get_balance(self):
        """ Returns balance """
        # YOUR CODE GOES HERE #
        return self.balance

    def add_balance(self, amount):
        """ Adds amount to balance """
        # YOUR CODE GOES HERE #
        self.balance += amount

    def last_purchase(self):
        """ Returns last purchase history instance """
        # YOUR CODE GOES HERE #
        return self.purchase_history.peek()

    def view_history(self):
        """ Prints user purchase history """
        # YOUR CODE GOES HERE #
        print(self.purchase_history)

    def view_cart(self):
        """ Prints user's cart """
        # YOUR CODE GOES HERE #
        print(self.cart)

    def clear_cart(self):
        """ Empties cart """
        # YOUR CODE GOES HERE #
        while not self.cart.is_empty():
            self.cart.dequeue()

    ##### Part 5.2 #####
    def add_cart(self, product_id):
        """ Adds product to user's cart """
        # YOUR CODE GOES HERE #
        add_product = self.store.warehouse.get_product(product_id)
        if add_product is not None:
            self.cart.enqueue(add_product)

    def checkout(self):
        """ Orders products in cart and returns list of purchased items """
        # YOUR CODE GOES HERE #
        purchased_products = []
        while not self.cart.is_empty():
            if not self.store.order(self.id, self.cart.peek().id):
                break
            purchased_products.append(self.cart.peek())
            self.cart.dequeue()
        return purchased_products

    ##### Part 5.3 #####
    def undo_purchase(self):
        """ Removes last purchase from purchase history """
        # YOUR CODE GOES HERE #
        if self.purchase_history.is_empty():
            print("USER: no purchase history")
            return
        if self.store.undo_order(self.id, self.last_purchase().product):
            self.purchase_history.pop()


class Premium_User(User):
    """ A class of user that has premium benefits """

    ##### Part 4.2 #####
    def __str__(self):
        """ Returns string representation of premium user instance """
        # YOUR CODE GOES HERE #
        return "premium user: {} - {}$".format(self.name, self.balance)

    ##### Part 5.4 #####
    def buy_all(self, product_id):
        """ Buys all limited products until product or balance runs out """
        # YOUR CODE GOES HERE #
        purchased_products = []
        product_instance = self.store.warehouse.get_product(product_id)
        if isinstance(product_instance, Limited_Product):
            while product_instance.amount > 0:
                if not self.store.order(self.id, product_id):
                    break
                purchased_products.append(product_instance)
        else:
            print("USER: not a limited product")
        return purchased_products

    def undo_all(self):
        """
        Undos all purchases until last purchase is limited or purchase
        history is cleared
        """
        # YOUR CODE GOES HERE #
        while not self.purchase_history.is_empty():
            if isinstance(self.last_purchase(), Limited_Product):
                break
            self.undo_purchase()


#######################################################################
#                               STORE                                 #
#######################################################################
class Store:
    """ A class that creates a store instance """

    ##### Part 4.3 #####
    def __init__(self, warehouse):
        """ A constructor that builds the store instance """
        # YOUR CODE GOES HERE #
        self.users = {}
        self.warehouse = warehouse

    def __str__(self):
        """ Returns string representation of store instance """
        # YOUR CODE GOES HERE #
        return "STORE: store with {} users and {} products".format(
            len(self.users), len(self.warehouse))

    def get_product(self, product_id):
        """ Looks up product using product_id """
        # YOUR CODE GOES HERE #
        return self.warehouse.get_product(product_id)

    def view_products(self, sort=False):
        """ Prints all products in inventory """
        # YOUR CODE GOES HERE #
        header = "============================" + "\n" + "<ID> Product - Price"
        footer = "============================"
        if sort:
            sorted_product_prices = sorted([
                i.price for i in self.warehouse.list_products()])
            print(header)
            [print(j) for i in sorted_product_prices
                for j in self.warehouse.list_products() if j.price == i]
            print(footer)
        else:
            print(header)
            for i in self.warehouse.list_products():
                print(i)
            print(footer)

    ##### Part 5.1 #####
    def add_user(self, user):
        """ Adds user to store user records """
        # YOUR CODE GOES HERE #
        if user in self.users.values():
            print("STORE: User already exists")
            return False
        self.users[user.id] = user
        return True

    ##### Part 5.2 #####
    def order(self, user_id, product_id):
        """ Orders the product for user from the store """
        # YOUR CODE GOES HERE #
        shipping_fee = 1.1
        try:
            product_order = self.warehouse.inventory[product_id]
        except KeyError:
            print("STORE: Product not found")
            return False
        else:
            user_order = self.users[user_id]
            if isinstance(product_order, Special_Product):
                if isinstance(user_order, Premium_User):
                    if user_order.get_balance() >= product_order.price:
                        user_order.balance = (
                            user_order.get_balance() - int(product_order.price)
                            )
                        self.warehouse.export_product(product_id)
                        print(
                            "STORE: {0} ordered {1}. {0} has {balance}$ left."
                            .format(
                                user_order.get_name(),
                                product_order.name,
                                balance = user_order.get_balance())
                            )
                        order_hist_inst = History(product_order, user_order)
                        user_order.purchase_history.push(order_hist_inst)
                        return order_hist_inst
                    print("STORE: Not enough money QQ")
                    return False
                print("STORE: Special product is limited to premium user")
                return False
            if isinstance(user_order, Premium_User):
                product_price = int(product_order.price)
            else:
                product_price = int(shipping_fee * product_order.price)
            if user_order.get_balance() < product_price:
                print("STORE: Not enough money QQ")
                return False
            user_order.balance = user_order.get_balance() - product_price
            self.warehouse.export_product(product_id)
            print(
                "STORE: {0} ordered {1}. {0} has {balance}$ left."
                .format(
                    user_order.get_name(),
                    product_order.name,
                    balance = user_order.get_balance())
                )
            order_hist_inst = History(product_order, user_order)
            user_order.purchase_history.push(order_hist_inst)
            return order_hist_inst

    ##### Part 5.3 #####
    def undo_order(self, user_id, product):
        """ Cancels user's last order and refunds money """
        # YOUR CODE GOES HERE #
        if isinstance(product, Limited_Product):
            print("STORE: can’t refund Limited_Product")
            return False
        self.users[user_id].balance += product.price
        print(
            "STORE: {0} refunded {1}. {0} has {balance}$ left."
            .format(
                self.users[user_id].get_name(),
                product.name,
                balance = self.users[user_id].get_balance())
            )
        return True

    ##### Part 6 #####
    def so_rich(self, money):
        """
        A function that returns the least amount of money left from money
        after buying a combination of products
        """
        # YOUR CODE GOES HERE #

        # suppose you haven't seen any product yet
        # the only possible amount of money left is "money"
        # this is a set to record the possible money left
        left = set([money])

        # get products
        lst = self.warehouse.list_products()

        for product in lst:

            # a temporary set to save the updates of "left"
            # you don't want to modify the set you're iterating through
            tmp_left = set()

            for m in left:
                # update tmp_left
                if type(product) != Limited_Product:
                    new_left = m
                    while new_left >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                else:
                    # handle limited product
                    new_left = m
                    product_left = product.amount
                    while new_left >= 0 and product_left >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                        product_left -= 1
            left = set(tmp_left)
        return min(left)

    def so_rich_recursive(self, money):
        """ The same function as so_rich but done recursively """
        # YOUR CODE GOES HERE #

        # get products
        lst = self.warehouse.list_products()

        def helper(lst, money):
            # base case
            if len(lst) == 0:
                return money

            cur_min = money
            product = lst[0]
            if type(product) != Limited_Product:
                tmp = money
                while tmp >= product.price:
                    tmp -= product.price
                    if tmp < cur_min:
                        cur_min = tmp
            else:
                tmp = money
                count = product.amount
                while tmp >= product.price and count > 0:
                    tmp -= product.price
                    count -= 1
                    if tmp < cur_min:
                        cur_min = tmp
            return helper(lst[1:], cur_min)

        return min([helper(lst[i:], money) for i in range(len(lst))])
