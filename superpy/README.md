 # **SuperPy**
 
*This program was created to support supermarkets in providing easy insight into their processes. By using this program, for example, the stock can be requested or it can be shown what the profit is over the requested time period.*


# Parts of the program

This paragraph provides an overview of the components of the program. Explanation about the use can be found in the user manual section. The program contains the following components:

This program consists three main parts: working with time, inventory management and financial insight.

Working with time has three program parts: today, reset_today, advance_time and backward_time.

Inventory management has eight parts: inventory, inventory_csv_to_pdf, buy, sell, purchases, sales, lack and stock.

Financial insight has two program components: profit and revenue.

# Before using

Open a command line tool. First, check whether you have Python installed on your computer. If not, download python. Download and save Superpy to your computer. And download all modules that this program uses: (argparse, csv, datetime, rich, pandas, os and csv2pdf). Create a folder (directory) called superpy in your current working directory. You can decide for yourself how to do that. If you can't do this by the command prompt or powershell, you can use the helper function create_working_directory('superpy').

The command "directory" creates a folder where the csv files are stored. "directory" does not take positional arguments.

superpy>main.py directory

# User manual

In the command line tool: go to where you saved Superpy. A command that is a good option to start with is the --help comand. If all goes well you will see the following:

C:\Users\your_name\Desktop\superpy>main.py --help

usage: main.py [-h] {today,advance_time,backward_time,inventory,inventory_csv_to_pdf,purchases,sales,lack,stock,buy,sell,revenue,profit} ...

Superpy command line tool for supermarket data

positional arguments:
  {today,advance_time,backward_time,inventory,inventory_csv_to_pdf,purchases,sales,lack,stock,buy,sell,revenue,profit}
-    today                Show today's date
-    reset_today          Reset the internal date to calendar date
-    advance_time         Moves the internal date forward by the desired number of days
-    backward_time        Moves the internal date backwards by the desired number of days
-    inventory            Shows the current stock of the supermarket using rich
-    inventory_csv_to_pdf Converts inventory.csv to inventory.pdf
-    purchases            Shows the purchases of the supermarket
-    sales                Shows the sales of the supermarket
-    lack                 Shows the shrinkage of the supermarket
-    stock                Shows the stock of the supermarket
-    buy                  Add new purchase to current stock file and purchases file
-    sell                 Remove stock from the current stock file and adds new sales to sales file
-    revenue              Shows the revenue of the supermarket. Please enter dates in the following format: yyyy-mm-dd
-    profit               Shows the profit of the supermarket. Please enter dates in the following format: yyyy-mm-dd

options:
  -h, --help            show this help message and exit

## working with time
The command "reset_today" resets the date to the calendar date. "reset_today" does not take positional arguments.

superpy>main.py reset_today

The command "today" shows today's date. "today" does not take positional arguments.

superpy>main.py today

The command "advance_time" shows internal date plus the days you entered. It take one positional argument: an integer. For example if you want to add two days to today:

superpy>main.py advance_time 2

The command "backward_time" shows internal date minus the days you entered. It take one positional argument: an integer. For example, if you want to subtract two days from today:

superpy>main.py backward_time 2

## Inventory management

The command "inventory" Shows the current stock of the supermarket using rich. "inventory" does not take positional arguments.

superpy>main.py inventory

The command "inventory_csv_to_pdf" Converts inventory.csv to inventory.pdf. "inventory_csv_to_pdf" does not take positional arguments.

superpy>main.py inventory_csv_to_pdf

The command "purchases" Shows the purchases of the supermarket. "purchases" does not take positional arguments.

superpy>main.py purchases

The command "sales" Shows the sales of the supermarket. "sales" does not take positional arguments.

superpy>main.py sales

The command "lack" Shows the shrinkage of the supermarket. "lack" does not take positional arguments.

superpy>main.py lack

The command "stock" Shows the stock of the supermarket. "stock" does not take positional arguments.

superpy>main.py stock

The command "buy" add new purchase to current stock file and purchases file. It takes four positional arguments: a string, integer, integer, string. So for example:

superpy>main.py buy 'Plum', 4, 2, '2023-10-19'

The command "sell" remove stock from the current stock file and adds new sales to sales file. It takes four positional arguments: a string, integer, integer, string. So for example:

superpy>main.py sell 'Apple', 4, 2, '2023-10-19'

## Financial insight

The command "revenue" shows the revenue of the supermarket. It takes two positional arguments: a string and a string. So for example: 
Please notice, dates should be entered in the following format: yyyy-mm-dd

superpy>main.py revenue 2023-01-01 2023-02-28

The command "profit" shows the profit of the supermarket. It takes two positional arguments: a string and a string. So for example: 
Please notice, dates should be entered in the following format: yyyy-mm-dd

superpy>main.py profit 2023-01-01 2023-02-28

# In conclusion

The maker of Superpy hopes that this tool will make working in the supermarket a lot easier.