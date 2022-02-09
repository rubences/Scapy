#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
vinculo_db=MySQLdb.connect(host="localhost", user="root",
passwd="", db="python_db")
peticion="insert into USER(PSEUDO) VALUE('Roberto')"
vinculo_db.query(peticion)
vinculo_db.commit()
peticion="SELECT * from USER"
vinculo_db.query(peticion)
resultado= vinculo_db.store_result()
nb_tupla=resultado.num_rows()
for l in resultado.fetch_row(maxrows=nb_tupla,how=1):
	print(l["id"],l["PSEUDO"])
vinculo_db.close()
