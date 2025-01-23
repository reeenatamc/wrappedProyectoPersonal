import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Carga del archivo JSON
# primero se abre el archivo, se le pasa la url, r se usa para read que practicamente es que solo lo lea, y el encodde normal.
# luego le dice que como archivo, se le da un nombre a la variable y se usa json.load para cargar el archivo 
with open('archivos\Streaming_History_Audio_2022-2023_0.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# siguiente se lo convierte en un dataframe ya que asi trabaja pandas
df = pd.DataFrame(data)

# se usa print con el dataframe y se llama a head para imprimirlo como un dataframe
print(df.head())