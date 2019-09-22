from src.CSVDataTable import CSVDataTable
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
    print("--- CSVDataTable test ---")
    print('No Primary Key')
    print(' - testing load')
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    csv_tbl = CSVDataTable("people", connect_info, None)
    print("Created table = " + str(csv_tbl))

    print(' - testing find_by_template')
    template = {"nameLast": "Williams", "birthCity": "San Diego"}
    subset = csv_tbl.find_by_template(template, field_list=["playerID", "nameLast", "nameFirst"])
    print(str(pd.DataFrame(subset)))

    print(' - testing update_by_template (first row birthCity from Denver to Los Angeles')
    template = {"playerID": "aardsda01"}
    n_updates = csv_tbl.update_by_template(template, new_values={"birthCity": "Los Angeles"})
    print("Update by template: " + str(n_updates) + " updates")
    print(str(csv_tbl))

    print(' - testing insert')
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "lawlesszach01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))

    print(' - testing delete (first row being deleted)')
    template = {"playerID": "aardsda01"}
    n_deletions = csv_tbl.delete_by_template(template)
    print("Delete by template: " + str(n_deletions) + " deletions")
    print(str(csv_tbl))

    print(' - testing save (Data/People_saved.csv will be created)')
    csv_tbl.save()

    print('With Primary Key')
    print(' - testing load and find')
    csv_tbl = CSVDataTable("people", connect_info, ["playerID"])
    print(csv_tbl)
    key_fields = ["willite01"]
    subset = csv_tbl.find_by_primary_key(key_fields, field_list=["playerID", "nameLast", "nameFirst"])
    print("Found by key")
    print(str(pd.DataFrame(subset)))

    print(' - testing update_by_key (first row birthCity from Denver to Los Angeles')
    key_fields = ["aardsda01"]
    n_updates = csv_tbl.update_by_key(key_fields, new_values={"birthCity": "Los Angeles"})
    print("Update by template: " + str(n_updates) + " updates")
    print(str(csv_tbl))

    print(' - testing insert (new record, will succeed')
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "lawlesszach01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))

    print(' - testing insert (duplicate record, will not insert')
    print("Number of records before insert: " + str(len(csv_tbl.get_rows())))
    new_record = {
        "playerID": "aardsda01",
        "birthCity": "Dallas",
        "age": "26"
    }
    csv_tbl.insert(new_record)
    print("Number of records after insert: " + str(len(csv_tbl.get_rows())))

    print(' - testing delete (first row being deleted)')
    key_fields = ["aardsda01"]
    n_deletions = csv_tbl.delete_by_key(key_fields)
    print("Delete by key: " + str(n_deletions) + " deletions")
    print(str(csv_tbl))

    print(' - save already tested')


main()
