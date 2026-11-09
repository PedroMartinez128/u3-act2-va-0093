import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Declaración de las listas con los datos del Problema 8: Dispositivos
# [Modelo, precio USD, incluye control remoto, memoria RAM GB]
chr = ['Chromecast HD', 29.99, True, 1.5]
frt = ['Fire TV Stick 4K', 49.99, True, 2.0]
rku = ['Roku Express', 24.99, True, 1.0]
app = ['Apple TV 4K', 129.00, True, 4.0]
nvd = ['Nvidia Shield', 199.99, True, 3.0]

# Matriz / Lista de listas
lista_dispositivos = [chr, frt, rku, app, nvd]

# Creación del DataFrame con los nuevos nombres de columnas
df_dispositivos = pd.DataFrame(lista_dispositivos,
                               columns=["Modelo", "Precio_USD", "Incluye_Control", "RAM_GB"])

print(df_dispositivos)

# Crear archivo CSV (Opcional)
df_dispositivos.to_csv("Dispositivos.csv", index=False)

# 1. Gráfica de líneas (Modelo vs Precio)
plt.plot(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
plt.title("Gráfica Dispositivos 0093")
plt.xlabel("Modelo del dispositivo")
plt.ylabel("Precio (USD)")
plt.show()

# 2. Gráfica de puntos
plt.scatter(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
plt.title("Gráfica Dispositivos 0093")
plt.xlabel("Modelo del dispositivo")
plt.ylabel("Precio (USD)")
plt.show()


# 3. Gráfica de barras
plt.bar(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
plt.title("Dispositivos 0093")
plt.xlabel("Dispositivos")
plt.ylabel("Precio (USD)")
plt.show()

# 4. Gráfica de barras ordenada de manera descendente (del precio más alto al más bajo)
df_disp_ordenado = df_dispositivos.sort_values("Precio_USD", ascending=False)
plt.bar(df_disp_ordenado["Modelo"], df_disp_ordenado["Precio_USD"])
plt.title("Gráfica Dispositivos 0093")
plt.xlabel("Modelo del dispositivo")
plt.ylabel("Precio (USD)")
plt.show()

# 5. Coloreando la gráfica de barras ordenada
df_disp_ordenado = df_dispositivos.sort_values("Precio_USD", ascending=False)
plt.bar(df_disp_ordenado["Modelo"], df_disp_ordenado["Precio_USD"],
        color=["b", "g", "c", "m", "y"])
plt.title("Gráfica Dispositivos 0093")
plt.xlabel("Modelo del dispositivo")
plt.ylabel("Precio (USD)")
plt.show()

# 6. Gráfica pastel (Distribución del precio)
plt.pie(df_dispositivos["Precio_USD"],
        labels=df_dispositivos["Modelo"])
plt.title("Gráfica Dispositivos 0093")
plt.xlabel("Modelo del dispositivo")
plt.ylabel("Precio (USD)")
plt.show()