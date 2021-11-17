import unittest
from vendingmachine import Item, VendingMachine


class VendingMachineTestCase(unittest.TestCase):
    """
    Testcases for Item and VendingMachine class methods.
    """

    def test_item_buy(self):
        """
        Test if the item quantity is reduced on buying item.
        :return:
        """
        item = Item(1, "test_item", 1, 5)
        item._buy()
        self.assertEqual(item.quantity, 4)

    def test_item_increment_quantity(self):
        """
        Test if the quantity is incremented by given number of units.
        :return:
        """
        item = Item(1, "test_item", 1, 5)
        item._increment_quantity(1)
        self.assertEqual(item.quantity, 6)

    def test_get_item(self):
        """
        Test if the item with given id is filtered.
        :return:
        """
        items = [Item(1, "test_item", 1, 5)]
        vm = VendingMachine(items)
        item = vm.get_item(1)
        self.assertIsNotNone(item)

    def test_add_item_not_exists(self):
        """
        Test if a new item can be added to the vending machine.
        :return:
        """
        items = [Item(1, "test_item", 1, 5)]
        vm = VendingMachine(items)
        vm.add_item(Item(2, "test_item_other", 2, 1))
        new_item = vm.get_item(2)

        self.assertIsNotNone(new_item)

    def test_add_item_exists(self):
        """
        Test if the quantity is incremented upon adding existing item.
        :return:
        """
        items = [Item(1, "test_item", 1, 5)]
        vm = VendingMachine(items)
        vm.add_item(Item(1, "test_item", 1, 1))
        new_item = vm.get_item(1)

        self.assertEqual(new_item.quantity, 6)


if __name__ == '__main__':
    unittest.main()
