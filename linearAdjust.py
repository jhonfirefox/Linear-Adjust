##########Ajuste Lineal de los datos##########
import numpy as np

def linAdj(x_exp,y_exp,n):
	#calculo de la pendiente y el intercepto
	if n != x_exp.size:
		print("Los datos no tienen el tamaño de: ", n)
		n = x_exp.size
		print("Se ajusta el valor de n: ", n)
	
	pend = (n*sum(x_exp*y_exp)-sum(x_exp)*sum(y_exp))/(n*sum(x_exp**2) - sum(x_exp)**2)
	inter = (sum(x_exp**2)*sum(y_exp) - sum(x_exp)*sum(x_exp*y_exp))/(n*sum(x_exp**2) - sum(x_exp)**2)

	#calculo de la desviacion estandar en Y
	dy=y_exp -(pend*x_exp+inter)
	Dy = np.sqrt(sum(dy**2)/(n-2))

	#calculo del error en la pendiente
	Dm = Dy*np.sqrt(n/(n*sum(x_exp**2) -sum(x_exp)**2));

	#calculo del error en el intercepto
	Db = Dy/np.sqrt(n);

	#Coeficiente de correlacion lineal
	r1 = (n*sum(x_exp*y_exp)-sum(x_exp)*sum(y_exp));
	r2 = np.sqrt((n*sum(x_exp**2)-sum(x_exp)**2)*(n*sum(y_exp**2)-sum(y_exp)**2));
	r = r1/r2;
	
	return pend, inter, Dm, Db, r, Dy
	#%r = (n*sum(x.*y)-sum(x)*sum(y))/sqrt((n*sum(x.*x)-sum(x)^2)(n*sum(y.*y)-sum(y)^2));
##########Ajuste Lineal de los datos##########

if __name__ == "__main__":
	#a litte demo of how works the function
	print("Este modulo devuelve el ajuste lineal de un conjunto de datos")
	print("El orden de entrega de parametros es el siguiente: ")
	print("(vector X, Vector Y, n:tamaño de los vectores)")
	print("Los datos de regreso son: ")
	print("(pendiente, intercepto, Error-pendiente, Error-intercepto, r^2, Error-Y)")