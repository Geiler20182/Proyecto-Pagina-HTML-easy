#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request

app= Flask(__name__)
f = []
online=''

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	"""
	FUNCION LOGIN :

	¿QUE HACE? FUNCION PARA QUE UN USUARIO REGISTRADO PUEDE INGRESAR

	¿QUE LE INGRESA? INGRESA UN USUARIO Y UNA CONTRASEÑA; SI EL USUARIO Y LA CONTRASEÑA 
	SE ENCUENTRAN EN LA BASE DE DATOS Y EN LA MISMA POSICION (INDICE)( ARCHIVOS PLANOS) , QUE EN ESTE CASO SON DOS, UNO PARA 
	ALMACENAR EL USUARIO Y OTRO PARA ALMACENAR LA CONTRASEÑA, ESTE RETORNA LA PAGINA PRINCIPAL
	"""
	global online
	if request.method=='POST':
	
		user=request.form['user'] #ALMACENA EN UNA VARIABLE EL USUARIO QUE ESINGRESADO DESDE EL HTML(INPUT)
		password=request.form['password']#ALMACENA EN UNA VARIABLE EL USUARIO QUE ESINGRESADO DESDE EL HTML(INPUT)
		users=open("user", mode="r")#ABRE EL ARCHIVO PLANO "user" Y LO LEE
		passwords=open("contraseñas", mode="r")#ABRE EL ARCHIVO PLANO "contraseña"
		users1=users.readlines() #OBTIENE UNA LISTA CON LINEAS
		pass1=passwords.readlines() #LEE EL ARCHIV
		online+=user
		
		"""
		ALGORITMO

		¿QUE HACE? ALGORITMO PARA LEER Y VERIFICAR QUE EL USUARIO Y LA CONTRASEÑA QUE 
				   INGRESADOS SEAN LOS CORRECTOS Y ESTEN EN EL MISMO INDICE EN CADA 
				   ARCHIVO PLANO ("user" y "contraseñas")
		
		¿QUE LE INGRESA? LOS DATOS ALMACENADOS EN LAS VARIABLES "user" y "password"

		"""
		for i in users1: 
			for y in pass1:
				x=i.split() #LA CADENA DE TEXTO LA DIVIDE EN VARIAS PARTES
				k=y.split() 
				i=0
				while i <len(x):
					if x[i]==user and k[i]==password: 
						return render_template('home.html')
					i+=1


		users.close()
		passwords.close()
		return render_template('index.html')
	
@app.route('/registro', methods=['POST'])
def registro():
   """
   FUNCION REGISTRO

   ¿QUE HACE? ALMACENA DATOS INGRESADOS POR UN USUARIO EN ARCHIVOS PLANOS

   ¿QUE LE INGRESA? NOMBRE, USUARIO, CONTRASEÑA Y TELEFONO
   """
   if request.method=='POST':
      users=request.form['user'] 
      
      user=open("user", mode="a") #ABRE EL ARCHIVO PLANO PARA ESCRIBIR
      user.write(users)
      user.write(' ')
      user.close()
      password=request.form['password']
      passwords=open("contraseñas", mode="a")
      passwords.write(password)
      passwords.write(' ')

      x='datos'+users
      name=request.form['name']
      phone=request.form['phone']
      datos=open(x, mode="a")
      datos.write(' ')
      datos.write(' ')
      datos.write(name)
      datos.write(' ')
      datos.write(phone)
      datos.write(' ')

      datos.close()
      passwords.close()

   return render_template('index.html')

def conversionHora(hora_act):

	"""
	FUNCION CONVERSION HORA

	¿QUE HACE? COLOCA DOS PUNTOS A LA HORA DE UN VUELO
			   PARA QUE QUEDE BIEN ESPECIFICADO 
	"""
	parte_izq = ''
	parte_der = ''

	i = 0
	j = 2
	while(i < 2):
	    parte_izq += hora_act[i] 
	    parte_der += hora_act[j]
	    i += 1
	    j += 1

	hora_nueva = parte_izq+':'+parte_der
	return hora_nueva.strip()

@app.route('/reserva', methods=['POST'])
def reserva():
   """
   FUNCION PARA RESERVAR UN VUELO
   ¿QUE HACE? BUSCA EN  EL ARCHIVO "datos", DONDE SE ENCUENTRA TODA LA INFORMACION DE LOS VUELOS
   LOS DATOS SELECCIONADOS POR EL USUARIOS (Origen, Destino y aerolinea )

   """
   global f
   if request.method=='POST':
      global j
      x=open("vuelos", mode="r+") #ABRE E ARCHIVO PLANO EN MODO LECTURA Y ESCRITURA
      j=[] 
      print("aqui1")
      y=x.readlines()[59:]
      """
   DICCIONARIO PARA VER  EL CLAVE DEL VALOR INGRESADO Y VICEVERSA
   """
   #aerolineas={'DL':'Delta Airlines','AA':'American Airlines','US':'US Airways','CO':'Copa Airlines','WN':'Wright Air','TW':'Tradewind Aviation','YV':'Travel Air','HP':'Hawaiian Airlines','NW':'Norwegian','UA':'United Airlines','PA':'Pacific Airways','QF':'Qatar Airways','YX':'West Jet','ZK':'KLM Airlines','AD':'Air France','4X':'40-Mile Air','MG':'Mokulele Airlines','AS':'Alaska Seaplane','FF':'Frontier 
   ciudades = {'Albuquerque, New Mexico':'ABQ','Atlanta, Georgia':'ATL','Nashville, Tennessee':'BNA',
              'Boston, Massachusetts':'BOS','Washington D.C.':'DCA','Denver, Colorado':'DEN','Dallas, Texas':'DEN',
              'Detroit, Michigan':'DTW','Houston, Texas':'HOU','New York':'JFK','Los Angeles, California':'LAX',
              'Miami, Florida':'MIA','Minneapolis, Minnesota':'MSP','New Orleans, Louisiana':'MSY',
              'Chicago, Illinois':'ORD','Providence/Newport, Rhode Island':'PVD','Philadelphia, Pennsilvania':'PHL',
              'Phoenix, Arizona':'PHX','Raleigh/Durham, North Carolina':'RDU','Seattle/Tacoma, Washington':'SEA',
              'San Francisco, California':'SFO','St Louis, Missouri':'STL','Tampa, Florida':'TPA'}
   aerolinea = {'DL':'Delta Airlines','AA':'American Airlines',
                'US':'US Airways','CO':'Copa Airlines','WN':'Wright Air',
                'TW':'Tradewind Aviation','YV':'Travel Air','HP':'Hawaiian Airlines',
                'NW':'Norwegian','UA':'United Airlines','PA':'Pacific Airways','QF':'Qatar Airways',
                'YX':'West Jet','ZK':'KLM Airlines','AD':'Air France','4X':'40-Mile Air',
                'MG':'Mokulele Airlines','AS':'Alaska Seaplane','FF':'Frontier Airlines'}

   aerolinea2 = {'Delta Airlines':'DL','American Airlines':'AA',
                'US Airways':'US','Copa Airlines':'CO','Wright Air':'WN',
                'Tradewind Aviation':'TW','Travel Air':'YV','Hawaiian Airlines':'HP',
                'Norwegian':'NW','United Airlines':'UA','Pacific Airways':'PA','Qatar Airways':'QF',
                'West Jet':'YX','KLM Airlines':'ZK','Air France':'AD','40-Mile Air':'4X',
                'Mokulele Airlines':'MG','Alaska Seaplane':'AS','Frontier Airlines':'FF'}

   origen=ciudades[request.form['origen']]
   destino=ciudades[request.form['destino']]
   aerolineaa=aerolinea2[request.form['aerolinea']]
   conversion_meridiano = {'P':'PM','A':'AM'}
   print("aqui2")

   #ALGORITMO PARA VERIFICAR SI EXISTE UN ORIGEN, DESTINO Y AEROLINEAS EN LA BASE DE DATOS, 
   #PARA ALAMCENARLOS EN UNA LISTA

   for line in y:
      print(line)
      if(line[0:2]==aerolineaa and line[8:11] ==origen and line[19:22]==destino):
         j+={line[0:44]}	
      #ALGORITMO PARA VER TODAS LAS AEROLINEAS DISPONIBLES PARA LA RESERVA
   for i in range(0,len(j)):
      f +=[ {'aereolinea':aerolinea[j[i][0:2]],
                'vuelo':j[i][2:6].replace(' ',''),
                'ciudad_origen':j[i][8:11],
                'hora_salida':conversionHora(j[i][12:16]),
                'meridiano_salida':conversion_meridiano[j[i][16]],
                'ciudad_destino':j[i][19:22],
                'hora_llegada':conversionHora(j[i][23:27]),
                'meridiano_llegada':conversion_meridiano[j[i][27]],
                'paradas':j[i][36],
                'areonave':j[i][41:44]}]

   if (f != []):
      print("aqui4")  
      print(f)
      
      return render_template('reserDis.html',vuelos=f)
   else:
      return render_template ('reservas.html')
   print("aqui5")

   x.close()	       	
"""
FUNCIONES PARA REDIRECCIONAR A DIFERENTES PAGINAS CON LAS OPCIONES DE LA PARTE SUPERIOR DE LA PAGINA
 
"""
@app.route('/reservas', methods=['POST'])
def reservas():
	global f
	f = []
	if request.method=='POST':
		return render_template('reservas.html')
@app.route('/historial', methods=['POST'])
def historial():
		return render_template('historial.html')
@app.route('/contacto', methods=['POST'])
def contacto():
	if request.method=='POST':
		return render_template('contacto.html')
@app.route('/inicio', methods=['POST'])
def inicio():
	if request.method=='POST':
		return render_template('index.html')


@app.route('/solicitar_reserva', methods=['POST'])
def solicitar_reserva():
	"""
	FUNCION PARA RESERVAR UN VUELO

	¿QUE HACE? RESERVA UN VUELO Y LO ALMACENA EN UN ARCHIVO PLANO 
	"""
	global f, online

	x=('reservas'+online)

	HistorialVuelos=open(x,"a") #ABRE LA EL ARCHIVO PLANO "solicitudReserva"
	vuelo_reserva = {}
	id_vuelo = ''
	if request.method=='POST':
		
		id_vuelo = request.form['id_vuelo']
		print(id_vuelo)
		for i in f:
			if(i["vuelo"] == id_vuelo):
				vuelo_reserva = i
				print(vuelo_reserva)
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Origen: ')
				HistorialVuelos.write(vuelo_reserva['ciudad_origen'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Destino: ')
				HistorialVuelos.write(vuelo_reserva['ciudad_destino'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Aerolinea: ')
				HistorialVuelos.write(vuelo_reserva['aereolinea'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Hora de salida: ')
				HistorialVuelos.write(vuelo_reserva['hora_salida'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Aeronave: ')
				HistorialVuelos.write(vuelo_reserva['areonave'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Tipo de hora: ')
				HistorialVuelos.write(vuelo_reserva['meridiano_llegada'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Paradas:')
				HistorialVuelos.write(vuelo_reserva['paradas'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Hora de llegada')
				HistorialVuelos.write(vuelo_reserva['hora_llegada'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Tipo de hora de llegada: ')
				HistorialVuelos.write(vuelo_reserva['meridiano_llegada'])
				HistorialVuelos.write(' ')
				HistorialVuelos.write('Vuelo:')
				HistorialVuelos.write(vuelo_reserva['vuelo'])
				HistorialVuelos.write(' ')


   					
	return render_template('historial.html', vuelos=f)

if __name__ == '__main__':
   app.run(debug=True, port=8000)
