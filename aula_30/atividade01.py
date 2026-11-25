import pandas as pd 
import polars as pl
from datetime import datetime
import os

ENDERECO_DADOS = './../DADOS/auxilio/'
# pandas 5:25:00
# polars 1:13:00
try:
    inicio = datetime.now()
    print('Obtendo os dados de auxílio...')

    df_auxilio = None
    lista_arquivos = []  # Lista Principal p/ o processamento

    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)


    # ### Obtendo os Dataframes
    for arquivo in lista_arquivos:
        print(f'\nProcessando o arquivo {arquivo}...')
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso8859-1') #Polars
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso8859-1')

        if df_auxilio is None:
            df_auxilio = df
        else:
            df_auxilio = pl.concat([df_auxilio, df]) #Polars
            # df_auxilio = pd.concat([df_auxilio, df])

        del df
        print(df_auxilio.head())        
        print(f'\nArquivo {arquivo} processado com sucesso!')


    print(f'Dados concatenados com sucesso!!!')    


    df_auxilio = df_auxilio.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )


    # Salvando em arquivo parquet 
    # instalar biblioteca FASTPARQUET
    print(f'\nSalvando arquivo parquet...')
    df_auxilio.write_parquet('./../DADOS/auxilio.parquet')
    print('Arquivo parquet criado com sucesso!!!')

    fim = datetime.now()
    print(f'Tempo total {fim - inicio}')
except Exception as e:
    print(f'Erro ao obter os dados {e}')

