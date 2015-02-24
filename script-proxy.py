import sys

opcion = sys.argv[1]
tipo = sys.argv[2]
contenido = sys.argv[3]

if opcion == "-a":
	if tipo == "-url":
		fichero = open("etc/squid3/urlnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
	elif tipo == "-dom":
		fichero.open("/etc/squid3/domnegro.acl","a")
		fichero.write(contenido+"\n")
		fichero.close
elif opcion == "-d":
	if tipo == "-url":
		fichero = open("/etc/squid3/urlnegro.acl","a")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			# if linea.find(contenido) == 0:
			# 	fichero.open("etc/squid3/urlnegro","w")
			# 	lineas.remove(linea)
				#Falta borrar
	elif tipo == "-dom":
		fichero = open("/etc/squid/domnegro.acl","r")
		lineas = fichero.readlines()
		fichero.close
		for linea in lineas:
			#Borrar dominio
