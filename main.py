from vendingmachine import VendingMachine, Item
from utils import custom_log, MSG_DEBUG, MSG_ERROR, MSG_INFO


def main():
    """
    Vending machine class instance is created and few snack items are added.
    Shopping for a user is started in an infinite loop until user wants
    to stop shopping.
    :return:
    """

    items = [Item(1, 'Crisps', 2, 1),
             Item(2, 'Fazer Chocolate', 2.95, 1),
             Item(3, 'Geisha Chocolate', 1.50, 1),
             Item(4, 'Tutti Frutti Mix', 2.80, 5),
             Item(5, 'Domino Original', 2.30, 2),
             Item(6, 'Fasupala waffle', 3.20, 4),
             Item(7, 'Xylimax Peppermint', 2.70, 4),
             Item(8, 'Coke', 1, 1)]

    v = VendingMachine(items)

    continue_buying = True
    while continue_buying:
        items = v.get_items()

        if len(items) == 0:
            custom_log("Sorry, No snack item is available.", MSG_ERROR)
            v.return_change()
            break

        custom_log("\nAvailable snacks, prices and quantity as :", MSG_INFO)
        custom_log("--------------------------------------------------\n", MSG_INFO)
        custom_log(f"0 - Exit", MSG_INFO)
        for item in items:
            custom_log(f"{item.id} - {item.name} €{item.price}   ({item.quantity})", MSG_INFO)

        option = ''
        try:
            option = int(input('Enter ID for selected snack : '))

            if option == 0:
                continue_buying = False
                v.return_change()
            else:
                item = v.get_item(option)

                if item:
                    v.pay_for_item(item)
                    v.buy_item(item)
                    buy_more = input("Continue to buy something else? (y/n): ")

                    if buy_more != 'y':
                        continue_buying = False
                        v.return_change()
                else:
                    custom_log("Selected item is not available.", MSG_ERROR)

        except ValueError:
            custom_log("Invalid input. Please enter a number.", MSG_ERROR)


main()
