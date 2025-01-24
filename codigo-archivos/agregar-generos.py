import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
import time

# Credenciales de la API de Spotify
client_id = 'cc52674f8e7d4e42b8b0be86be82eaff'
client_secret = '423bbdde19d2429fb3d64d1bd1c3dbda'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Cargar datos
input_file = "archivos/datos_unidos.json"
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Obtener nombres únicos de artistas
artistas_unicos = list(set(entry.get("master_metadata_album_artist_name") for entry in data if entry.get("master_metadata_album_artist_name")))

# Crear un diccionario para almacenar los géneros por artista
generos_por_artista = {}

import time

def obtener_generos(artist_name):
    while True:  # Reintentar hasta que funcione
        try:
            results = sp.search(q=f"artist:{artist_name}", type="artist", limit=1)
            if results['artists']['items']:
                return results['artists']['items'][0]['genres']
            else:
                return []
        except Exception as e:
            if "rate/request limit" in str(e).lower():
                wait_time = 65  # Tiempo de espera en segundos
                print(f"Límite alcanzado. Esperando {wait_time} segundos...")
                time.sleep(wait_time)
            else:
                print(f"Error al obtener géneros para {artist_name}: {e}")
                return []


# Obtener géneros para cada artista único
for i, artist_name in enumerate(artistas_unicos):
    if artist_name not in generos_por_artista:
        generos_por_artista[artist_name] = obtener_generos(artist_name)
        print(f"{i+1}/{len(artistas_unicos)}: Géneros obtenidos para {artist_name}")
        time.sleep(0.1)  # Para evitar sobrecargar la API

# Agregar géneros al conjunto de datos original
for entry in data:
    artist_name = entry.get("master_metadata_album_artist_name")
    if artist_name in generos_por_artista:
        entry["genres"] = generos_por_artista[artist_name]

# Guardar datos actualizados
output_file = "archivos/datos_unidos_optimizado.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Archivo actualizado con géneros: {output_file}")
