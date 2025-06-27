import pandas as pd
import json

# Caminhos dos arquivos
arquivo1 = '/home/bruno/Documentos/Desenv/data/geo/BR_Municipios_2024 - convertido/BR_Municipios_2024-1.json'
arquivo2 = '/home/bruno/Documentos/Desenv/data/geo/BR_Municipios_2024 - convertido/BR_Municipios_2024-2.json'

# Carrega os JSONs em DataFrames
df1 = pd.read_json(arquivo1)
df2 = pd.read_json(arquivo2)

# Junta os DataFrames (sem eliminar duplicadas)
df_final = pd.concat([df1, df2], ignore_index=True)

# (Opcional) Remover duplicatas com base em alguma coluna
# df_final = df_final.drop_duplicates(subset='id')

# Exporta como JSON (estrutura: lista de dicionários)
df_final.to_json('/home/bruno/Documentos/Desenv/build_data_urbis/data/geo/BR_Municipios_2024-compeleto.json', orient='records', indent=2, force_ascii=False)
