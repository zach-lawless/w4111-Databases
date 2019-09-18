from src.BaseDataTable import BaseDataTable
import json
import logging
import pymysql

class RDBDataTable(BaseDataTable):

    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """

    _rows_to_print = 10
    _no_of_separators = 2

    def __init__(self, table_name, connect_info, key_columns):
        """

        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """
        self._data = {
            "table_name": table_name,
            "connect_info": connect_info,
            "key_columns": key_columns
        }

        self._logger = logging.getLogger()

        self._logger.debug("RDBDataTable.__init__: data = " + json.dumps(self._data, indent=2))

        self.cnx = pymysql.connect(
            host=self._data["connect_info"].get("host"),
            user=self._data["connect_info"].get("user"),
            password=self._data["connect_info"].get("password"),
            db=self._data["connect_info"].get("db"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def find_by_primary_key(self, key_fields, field_list=None):
        """

        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.
        """
        template = dict(zip(self._data["key_columns"], key_fields))
        return self.find_by_template(template, field_list)

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """

        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}
        :param field_list: A list of request fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list containing dictionaries. A dictionary is in the list representing each record
            that matches the template. The dictionary only contains the requested fields.
        """
        w_clause, args = self.template_to_where_clause(template)
        field_list = self.get_select_fields(field_list)
        schema_name = self._data["connect_info"].get("db")
        table_name = self._data["table_name"]
        full_name = f"{schema_name}.{table_name}"
        sql = "select " + field_list + " from " + full_name + " " + w_clause
        cur = self.cnx.cursor()
        res = cur.execute(sql, args)
        result = cur.fetchall()
        return result

    def delete_by_key(self, key_fields):
        """

        Deletes the record that matches the key.

        :param key_fields: List of value for the key fields.
        :return: A count of the rows deleted.
        """
        template = dict(zip(self._data["key_columns"], key_fields))
        return self.delete_by_template(template)

    def delete_by_template(self, template):
        """

        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        w_clause, args = self.template_to_where_clause(template)
        schema_name = self._data["connect_info"].get("db")
        table_name = self._data["table_name"]
        full_name = f"{schema_name}.{table_name}"
        sql = "delete from " +  full_name + " " + w_clause
        cur = self.cnx.cursor()
        res = cur.execute(sql, args)
        return res

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """
        template = dict(zip(self._data["key_columns"], key_fields))
        return self.update_by_template(template, new_values)

    def update_by_template(self, template, new_values):
        """

        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields.
        :return: Number of rows updated.
        """
        update_list = []
        for k, v in new_values.items():
            update_list.append(f"`{k}`='{v}'")
        update_str = ", ".join(update_list)
        w_clause, args = self.template_to_where_clause(template)
        schema_name = self._data["connect_info"].get("db")
        table_name = self._data["table_name"]
        full_name = f"{schema_name}.{table_name}"
        sql = "update " + full_name + " set " + update_str + " " + w_clause
        print(sql)
        cur = self.cnx.cursor()
        res = cur.execute(sql, args)
        return res

    def insert(self, new_record):
        """

        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """
        if self._data["key_columns"] is not None:
            key_fields = []
            for k in self._data["key_columns"]:
                key_fields.append(new_record[k])
            if len(self.find_by_primary_key(key_fields)) > 0:
                raise ValueError("Can't insert new_record, violates table key")

        cols = []
        values = []
        for k, v in new_record.items():
            cols.append("`" + k + "`")
            values.append("'" + v + "'")
        cols_str = ", ".join(cols)
        values_str = ", ".join(values)
        schema_name = self._data["connect_info"].get("db")
        table_name = self._data["table_name"]
        full_name = f"{schema_name}.{table_name}"
        sql = "insert into " + full_name + " (" + cols_str + ") values (" + values_str + ")"
        print(sql)
        cur = self.cnx.cursor()
        res = cur.execute(sql)

    @staticmethod
    def template_to_where_clause(template):

        if template is None or template == {}:
            w_clause = None
            args = None
        else:
            terms = []
            args = []
            for k, v in template.items():
                terms.append(k + "=%s")
                args.append(v)

            w_clause = "where " + (" and ".join(terms))

        return w_clause, args

    @staticmethod
    def get_select_fields(fields):

        if fields is None or fields == []:
            field_list = " * "
        else:
            field_list = ",".join(fields)

        return field_list
