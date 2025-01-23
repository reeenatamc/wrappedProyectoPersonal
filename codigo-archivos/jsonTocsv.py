import pandas as pd

input_file_json = "archivos\datos_unidos.json"
output_file_csv = "archivos\datos_unidos.csv"

df = pd.read_json(input_file_json)

df.to_csv(output_file_csv, index=False, encoding='utf-8')
print(f"Archivo convertido a CSV: {output_file_csv}")
