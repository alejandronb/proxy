# -*- coding: utf-8 -*-
import sys

opcion = sys.argv[1]
tipo = sys.argv[2]
contenido = sys.argv[3]

if opcion == "-a":
	if tipo == "-url":
		fichero = open("/etc/squid3/urlnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
		print "La url se ha añadido"
	elif tipo == "-dom":
		fichero = open("/etc/squid3/domnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
		print "El dominio se ha añadido"
elif opcion == "-d":
	if tipo == "-url":
		fichero = open("/etc/squid3/urlnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			if linea == contenido+"\n":
				fichero = open("/etc/squid3/urlnegro.acl","w")
				lineas.remove(contenido+"\n")
				for linea in lineas:
					fichero.write(linea)
				fichero.close
				print "La url se ha borrado"
	elif tipo == "-dom":
		fichero = open("/etc/squid3/domnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			if linea == contenido+"\n":
				lineas.remove(contenido+"\n")
				fichero = open("/etc/squid3/domnegro.acl","w")
				for linea in lineas:
					fichero.write(linea)
				fichero.close
				print "El dominio se ha borrado"