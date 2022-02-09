#!/usr/bin/python
#-*- coding: utf-8 -*-
import MySQLdb
vinculo_db=MySQLdb.connect(host= "localhost", user="root",passwd="", db="python_db")
vinculo_db.query("SELECT * FROM USER")
resultado= vinculo_db.store_result()
nb_tupla=resultado.num_rows()
while nb_tupla>0:
	linea=resultado.fetch_row()
 	print(linea)
 	nb_tupla=nb_tupla - 1
