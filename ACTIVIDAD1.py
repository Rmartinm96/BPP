#APARTADO1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tabla = pd.read_csv('finanzas2020.csv',sep = '\t')
df = pd.DataFrame(tabla)

ingresos = 0
gastos = 0
ingresos_mes = []
gastos_mes = []
suma = 0
balance = []
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#Comprobación para datos correctos
for j in range((df.columns.get_loc('Diciembre'))+1):
    for i in range(len(df)):
        valor = df.iloc[i,j]
        try: 
            valor = int(df.iloc[i,j])
        except ValueError:
            valor = 0    
        else:
            if valor >= 0:
                ingresos = ingresos + valor
                suma = suma + valor
            else:
                gastos = gastos + valor
                suma = suma + valor
    ingresos_mes.append(ingresos)
    gastos_mes.append(gastos)
    balance.append(suma)
    suma = 0
    gastos = 0
    ingresos = 0 


#Mes que más se ha gastado
for z in range(len(gastos_mes)):
    if gastos_mes[z] == min(gastos_mes):
        print("El mes en el que más se ha gastado es",meses[z])
#Mes que más se ha ahorrado
for t in range(len(balance)):
    if balance[t] == max(balance):
        print("El mes en el que más se ha ahorrado es",meses[t])

#Media de gastos al año
media = abs(sum(gastos_mes))/len(gastos_mes)
print("La media de gastos al año es",abs(media))

#Gasto total durante el año
print("Gasto total en el año:",abs(sum(gastos_mes)))

#Ingresos totales durante el año
print("Ingresos totales en el año:",abs(sum(ingresos_mes)))

#Gráfica ingresos por mes
eje_x = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
eje_y = ingresos_mes

plt.barh(eje_x, eje_y, color="green")
plt.xlabel('Meses')
plt.ylabel('Ingresos')
plt.title('Ingresos por mes en 2020')
try:
    plt.show()
except:
    print("No muestra nada")


#APARTADO 2

#Comprobación de que el fichero existe,que tiene 12 columnas y que para cada mes hay contenido   
try:
    fichero = open("finanzas2020.csv","r")
    lines = fichero.readlines()
    meses = lines[0].split(sep = '\t')
    print(lines)
except IOError:
    print("No encuentro el fichero o no puedo leerlo")
else:
    print("Hay",len(meses),"columnas en el fichero")
    print("He leído el fichero sin problemas.Lo cierro y termino")
    fichero.close()
