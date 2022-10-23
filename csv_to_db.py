### Proposta para converter um arquivo .csv para .db via python
# Dataset usado de exemplo: https://www.kaggle.com/datasets/lfarhat/brasil-students-scholarship-prouni-20052019


# Libraries
import pandas as pd
import sqlite3
import os


# Deletando caso já exista
os.remove('prouni.db') if os.path.exists('prouni.db') else None

# Lendo o arquivo (especificar o caminho adequado)
df = pd.read_csv(r'C:\Users\marce\Documents\Tableau\prouni_2005_2019.csv')


# Ajustando as colunas removendo espaços (substituindo por _) e caracteres indesejados
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('(','')
df.columns = df.columns.str.replace(')','')
df.columns = df.columns.str.replace(',','')
df.columns = df.columns.str.replace('.','')
df


# Criando a conexão SQL
c = sqlite3.connect('prouni.db')
cursor = c.cursor()


# Criando a instrução SQL para criar as tabelas
sql_create = "CREATE TABLE prouni_data ("
for n, j in enumerate(df.columns):
  if n != len(df.columns)-1:
    sql_create += f"{j} TEXT,"
  else:
    sql_create += f"{j} TEXT)"

sql_create


# Executando a query e criando as tabelas
cursor.execute(sql_create)


# Criando a lista com o conteúdo do arquivo .csv
records = [tuple(r) for r in df.to_numpy().tolist()]
type(records)


# CCriando a instrução SQL para gravar na tabela
x = '?,'*len(df.columns)
sql_insert = 'insert into prouni_data values ({})'.format(x[:len(x)-1])


# Iteração para executar a gravação
for r in records:
  cursor.execute(sql_insert, r)


# Commit, gravação salva e arquivo com os dados no formato .db
c.commit()
