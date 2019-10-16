from src.data_service.RDBDataTable import RDBDataTable


def t1():
    table = RDBDataTable(table_name="appearances", db_name="lahman2019clean")
    print(table)


t1()
