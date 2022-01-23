#Programa para realizar un ajsute lineal en python
import numpy as np
import matplotlib.pyplot as plt
import linearAdjust as la
import random as rand
import time as tm

def str2float(lst):
	return np.array([float(i) for i in lst])

#Se pide el nombre de archivo 
print("Nombre de archivo de los datos con extension: ", end="")
name = str(input())
print("Delimitador de campo: ", end="")
delimiter = str(input())
print("# de linea de inicio de datos: ", end="")
sLine = int(input())
print("# de ajustes lineales a realizar: ", end="")
numAjus = int(input())

fileData = np.loadtxt(name,dtype=str, delimiter=delimiter, skiprows = sLine)

plt.figure()
rand.seed(tm.time())
for i in range(0,2*numAjus-1,2):
	x_exp = str2float(fileData[:,i])
	y_exp = str2float(fileData[:,i+1])
	n = x_exp.size

	##########Ajuste Lineal de los datos##########
	(pend, inter, Dm, Db, r, Dy) = la.linAdj(x_exp,y_exp,n)
	##########Ajuste Lineal de los datos##########

	print("##########Ajuste Lineal de los datos##########")
	print("Asjute lineal #: ", i)
	print("pendiente: ", pend)
	print("intercepto: ", inter)
	print("maximo error en Dy: ", Dy)
	print("error en Pendiente: ",Dm)
	print("error en intercepto: ",Db)
	print("Coeficiente de Correlacion Lineal (R^2): ",r)
	print("##############################################")

	x_teo = np.linspace(x_exp[0], x_exp[n-1], n*100)
	y_teo = pend*x_teo + inter

	#print("Datos en x: %f", x_exp)
	#print("Datos en y: %f", y_exp)
	r = rand.random()
	b = rand.random()
	g = rand.random()
	color = (r, g, b)

	plt.plot(x_exp,y_exp,"o", label="Exp. Data - " + str(i/2+1),color = color)
	plt.plot(x_teo,y_teo,"--", label="Linear Adjust - "+str(i/2 + 1), color = color)
	
plt.xlabel("x Data")
plt.ylabel("y Data")
plt.title("Linear Adjust")
plt.legend()
plt.savefig("linearAdjust.png")
plt.show()

#Se leen los datos en el archivo de texto
