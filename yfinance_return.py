# Download automático de cotações a partir de uma lista de ativos pelo yfinance
# Ajuste para calculo do retorno mensal de cada ativo e extração para .xlsx.


# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# Lista de ativos
listaibov = ['BBAS3.SA', 'ALPA4.SA', 'ABEV3.SA', 'AMER3.SA', 'ARZZ3.SA', 'ASAI3.SA', 
'AZUL4.SA', 'B3SA3.SA', 'BPAN4.SA', 'BBSE3.SA', 'BRML3.SA', 'BBDC3.SA', 'BBDC4.SA', 
'BRAP4.SA', 'BRKM5.SA', 'BRFS3.SA', 'BPAC11.SA', 'CRFB3.SA', 'CCRO3.SA', 
'CMIG4.SA', 'CIEL3.SA', 'COGN3.SA', 'CPLE6.SA', 'CSAN3.SA', 'CPFE3.SA', 'CMIN3.SA', 
'CVCB3.SA', 'CYRE3.SA', 'DXCO3.SA', 'ECOR3.SA', 'ELET3.SA', 'ELET6.SA', 'EMBR3.SA', 
'ENBR3.SA', 'ENGI11.SA', 'ENEV3.SA', 'EGIE3.SA', 'EQTL3.SA', 'EZTC3.SA', 'FLRY3.SA', 
'GGBR4.SA', 'GOAU4.SA', 'GOLL4.SA', 'NTCO3.SA', 'SOMA3.SA', 'HAPV3.SA', 'HYPE3.SA', 
'IGTI11.SA', 'IRBR3.SA', 'ITSA4.SA', 'ITUB4.SA', 'JBSS3.SA', 'KLBN11.SA', 'RENT3.SA', 
'LWSA3.SA', 'LREN3.SA', 'MGLU3.SA', 'MRFG3.SA', 'CASH3.SA', 'BEEF3.SA', 'MRVE3.SA', 
'MULT3.SA', 'PCAR3.SA', 'PETR3.SA', 'PETR4.SA', 'PRIO3.SA', 'PETZ3.SA', 'POSI3.SA', 
'QUAL3.SA', 'RADL3.SA', 'RAIZ4.SA', 'RDOR3.SA', 'RAIL3.SA', 'RRRP3.SA', 'SBSP3.SA', 'SANB11.SA', 
'SMTO3.SA', 'CSNA3.SA', 'SLCE3.SA', 'SULA11.SA', 'SUZB3.SA', 'TAEE11.SA', 'VIVT3.SA', 
'TIMS3.SA', 'TOTS3.SA', 'UGPA3.SA', 'USIM5.SA', 'VALE3.SA', 'VIIA3.SA', 'VBBR3.SA', 
'WEGE3.SA', 'YDUQ3.SA']


# Iterando e armazeando a extração do histórico de cada ação em dataframes em uma lista
dfs = []

for i in listaibov:
  print(f'Lendo o ticker {i}...')
  aux = yf.download(i, start='2010-01-01', end='2022-09-30',interval='1mo')
  aux2 = aux.dropna()
  aux2.reset_index(inplace=True)     
  aux2['ticker'] = i
  dfs.append(aux2)

dfs[1].tail(10)


# Função para ajuste do dataframe na separação das datas e calcular rentabilidade
# empurrando o vetor (shift)
def ajustes(df):
  df['year'] = df['Date'].dt.year
  df['month'] = df['Date'].dt.month
  df['day'] = df['Date'].dt.day
  df['adj_date'] = df['month'].map(str)+'/'+df['year'].map(str)
  df['profitability'] = df['Adj Close'] / df['Adj Close'].shift() * 100 -100


# Aplicando ajustes aos dfs
for d in dfs:
  ajustes(d)


# Gerando lista de DFs[] automaticamente para a concatenação abaixo
for i in range(0,92):
  print(f'dfs[{i}],', end='')

# Concatenando todos os dataframes
dfsconcatenados = pd.concat([dfs[0],dfs[1],dfs[2],dfs[3],dfs[4],dfs[5],dfs[6],dfs[7],
dfs[8],dfs[9],dfs[10],dfs[11],dfs[12],dfs[13],dfs[14],dfs[15],dfs[16],dfs[17],dfs[18],
dfs[19],dfs[20],dfs[21],dfs[22],dfs[23],dfs[24],dfs[25],dfs[26],dfs[27],dfs[28],dfs[29],
dfs[30],dfs[31],dfs[32],dfs[33],dfs[34],dfs[35],dfs[36],dfs[37],dfs[38],dfs[39],dfs[40],
dfs[41],dfs[42],dfs[43],dfs[44],dfs[45],dfs[46],dfs[47],dfs[48],dfs[49],dfs[50],dfs[51],
dfs[52],dfs[53],dfs[54],dfs[55],dfs[56],dfs[57],dfs[58],dfs[59],dfs[60],dfs[61],dfs[62],
dfs[63],dfs[64],dfs[65],dfs[66],dfs[67],dfs[68],dfs[69],dfs[70],dfs[71],dfs[72],dfs[73],
dfs[74],dfs[75],dfs[76],dfs[77],dfs[78],dfs[79],dfs[80],dfs[81],dfs[82],dfs[83],dfs[84],
dfs[85],dfs[86],dfs[87],dfs[88],dfs[89],dfs[90],dfs[91]])

dfsconcatenados

# Removendo coluna de data repetida
dfsconcat = dfsconcatenados.drop(columns=['Date'])
dfsconcat

# Exportando arquivo 
dfsconcat.to_excel(r"C:\Users\marce\Desktop\rentabilidadehist.xlsx")

