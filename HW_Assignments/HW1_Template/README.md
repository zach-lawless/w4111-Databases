# COMS W4111 Homework 1

Name: Zach Lawless

UNI: ztl2103

Date: 9/22/19

## Execution Instructions
In order to test the functionality of each database implementation,
you can run either `csv_table_tests.py` or `rdb_table_tests.py` from PyCharm using the 'Run filename.py'
PyCharm functionality. The output of these tests will be logged to the terminal, and the standard
output from the unaltered tests printed to the console have been manually copied into `csv_table_test.txt` and
`rdb_table_test.txt`, respectively.

Feel free to edit and test manually within files, as results will be printed to the console for inspection.

## Implementation
All functionality of the two implementations where developed and tested in
PyCharm. All of the `_by_template` functionality was implemented first, followed
by the `_by_key` functionality, which first checks for key violations, and then
if no violation, leverages `_by_template` functionality.

I used `find_by_key` functionality to test if there were any key violations. When there
were no violations, meaning nothing returned, then I would call `insert` or `update` functionality.

## General Notes and Comments
General relational database concepts taught in lectures 1 and 2 are implemented in the two abstractions
requested in the homework. This shows that there are many ways to develop database-like functionality, in
many different formats. However, from my experience developing this assignment, interfacing directly with
a relational database is much easier than implementing the same functionality from scratch (CSVDataTable).
RDBDataTable is a nice abstraction in Python to interface directly with an existing database, whereas
CSVDataTable aims to recreate the functionality directly. RDBDataTable could be implemented in a user-facing
web application, obfuscating the relational database concepts from the user but still leveraging them behind
the scenes.