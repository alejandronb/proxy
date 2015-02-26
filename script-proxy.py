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
			if linea == contenido:
				fichero = open("/etc/squid3/urlnegro","w")
				lineas.remove(contenido)
				for linea in lineas:
					fichero.write(linea)
				fichero.close
				#Comprobar funcionamiento
	elif tipo == "-dom":
		fichero = open("/etc/squid3/domnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			if linea.find(contenido) == 0:
				linea = ""
				fichero = open("/etc/squid3/domnegro","w")
				for linea in lineas:
					fichero.write(linea)
				fichero.close








	# elif tipo == "-dom":
	# 	fichero = open("/etc/squid3/domnegro.acl","r")
	# 	lineas = fichero.readlines()
	# 	fichero.close
	# 	for linea in lineas:
	# 		if linea == contenido:
	# 			lineas.remove(contenido)
	# 			fichero = open("/etc/squid3/domnegro","w")
	# 			for linea in lineas:
	# 				fichero.write(linea)
	# 			fichero.close