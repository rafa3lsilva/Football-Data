import pandas as pd
import numpy as np

# ler as bases de dados e armazenar em uma lista
dfs = []
df1 = pd.read_csv('BaseDados\Base_FootballData_2122.csv')
df2 = pd.read_csv('BaseDados\Base_FootballData_2223.csv')
df3 = pd.read_csv('BaseDados\Base_FootballData_2324.csv')
df4 = pd.read_csv('BaseDados\Base_FootballData_2425.csv')

#adicionar as bases à lista
dfs.append(df1)
dfs.append(df2)
dfs.append(df3)
dfs.append(df4)

#concatenar as duas bases
df = pd.concat(dfs, ignore_index=True)

#criar a coluna 'Over 2.5'
df['Over 2.5'] = np.where(df['Gols_H'] + df['Gols_A'] > 2.5, 1, 0)

#criar a coluna 'BTTS'
df['BTTS'] = np.where((df['Gols_H'] > 0) & (df['Gols_A'] > 0), 1, 0)

#salvar a base concatenada
df.to_csv('BaseDados\Base_FootballData.csv', index=False)