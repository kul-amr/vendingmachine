from utils import custom_log, MSG_DEBUG, MSG_ERROR, MSG_INFO


class Item:
    """
    SnackItem with attributes

    Attributes:
        id : int
            ID of the snack item.
            This will be unique to the item in a vending machine.
        name : string
            Name of the snack item.
        price : float
            Price of the snack item.
        quantity : int
            Stock quantity of the snack item.
    """

    def __init__(self, id, name, price, quantity):
        """
        Instantiates the snack item with below attributes.
        :param id (int): ID of the snack item
        :param name (string): Name of the snack item
        :param price (float): Price of the snack item
        :param quantity (int): Stock quantity of the snack item
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def _buy(self, units=1):
        """
        To buy given units of snack, by default 1 i.e reduces item quantity
        by given number of units or 1.

        :param units (int, optional): Number of items to buy, default 1.
        :return:
        """
        self.quantity -= units

    def _increment_quantity(self, units):
        """
        Increments the quantity of snack item by given number of units.

        :param units (int): Number of items to increment.
        :return:
        """
        self.quantity += units


class VendingMachine:
    """
    VendingMachine class contains list of snack items with attributes as
    price and quantity. User can view the list of snack items available
    with corresponding prices and quantity. User can select the snack and
    enter ID corresponding to that snack to buy it. User will be prompted
    to pay and continue/stop the shopping.
    """

    def __init__(self, items=[]):
        """
        Instantiates VendingMachine with list of snack items. By default
        no snack items available. The amount attribute stores and updates
        the money entered by user.
        :param items (list, optional): List of snack items.
        """
        self.amount = 0
        self.items = items

    def get_items(self):
        """
        Return existing items i.e with quantity non zero.
        :return:
        """
        return [item for item in self.items if item.quantity > 0]

    def get_item(self, option):
        """
        Checks if the item with id as the selected option exists in the vending machine.
        :param option (int): Selected snack's id
        :return: Vending machine snack item corresponding to the selected id.
        """
        selected_item = None
        items = [item for item in self.items if item.id == option]
        if len(items) > 0:
            selected_item = items[0]
        return selected_item

    def add_item(self, item):
        """
        Adds a snack item to the vending machine if not existing already else
        increments the quantity of the existing one by adding new quantity.
        :param item: Snack item to add to the vending machine .
        :return:
        """
        item_exists = self.get_item(item.id)

        if item_exists:
            item_exists._increment_quantity(item.quantity)
        else:
            self.items.append(item)

    def pay_for_item(self, item):
        """
        Checks if the entered payment amount is greater than the selected item price.
        Carry forwards the paid amount and item price difference for that user's further
        shopping.
        :param item: Selected item.
        :return:
        """
        while self.amount < item.price:
            paid_amount = float(input(f"Pay €{round((item.price - self.amount), 2)} : "))
            if paid_amount <= 0:
                custom_log("Invalid amount entered.", MSG_ERROR)
                continue
            self.amount = self.amount + paid_amount

    def buy_item(self, item):
        """
        Checks if the paid amount is not less than the item price.
        If not then buys the item.
        :param item:
        :return:
        """
        if self.amount < item.price:
            custom_log("Insufficient amount. Insert more coins.", MSG_ERROR)
        else:
            self.amount = round((self.amount - item.price), 2)
            item._buy()
            custom_log(f"You bought - {item.name}, remaining cash - €{self.amount}", MSG_DEBUG)

    def return_change(self):
        """
        Checks if there is any money left from what user had paid and returns it.
        :return:
        """

        if self.amount > 0:
            custom_log(f"Change to return : €{self.amount}", MSG_DEBUG)
        else:
            custom_log("No change to return.", MSG_DEBUG)
