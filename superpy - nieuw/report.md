

# Superpy Report
*In this report, you can read three technical aspects of Superpy*

1. **Helper.py**

Helper.py contains generic code that can be integrated into various functions in main.py. This improves the readability of the code and makes maintenance a lot easier.

2. **Buy() and sell()**

The buy() and sell() functions attribute data to both the current_stock.csv and the purchases.csv/sales.csv. The problem it solves is that two csv files have to be read and compared when requesting the stock. This is no longer necessary because the stock file is also updated with a purchase and a sale. When the stock is requested, only current_stock.csv needs to be read.

3. **Argparse**

The use of Argparse allows for user-friendly command-line interfaces. If you would not use this module, there is a chance that the script will be modified. Now you can issue commands to the program and call functions without typing in the environment where the script is located.
