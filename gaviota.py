from vpython import *
import numpy as np
'''Datos del problema
******
La fuerza es perpendicular a la superficie de las alas extendidas de la gaviota. 
Su magnitud depende de varios factores pero esencialmente es proporcional al cuadrado de la rapidez |L| = kv^2,
donde k es una constante de propporcionalidad que asumiremos fija y conocida.

a) La gaviota, cuya masa es conocida e igual a m, desea surcar, a una altura H, 
una trayectoria circular horizontal de radio R a velocidad angular constante.

	I) ¿Que valor debe tomar la inclinacion, Beta, de la gaviota?, Beta, 
	es el angulo definido desde la vertical hasta la normal al plano de las alas de la gaviota.
	II) Determine el valor necesario al cual la gaviota debe mantener la velodicidad angular

b) Para lanzarse al mar, la gaviota inicia un descenso en forma de helice. 
ie. el radio R y la velocidad angular siguen siendo constantes pero la gaviota 
adquiere ademas una velocidad vertical constante, dz, en direccion hacia el mar

	I) si conocemos R y dz, ¿ Que valor debe tomar la velocidad angular?
	II) Determine la inclinacion (Beta) de la gaviota necesaria para esta trayectoria
	
*******

radio : r
angulo azimutal : omega
angulo entre cilindro y tangente : beta
velocidad en el eje z : v_z
tiempo : dt
'''

r = 2
omega = 5
dt = np.linspace(0,10,1001)
v_z = 0.5
beta = np.pi/4

''' Ajustes pantalla '''
scene.title = "<b>A bird is flying</b></n>"
scene.width = 640
scene.height = 600
scene.forward = vector(0,-.3,-1)

''' Ajustes boceto '''
gaviota = sphere(pos=vector(r,0,0), radius=r/10, color=color.cyan,
		make_trail=True, interval=1)

#Vectores unitarios
x_i = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_j = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_k = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)

#Vectores de trayectoria con sus respectivas letras
rarr = arrow(pos=gaviota.pos, axis=vector(1,0,0), color=color.magenta, shaftwidth=0.05)
txt_rarr = text(text='n', pos=rarr.pos+rarr.axis, axis=rarr.axis, align='center', height=0.4,
          color=color.magenta, billboard=True, emissive=True)

tarr = arrow(pos=gaviota.pos, axis=vector(0,1,0), color=color.white, shaftwidth=0.05)
txt_tarr = text(text='t', pos=tarr.pos+tarr.axis, axis=tarr.axis, align='center', height=0.4,
          color=color.white, billboard=True, emissive=True)

Larr = arrow(pos=gaviota.pos, axis=np.sin(beta)*rarr.axis+np.cos(beta)*z_k.axis, shaftwidth=0.05,
			color=color.orange)
txt_Larr = text(text='L', pos=Larr.pos+Larr.axis, axis=Larr.axis, align='center', height=0.4,
          color=color.orange, billboard=True, emissive=True)

scene.autoscale = True

# aqui escribimos la descripcion del video
scene.append_to_caption("""Una gaviota puede planear, a pesar de la gravedad,
gracias a una fuerza de origen aerodinamico, conocida como fuerza de sustentacion, L.
El movimiento es descrito en esta representacion visual""")


while True:
	for this_t in dt:
		'''Actualiza la posicion de la gaviota
		y la direccion de los vectores unitarios r, theta'''
		rate(60)  # Espera 1/60 s para que no se vea tan rapido
		theta = omega*this_t

		# actualiza la direccion de r y theta
		rarr.axis = vector(np.cos(theta),np.sin(theta),0)
		tarr.axis = vector(-np.sin(theta), np.cos(theta), 0)
		Larr.axis = -np.sin(beta)*rarr.axis + np.cos(beta)*z_k.axis	

		# actualiza la direccion de r, theta y la gaviota
		Larr.pos = rarr.pos = tarr.pos = gaviota.pos = vector(r*np.cos(theta), r*np.sin(theta),
			v_z*this_t)
			
		#generamos las letras
		txt_rarr.pos = rarr.pos+rarr.axis
		txt_tarr.pos = tarr.pos+tarr.axis
		txt_Larr.pos = Larr.pos+Larr.axis
	res = input('Press any key to reset')
