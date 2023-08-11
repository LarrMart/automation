#!/usr/bin/env python

n = ""
while (not type(n) is int):
	try:
		n = int(input("Ingrese un número: "))
	except(ValueError):
		print("Hubo un error, ingrese el número nuevamente.")

print("Ok")
