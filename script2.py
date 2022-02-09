#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
vinculo_db=MySQLdb.connect(host="localhost", user="root",
passwd="", db="python_db")
vinculo_db.query("SELECT * FROM USER")
resultado= vinculo_db.store_result()
nb_tupla=resultado.num_rows()
linea=resultado.fetch_row(maxrows=nb_tupla,how=1)
print(linea)
