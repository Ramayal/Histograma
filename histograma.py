import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo Excel
df = pd.read_excel('C:\\Users\\Ramayal\\desktop\\Nueva carpeta\\Propiedades_Precios.xlsx')


# Verificar duplicados en una sola columna
duplicados = df.duplicated(subset=['id casa'])
filas_duplicadas = df[duplicados]



# Definir los límites del rango deseado
valor_minimo = 1
valor_maximo = 5

# Filtrar los valores fuera de rango en la columna específica
valores_fuera_de_rango = df.loc[(df['nro_banos'] < valor_minimo) | (df['nro_banos'] > valor_maximo)]

print(valores_fuera_de_rango)



print(filas_duplicadas)
