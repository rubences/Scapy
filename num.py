#!/usr/bin/python
#-*- coding: utf-8 -*-
nbr=raw_input("introduzca un número>")
while not nbr.isdigit():
	print "Por favor, introduzca un número"
	nbr=raw_input("introduzca un número>")
nbr=int(nbr)
if nbr<10:
	print "ha introducido un número inferior a 10"
elif 10<= nbr <= 20:
	print "ha introducido un número comprendido entre 10 y 20"
else:
	print "su número es mayor que 20"
