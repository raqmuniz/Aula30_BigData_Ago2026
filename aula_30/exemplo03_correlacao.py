# import pandas e numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Carregando os dados
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando as variávies 'cisp', 'roubo_veiculo', 'recuperacao_veiculos'
    df_ocorrencias = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # Agrupar por cisp e totalizar os roubos e as recuperações
    df_total_veiculos = df_ocorrencias.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()

    print(df_total_veiculos.head(10))

except Exception as e:
    print(f'Erro ao carregar os dados {e}')


# Obtendo a correlação person usando numpy
try:
    correlacao = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])[0, 1]
    print(f'\nA correlação é {correlacao}')


except Exception as e:
    print(f'Erro ao calcular a correlação {e}')


try:

    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.xlabel('Roubos')
    plt.ylabel('Recuperações')
    plt.title(f'Correlação: {correlacao:.2f}')
    plt.show()

except Exception as e: 
    print(f'Erro ao plotar o gráfico {e}')

