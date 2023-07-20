#importacion de modulos necesarios
import pandas as pd
import matplotlib.pyplot as plt
import easygui

# Leer el archivo Excel
msg = "Selecciona tu archivo excel"
print(msg)
seleccion = easygui.fileopenbox()
df = pd.read_excel(seleccion)
#buscar la tabla
data = input("Ingresa el nombre de la tabla: ")
data2 = df[[data]]
label = input("Como quieres que se  llame el Histrograma: ")
#generar el histograma con la cantidad de datos repetidos del excel
plt.hist(data2, bins=11, edgecolor="black")
plt.xlabel(label)
plt.title("Histograma")
plt.show()


# Leer el archivo Excel
#buscar con la tabla
print("Creacion de Grafico de pie ")
data = input("Ingresa el nombre de la tabla: ")
data2 = df[[data]]
#numeros posibles
input_string = input("ingrese sus valores con espacios: ")
lista = input_string.split()
labels = list(lista)
#contar los datos repetidos
conteo = data2.value_counts()
#generar el grafico de pie
plt.pie(conteo, labels=labels, autopct=("%0.1f %%"))
plt.axis("equal")
plt.show()

