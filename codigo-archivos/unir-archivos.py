import json
import pandas as pd
import os

# primero se manda la ubicacion de la carpeta en cuesti[on que tiene todos los archivos que quiero unir
carpeta_archivos = r"C:/Users/LENOVO/Documents/GitHub/wrappedProyectoPersonal/archivos"
# se hace un arreglo que guardara la informacion de todos estos archivos
all_data = []

# se usa un for al que se inicializa la variable filename que recorrera la lista de direcciones de la carpeta de archivos
for filename in os.listdir(carpeta_archivos):
    #si el archivo termina con json entonces entra en el condicional
    if filename.endswith(".json"):
        # aqui basicamente se crea una url para ir a esa ubicacion, siempre se asegura de que sea valida
        file_path = os.path.join(carpeta_archivos, filename)
        #ademas se abre la ruta dada anteriormente en modo lectura como un file, 
        with open(file_path, 'r', encoding='utf-8') as file:
            # ya solo queda cargar el jason
            data = json.load(file)
            # va anadiendo el contenido de la data conforme se vaya iterando
            all_data.extend(data)

# convierte el arreglo que contiene toda la informacion a un datafrma
df = pd.DataFrame(all_data)
# borra los valores duplicados
df_unique = df.drop_duplicates()

# convierte la columna de ts a una fecha
if 'ts' in df_unique.columns:
    df_unique['ts'] = pd.to_datetime(df_unique['ts'], errors='coerce')
# ordena los json por fecha
df_sorted = df_unique.sort_values(by='ts', ascending=True)

# vuelve a convertir los ts en cadenas, ya no fechas
if 'ts' in df_sorted.columns:
    df_sorted['ts'] = df_sorted['ts'].dt.strftime('%Y-%m-%d %H:%M:%S')

    #convierte el dataframe a un diccionario, o sea le da el formato de los anteriores json

sorted_data = df_sorted.to_dict(orient='records')

# me da el archivo y los identa

output_file_json = "archivos/datos_unidos.json"
with open(output_file_json, 'w', encoding='utf-8') as output_file:
    json.dump(sorted_data, output_file, ensure_ascii=False, indent=4)

print(f"Datos guardados en {output_file_json}")
