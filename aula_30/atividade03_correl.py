
#Correlacionar lesao_corp_dolosa e lesao_corp_morte
# import pandas e numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Carregando os dados
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando as variávies 'cisp', 'lesao_corp_dolosa', 'lesao_corp_morte'
    df_ocorrencias = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # Agrupar por cisp e totalizar as lesões dolosas e as mortes
    df_total_lesao = df_ocorrencias.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    print(df_total_lesao.head(10))

except Exception as e:
    print(f'Erro ao carregar os dados {e}')


# Obtendo a correlação person usando numpy
try:
    correlacao = np.corrcoef(df_total_lesao['lesao_corp_dolosa'], df_total_lesao['lesao_corp_morte'])[0, 1]
    print(f'\nA correlação é {correlacao}')


except Exception as e:
    print(f'Erro ao calcular a correlação {e}')


try:

    plt.scatter(df_total_lesao['lesao_corp_dolosa'], df_total_lesao['lesao_corp_morte'])
    plt.xlabel('lesao corporal dolosa')
    plt.ylabel('mortes')
    plt.title(f'Correlação: {correlacao:.2f}')
    plt.show()

except Exception as e: 
    print(f'Erro ao plotar o gráfico {e}')

