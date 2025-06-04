import pandas as pd

# Listas de arquivos CSV (ajuste os nomes se forem diferentes)
arquivos_acidentes = ['acidentes2023.csv', 'acidentes2024.csv', 'acidentes2025.csv']
arquivos_datatran = ['datatran2023.csv', 'datatran2024.csv', 'datatran2025.csv']
arquivos_causas = ['acidentes2023_todas_causas_tipos.csv', 'acidentes2024_todas_causas_tipos.csv', 'acidentes2025_todas_causas_tipos.csv']

# Função que carrega e concatena arquivos CSV
def carregar_e_concatenar(lista_arquivos):
    dataframes = [pd.read_csv(arquivo, sep=';', encoding='latin1') for arquivo in lista_arquivos]
    df_unido = pd.concat(dataframes, ignore_index=True)
    return df_unido

# Juntando os dados
df_acidentes = carregar_e_concatenar(arquivos_acidentes)
df_datatran = carregar_e_concatenar(arquivos_datatran)
df_causas = carregar_e_concatenar(arquivos_causas)

# Salvando como novos CSVs unificados
df_acidentes.to_csv('acidentes_completo.csv', index=False)
df_datatran.to_csv('datatran_completo.csv', index=False)
df_causas.to_csv('acidentes_causas_completo.csv', index=False)
