%Programa para realizar un ajuste lineal
%por minimos cuadrados
clear all; close all; clc;

%graphics_toolkit ("qt")
graphics_toolkit ("gnuplot")
%graphics_toolkit ("fltk")

% Operaciones de lectura del fichero
#args = argv(); #Funcion para pasar parametros por programa
#printf ("Nombre de archivo CSV: %s\n", args{1});
#printf("Nombre de archivo (.csv): ")
name = input("Nombre de archivo (.csv): ", "s")
delimiter = input("delimitador de campo (';'): ", "s")

if (delimiter == '')
	delimiter = ';';
endif
#name = args{1};
#if (args{1} )
#nameF = "caidaLibre.csv"

file = fopen(name, 'r');
m=textscan(file, '%f %f', 'delimiter', delimitador);
x = transpose(m{1});
y = transpose(m{2});
n = length(x);

%calculo de la pendiente y el intercepto
pend = (n*sum(x.*y)-sum(x)*sum(y))/(n*sum(x.^2) - sum(x)^2);
inter = (sum(x.^2)*sum(y) - sum(x)*sum(x.*y))/(n*sum(x.^2) - sum(x)^2);

%calculo de la desviacion estandar en Y
dy=y -(pend*x+inter);
Dy = sqrt(sum(dy.^2)/(n-2));

%calculo del error en la pendiente
Dm = Dy*sqrt(n/(n*sum(x.^2) -sum(x)^2));

%calculo del error en el intercepto
Db = Dy/sqrt(n);

%Coeficiente de correlacion lineal
r1 = (n*sum(x.*y)-sum(x)*sum(y));
r2 = sqrt((n*sum(x.*x)-sum(x)^2)*(n*sum(y.*y)-sum(y)^2));
r = r1/r2;
%r = (n*sum(x.*y)-sum(x)*sum(y))/sqrt((n*sum(x.*x)-sum(x)^2)(n*sum(y.*y)-sum(y)^2));

printf("=============Datos de Ajuste Lineal=============\n")
printf("pendiente: %0.9f\n", pend)
printf("intercepto: %0.9f\n", inter)
printf("maximo error en Dy: %0.9f\n", Dy)
printf("error en Pendiente: %0.9f\n",Dm)
printf("error en intercepto: %0.9f\n",Db)
printf("Coeficiente de Correlacion Lineal (R^2): %0.5f\n",r)
printf("================================================\n")

hold on
%Grafica de los datos experimentales
figure(1)
plot(x,y,'r*')
%grafica de los datos de ajuste
x1=linspace(min(x),max(x),100*n);
y1=pend*x1+inter;
plot(x1,y1,'k-')

xlabel('x(s)')
ylabel('y(m^0.5)')
title('Ajuste Lineal x(s) vs y(m^0.5)')
legend("Datos Experimentales","Ajsute lineal")
grid("on")
print -djpg figure1.jpg
#hold off

fclose(file);
