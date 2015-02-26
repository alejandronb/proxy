import sys

opcion = sys.argv[1]
tipo = sys.argv[2]
contenido = sys.argv[3]

if opcion == "-a":
	if tipo == "-url":
		fichero = open("/etc/squid3/urlnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
	elif tipo == "-dom":
		fichero.open("/etc/squid3/domnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
elif opcion == "-d":
	if tipo == "-url":
		fichero = open("/etc/squid3/urlnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			if linea == contenido:
				fichero.open("/etc/squid3/urlnegro","w")
				lineas.remove(contenido)
				for linea in lineas:
					fichero.write(linea)
				fichero.close
				#Comprobar funcionamiento
	elif tipo == "-dom":
		fichero = open("/etc/squid/domnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			if linea == contenido:
				fichero.open("/etc/squid3/domnegro","w")
				lineas.remove(contenido)
				for linea in lineas:
					fichero.write(linea)
				fichero.close