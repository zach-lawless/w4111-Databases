# I write and test methods one at a time.
# This file contains unit tests of individual methods.

from src.CSVDataTable import CSVDataTable
from src.RDBDataTable import RDBDataTable
import logging
import os
import pandas as pd


# The logging level to use should be an environment variable, not hard coded.
logging.basicConfig(level=logging.DEBUG)

# Also, the 'name' of the logger to use should be an environment variable.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# This should also be an environment variable.
# Also not the using '/' is OS dependent, and windows might need `\\`
data_dir = os.path.abspath("../Data/Baseball")


# ----- CSVDataTable Unit Test Functions ----- #
def t_csv_load():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    print("Created table = " + str(csv_tbl))


def t_csv_find_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    template = {"nameLast": "Williams", "birthCity": "San Diego"}
    subset = csv_tbl.find_by_template(template, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by template")
    print(str(pd.DataFrame(subset)))


def t_csv_find_by_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])

    key_fields = ["willite01"]
    subset = csv_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by key")
    print(str(pd.DataFrame(subset)))


def t_csv_del_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    # template = {"nameLast": "Williams", "birthCity": "San Diego"}
    template = {"playerID": "aardsda01"}
    n_deletions = csv_tbl.delete_by_template(template)
    print("Delete by template: " + str(n_deletions) + " deletions")
    print(str(csv_tbl))


def t_csv_del_by_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])

    # key_fields = ["willite01"]
    key_fields = ["aardsda01"]
    n_deletions = csv_tbl.delete_by_key(key_fields)
    print("Delete by key: " + str(n_deletions) + " deletions")
    print(str(csv_tbl))


def t_csv_update_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    #template = {"nameLast": "Williams", "birthCity": "San Diego"}
    template = {"playerID": "aardsda01"}
    n_updates = csv_tbl.update_by_template(template, new_values={"birthCity": "Los Angeles"})
    print("Update by template: " + str(n_updates) + " updates")
    print(str(csv_tbl))


def t_csv_update_by_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])

    # key_fields = ["willite01"]
    key_fields = ["aardsda01"]
    n_updates = csv_tbl.update_by_key(key_fields, new_values={"birthCity": "Los Angeles"})
    print("Update by template: " + str(n_updates) + " updates")
    print(str(csv_tbl))


def t_csv_insert_no_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "lawlesszach01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))


def t_csv_insert_with_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "lawlesszach01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))


def t_csv_insert_with_key_failure():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "aardsda01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))


def t_csv_save():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)
    csv_tbl.save()


# t_csv_load()
# t_csv_find_by_template()
# t_csv_find_by_key()
# t_csv_del_by_template()
# t_csv_del_by_key()
# t_csv_update_by_template()
# t_csv_update_by_key()
# t_csv_insert_no_key()
# t_csv_insert_with_key()
# t_csv_insert_with_key_failure()
# t_csv_save()

# ----- RDBDataTable Unit Test Functions ----- #
def t_rdb_find_by_template():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, None)

    template = {"nameLast": "Williams", "birthCity": "San Diego"}
    result = rdb_tbl.find_by_template(template, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by template")
    print(str(pd.DataFrame(result)))


def t_rdb_find_by_primary_key():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])

    key_fields = ["willite01"]
    result = rdb_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by key")
    print(str(pd.DataFrame(result)))


def t_rdb_del_by_template():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, None)

    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    n_deletions = rdb_tbl.delete_by_template(new_record)
    print("Deleted " + str(n_deletions) + " records")


def t_rdb_del_by_key():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])

    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    new_record_key_fields = [new_record["playerID"]]
    n_deletions = rdb_tbl.delete_by_key(new_record_key_fields)
    print("Deleted " + str(n_deletions) + " records")


def t_rdb_update_by_template():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, None)

    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    result = rdb_tbl.find_by_template(new_record, field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found inserted record")
    print(str(pd.DataFrame(result)))

    new_values = {"birthCity": "Fort Worth"}
    n_updates = rdb_tbl.update_by_template(new_record, new_values)
    print("Updated " + str(n_updates) + " records")

    result = rdb_tbl.find_by_template({"playerID": "lawleza01"}, field_list=["playerID", "nameLast", "nameFirst", "birthCity"])
    print("Found updated record")
    print(str(pd.DataFrame(result)))

    n_deletions = rdb_tbl.delete_by_template({"playerID": "lawleza01"})
    print("Deleted " + str(n_deletions) + " records")


def t_rdb_update_by_key():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])

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


def t_rdb_insert_no_key():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, None)

    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    result = rdb_tbl.find_by_template(new_record, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found inserted record")
    print(str(pd.DataFrame(result)))

    n_deletions = rdb_tbl.delete_by_template(new_record)
    print("Deleted " + str(n_deletions) + " records")


def t_rdb_insert_with_key():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])

    new_record = {"playerID": "lawleza01", "nameLast": "Lawless", "nameFirst": "Zach", "birthCity": "Dallas"}
    rdb_tbl.insert(new_record)

    new_record_key_fields = [new_record["playerID"]]
    result = rdb_tbl.find_by_primary_key(new_record_key_fields, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found inserted record")
    print(str(pd.DataFrame(result)))

    n_deletions = rdb_tbl.delete_by_key(new_record_key_fields)
    print("Deleted " + str(n_deletions) + " records")


def t_rdb_insert_with_key_failure():
    connect_info = {
        "host": "localhost",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "db": "lahman2019raw",

    }

    rdb_tbl = RDBDataTable("people", connect_info, ["playerID"])

    new_record = {"playerID": "willite01", "nameLast": "Williams", "nameFirst": "Ted",}
    rdb_tbl.insert(new_record)


# t_rdb_find_by_template()
# t_rdb_find_by_primary_key()
# t_rdb_del_by_template()
# t_rdb_del_by_key()
# t_rdb_update_by_template()
# t_rdb_update_by_key()
# t_rdb_insert_no_key()
# t_rdb_insert_with_key()
# t_rdb_insert_with_key_failure()
