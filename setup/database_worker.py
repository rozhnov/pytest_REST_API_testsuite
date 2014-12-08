__author__ = 's.lugovskiy'
import pymysql


def connect(dbhost='10.8.0.229', dbport=3306, dbuser='root', dbpasswd='123456', dbname='monitoring'):
    conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbname)
    cur = conn.cursor()
    return cur