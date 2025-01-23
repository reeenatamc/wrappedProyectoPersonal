import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os #interactuar con el sistema operativo

carpeta_archivos = r"C:/Users/LENOVO/Documents/GitHub/wrappedProyectoPersonal/codigo-archivos"

all_data = [] # arreglo para guardar los archivos

for filename in os.listdir(carpeta_archivos):
    if filename.endswith(".json"):
        file_path = os.path.join(carpeta_archivos, filename) #solo hace una ruta y por lo tanto asegura que sea valida
        
        # Leer el contenido del archivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_data.extend(data)  


df = pd.DataFrame(all_data)

# Eliminar duplicados exactos
df_unique = df.drop_duplicates()

# Ver el número de registros únicos
print(f"Total de registros únicos: {len(df_unique)}")
