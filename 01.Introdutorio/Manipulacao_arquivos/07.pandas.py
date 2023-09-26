import pandas as pd

print(pd.__version__)

file = r"01.Introdutorio\Manipulacao_arquivos\arquivos\salarios.csv"

# df - dataframe
df = pd.read_csv(file)

print(df.head())

print(df['Position Title'].value_counts())