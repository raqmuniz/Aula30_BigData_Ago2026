import pandas as pd
import polars as pl
from datetime import datetime


ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Obtendo dados parquet...')

    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # Pandas 29 seg
    # df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # Polars - Leitura direta 17 seg


    # Sacan Parquet: 
    # Cria um plano de execução. Não obtem os dados direto.
    # 13 seg
    df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # Polars Leitura Preguiçosa

    # Collect: Executa o plano de execução e traz os dados
    df_bolsa_familia = df_bolsa_familia.collect()
    print(df_bolsa_familia.head())



except Exception as e:
    print(f'Erro ao obter dados parquet')


# Processamento
try:
    import numpy as np
    import matplotlib.pyplot as plt
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

    plt.boxplot(array_valor_parcela, orientation='horizontal')
    fim = datetime.now()
    plt.show()

    print(f'Tempo total {fim - inicio}')
except Exception as e:
    print('Erro')