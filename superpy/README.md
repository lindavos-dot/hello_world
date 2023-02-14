 # Python Final Assignment: SuperPy
 
 *You need to master the following to complete this assignment:*
*Independently designing logic flow based on a description of what the program should do; Using and debugging Python classes; Writing, running and interpreting tests in Pytest.*

This is your biggest Python assignment so far, so get comfortable! It is supposed to take you a couple days to complete. You are going to build a command-line tool that a supermarket will use to keep track of their inventory.

There are three important modules from the standard library you must use for this:

1. csv -- CSV File Reading and Writing

CSV stands for 'comma separated values'. It's the most common import and export format for spreadsheets and databases, used by -- or at least compatible with -- every software package you can think of in that space. It is a great skill to be able to read, manipulate and write these files.

2. argparse -- Parser for command-line options, arguments and subcommands

Command-line tools are tools you've probably used a lot already. Examples that may be familiar to you are ls to show the contents of a directory and cd to change the working directory. Another common tool is echo to parse and output some input you give it (try echo "hello world").

There are three command-line fundamentals you should search the web for before you dive into the exercise: stdin, stdout, command-line arguments. The argparse module helps you to write your own command-line tool. Now that you know about command-line arguments, you should be able to see why it's named argparse.

3. datetime -- Basic date and time types(opens in a new tab)

Dates are notoriously hard to work with in software. The list of things to consider includes timezones, daylight saving time, leap years and of course countless different notation styles. We will standardize on a single source of truth: the date object, and use a string representation following the format: '%Y-%m-%d'. Read the linked documentation to learn how to use these two facts!

# Superpy

A large supermarket chain has asked you to write a command-line tool that is able to keep track of their inventory: they want to call it SuperPy. The core functionality is about keeping track and producing reports on various kinds of data:

Which products the supermarket offers;
How many of each type of product the supermarket holds currently;
How much each product was bought for, and what its expiry date is;
How much each product was sold for or if it expired, the fact that it did;
All data must be saved in CSV files. 

Your program should have an internal conception of what day it is. Interaction with your program must go through the command-line. 

# Code

Be creative with your implementation! We intentionally keep the specification open to encourage you to be creative with this project. However, to obtain a passing grade, you will at least need to satisfy the following requirements:

Well-structured and documented code, including:
- Clear and effective variable and function names;
- Use of comments where the code does not speak for itself;
- Clear and effective separation of code into separate functions and possibly files.
- Use of modules to the extent that it shows you were able to independently read and understand the documentation, and apply the techniques within:
csv, argparse, datetime, including in particular the date object, strftime
and strptime functions and datetime arithmetic using timedelta.

- Use of external text files (CSV) to read and write data.
- A well-structured and user friendly command-line interface with clear descriptions of each argument in the --help section.

A text file containing a usage guide aimed with peers as the target audience. The usage guide should include plenty of examples.

# The application must support:

Setting and advancing the date that the application perceives as 'today';
Recording the buying and selling of products on certain dates;
Reporting revenue and profit over specified time periods;
Exporting selections of data to CSV files;
Two other additional non-trivial features of your choice, for example:
The use of an external module Rich(opens in a new tab) to improve the application.
The ability to import/export reports from/to formats other than CSV (in addition to CSV)
The ability to visualize some statistics using Matplotlib(opens in a new tab)
Another feature that you thought of.
Report

Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. Include this in your repository as a report.md file.

You may use Markdown for your report, but it is not required.
To assist your explanation you may use code snippets.