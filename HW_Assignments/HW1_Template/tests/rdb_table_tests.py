from src.RDBDataTable import RDBDataTable
import logging
import os
import pandas as pd

# The logging level to use should be an environment variable, not hard coded.
# logging.basicConfig(level=logging.DEBUG)

# Also, the 'name' of the logger to use should be an environment variable.
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# This should also be an environment variable.
# Also not the using '/' is OS dependent, and windows might need `\\`
data_dir = os.path.abspath("../Data/Baseball")


def main():
    print("--- RDBDataTable test ---")
    print('No Primary Key')
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }
    rdb_tbl = RDBDataTable("people", connect_info, None)
    print(rdb_tbl)
    print(' - testing find_by_template')
    template = {"nameLast": "Williams", "birthCity": "San Diego"}
    result = rdb_tbl.find_by_template(template, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by template")
    print(str(pd.DataFrame(result)))

    print(' - testing insert a new record, updating the record, and deleting the record')
    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    result = rdb_tbl.find_by_template(new_record, field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found inserted record")
    print(str(pd.DataFrame(result)))

    new_values = {"birthCity": "Fort Worth"}
    n_updates = rdb_tbl.update_by_template(new_record, new_values)
    print("Updated " + str(n_updates) + " records")

    result = rdb_tbl.find_by_template({"playerID": "lawleza01"},
                                      field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found updated record")
    print(str(pd.DataFrame(result)))

    n_deletions = rdb_tbl.delete_by_template({"playerID": "lawleza01"})
    print("Deleted " + str(n_deletions) + " records")

    print('With Primary Key')
    print(' - testing load and find')
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }
    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])
    print(rdb_tbl)
    key_fields = ["willite01"]
    result = rdb_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by key")
    print(str(pd.DataFrame(result)))

    print(' - testing insert a new record, updating the record, and deleting the record')
    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    key_fields = ["lawleza01"]
    result = rdb_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found inserted record")
    print(str(pd.DataFrame(result)))

    new_values = {"birthCity": "Fort Worth"}
    n_updates = rdb_tbl.update_by_key(key_fields, new_values)
    print("Updated " + str(n_updates) + " records")

    result = rdb_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found updated record")
    print(str(pd.DataFrame(result)))

    n_deletions = rdb_tbl.delete_by_key(key_fields)
    print("Deleted " + str(n_deletions) + " records")

    print(' - showing that insert with a key that already exists doesnt execute')
    new_record = {"playerID": "willite01", "nameLast": "Williams", "nameFirst": "Ted", }
    rdb_tbl.insert(new_record)


main()
