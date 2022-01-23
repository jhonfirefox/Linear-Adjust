#Programa para realizar un ajsute lineal en python
import numpy as np
import matplotlib.pyplot as plt

#Funcion para convertir string a float, devueve un lista np
def str2float(lst):
	return np.array([float(i) for i in lst])

#Se pide el nombre de archivo 
print("Nombre de archivo de los datos con extension: ", end="")
name = str(input())
print("Delimitador de campo: ", end="")
delimiter = str(input())
print("# de linea de inicio de datos: ", end="")
sLine = int(input())

fileData = np.loadtxt(name,dtype=str, delimiter=delimiter, skiprows = sLine)

#x_exp = np.array([float(i) for i in fileData[:,0]])
#y_exp = np.array([float(i) for i in fileData[:,1]])
x_exp = str2float(fileData[:,0])
y_exp = str2float(fileData[:,1])
n = x_exp.size

##########Ajuste Lineal de los datos##########
#calculo de la pendiente y el intercepto
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
#%r = (n*sum(x.*y)-sum(x)*sum(y))/sqrt((n*sum(x.*x)-sum(x)^2)(n*sum(y.*y)-sum(y)^2));
##########Ajuste Lineal de los datos##########

print("##########Ajuste Lineal de los datos##########")
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
plt.figure()
plt.plot(x_exp,y_exp,"bo", label="Exp. Data")
plt.plot(x_teo,y_teo,"r--", label="Linear Adjust")
plt.xlabel("x Data")
plt.ylabel("y Data")
plt.title("Linear Adjust")
plt.legend()
plt.savefig("linearAdjust.png")
plt.show()

#Se leen los datos en el archivo de texto
