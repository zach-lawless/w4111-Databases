# COMSW 4111 Homework 2
* Name: Zach Lawless
* UNI: ztl2103

## Design Decisions
I made all design decisions with the mindset of keeping code as simple and modular as possible.
I took advantage of the `dbutils` functions in order to execute on `db` and `tbls` API calls.

As for the `RDBDataTable` class, I implemented `get_row_count`, `get_primary_key_columns`,
`get_sample_rows`, and an additional `get_columns` that wasn't included in the skeleton
framework.  Each of these methods updates the class variables for their respective function
definition. I did need to change the connection credentials to connect to my `lahman2019clean` schema. Similarly to Homework 1 as well as demos from lectures, my connection username is `dbuser` and my connection password is `dbuserdbuser`. These values are hardcoded into the `RDBDataTable.py` file, and if connection errors occur during grading, this would be a good place to start debugging.

Once those setup implementations were complete, I was able to focus on API functions.
Based on the incoming HTTP Request code (`GET`, `DELETE`, `PUT`, `POST`), I implemented the
respective SQL implementation via `RDBDataTable` (`SELECT`, `DELETE`, `UPDATE`, `INSERT`).

I checked the result of the queries before returning an HTTP Response. If the query was
successful, I returned HTTP 200 code with either the data selected, or the number of records
updated, inserted, or deleted.  If the result came back empty, I returned an HTTP 404 Not
Found error.

## Testing
I did some basic testing of `data_table_adaptor` and `RDBDataTable` development in
`unit_test.py`, but due to the functionality basically being provided, I spent most time
testing via Postman API calls to the running Flask app.  This testing paradigm was simple,
intuitive, and fast. All of my complete unit testing screenshots proving out functionality
is included in `unit_tests.pdf`.

## Learning Objectives
The overall learning objectives for this homework are as followed:
1. Understanding HTTP and API execution
2. Translating incoming HTTP Requests into SQL queries
3. Returning appropriate HTTP Responses back to the API
4. Understand the overall software architecture of a lightweight app and how a user might
inherently interact with data without knowing it.

## Closing Remarks
I found this homework to be a nice, logical assignment that built on the foundation laid by
Homework 1 and recent lectures. The exposure to Postman was new and a fun tool to learn.
While this assignment doesn't come close to the complexity of a full-stack software web app,
it was a nice taste in to how the development may occur, and the design decisions
associated with web app development.
