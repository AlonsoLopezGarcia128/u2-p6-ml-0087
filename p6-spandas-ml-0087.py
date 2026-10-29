# Alonso Lopez Garcia NC = 0087 | Fecha 29/10/2026
import pandas as pd
import numpy as np
serie_amigos = ["Matias", "Andres", "Pedro", "Catherine", "Arriaga", "Valeria", "Luis"]
print(" ---- Serie listado de amigos ---- NC = 0087")
amigos = pd.Series(serie_amigos)
print(amigos)

print(" ")
serie_billetes = [20, 50, 100, 200, 500, 1000]
print(" ---- Serie listado valor de billetes ---- NC = 0087")
billetes = pd.Series(serie_billetes)
print(billetes)

print(" ")
serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_bletras = ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
print(" ---- Serie listado nombre y valor de billetes MX ---- NC = 0087")
tabla_billetes = pd.Series(serie_billetes, serie_bletras)
print(tabla_billetes)

# Diccionario DataFrame 
# Diccionario de valor monedas y nombre
print(" ")
print("Datos de diccionario a dataframe en pandas")
dic_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000],
    "serie_bletras":["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
}
tabla_billetes = pd.DataFrame(dic_monedas, index = ["A", "B", "C", "D", "E", "F"])
print(tabla_billetes)

print(" ")
print("Casa de Cambio Alonso Lopez Garcia NC = 0087")

