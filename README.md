VendingMachine application gives list of snack items 
with attributes as price and quantity. User can view 
the list of snack items available with corresponding 
prices and quantity. User can select the snack and 
enter ID corresponding to that snack to buy it. User 
will be prompted to pay and continue/stop the shopping.

To run the application, need to create the docker image as:

    docker build -t [IMAGE-TAG] .

To run the application interactively from docker container :
    
    docker run -it [IMAGE-TAG]

This will display the list of snack items available. 

    Available snacks, prices and quantity as :
    ------------------------------------------------
    
    0 - Exit
    1 - Crisps €2   (1)
    2 - Fazer Chocolate €2.95   (1)
    3 - Geisha Chocolate €1.5   (1)
    4 - Tutti Frutti Mix €2.8   (5)
    5 - Domino Original €2.3   (2)
    6 - Fasupala waffle €3.2   (4)
    7 - Xylimax Peppermint €2.7   (4)
    8 - Coke €1   (1)
    Enter ID for selected snack : 1
    Pay €2 : 5
    You bought - Crisps, remaining cash - €3.0
    Continue to buy something else? (y/n): y


If entered incorrect ID, app will show error message and will
prompt to enter ID again. When the user does not want to buy 
anything, this app will return the remaining amount. 