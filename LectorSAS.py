

#Importar librerias
import time
import datetime
import os
import sys
from pathlib import Path
from pyduino import Arduino
from pathlib import Path

a=Arduino("COM11")
#Creacion de fecha actual. Para el nombre del programa.
now=datetime.datetime.now()

nombre= os.path.dirname(os.path.abspath(sys.argv[0]))+"\Trama"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"--"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+".txt"
f=open(nombre,"w")
time.sleep(1)


try:
	while True:
		linea="" 
		for i in range(30):
			time.sleep(0.01)
			linea=str(a.digital_read("10"))+linea
		f.write(linea+"\n")
		
except KeyboardInterrupt: 

	f.close()
	pass