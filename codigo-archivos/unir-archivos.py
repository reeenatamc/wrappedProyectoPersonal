import json
import os
import pandas as pd

carpeta_archivos = r"C:/Users/LENOVO/Documents/GitHub/wrappedProyectoPersonal/archivos"  

all_data = []  

for filename in os.listdir(carpeta_archivos):
    if filename.endswith(".json"):  
        file_path = os.path.join(carpeta_archivos, filename)  
        print(f"Procesando archivo: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)  
                print(f"Registros leídos del archivo {filename}: {len(data)}")  
                all_data.extend(data)  
            except json.JSONDecodeError as e:
                print(f"Error al leer el archivo {filename}: {e}")
            except Exception as e:
                print(f"Error inesperado con el archivo {filename}: {e}")



df = pd.DataFrame(all_data)

print(f"Total de registros cargados: {len(df)}")

df_unique = df.drop_duplicates()

print(f"Total de registros únicos: {len(df_unique)}")

output_file_json = "archivos/datos_unidos.json"
df_unique.to_json(output_file_json, orient='records', lines=True, force_ascii=False)

print(f"Datos guardados en {output_file_json}")

