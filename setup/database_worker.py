__author__ = 's.lugovskiy'
import pymysql


def connect(dbhost='10.8.0.229', dbport=3306, dbuser='root', dbpasswd='123456', dbname='monitoring'):
    """

    :rtype: Connect
    """
    conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbname)
    return conn


def select(table, column, where='', limit=' LIMIT 1 ', order=' ORDER BY id DESC '):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT ' + column + ' from ' + table + where + order + limit
    print(sql)
    cursor.execute(sql)
    connection.commit()
    elements = cursor.fetchall()
    connection.close()
    return elements


def update(table, where_column, where_value, column, value):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = 'UPDATE ' + table + ' SET ' + column + ' = "' + str(value) + '" WHERE ' + where_column + ' = "' + where_value + '"'
    print(sql)
    cursor.execute(sql)
    connection.commit()
    elements = cursor.fetchall()
    connection.close()
    return elements


def delete(table, where_column, where):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = 'DELETE FROM ' + str(table) + ' WHERE ' + str(where_column) + " = '" + where + "'"
    print(sql)
    cursor.execute(sql)
    connection.commit()
    connection.close()


# if __name__ == "__main__":
#     emails = select('emails', 'email', limit=' LIMIT 1 ', order='')
#     email = emails[0]['email']
#     print(email)
#     update('emails', 'email', email, 'used', '1')







