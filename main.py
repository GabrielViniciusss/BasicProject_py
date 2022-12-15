import pandas as pd # Importando a biblioteca mais recomendada para tratar dados em Python
import numpy as np  # Importando uma biblioteca que me ajudará a trabalhar na análise dos dados(aritmetica)
import matplotlib.pyplot as plt #Importando uma biblioteca que me ajudará a plotar os gráficos

Table2006 = pd.read_csv("FIFA - 2006.csv", sep=",", usecols=["Goals For", "Goals Against"], nrows=15)
Table2010 = pd.read_csv("FIFA - 2010.csv", sep=",", usecols=["Goals For", "Goals Against"], nrows=15)
Table2014 = pd.read_csv("FIFA - 2014.csv", sep=",", usecols=["Goals For", "Goals Against"], nrows=15)
Table2018 = pd.read_csv("FIFA - 2018.csv", sep=",", usecols=["Goals For", "Goals Against"], nrows=15)

#Debug para ver se estava carregando corretamente a tabela
#print(Table2006)
#print(Table2010)
#print(Table2014)
#print(Table2018)

GoalsFor_List = Table2006["Goals For"].tolist() + Table2010["Goals For"].tolist() + Table2014["Goals For"].tolist() + Table2018["Goals For"].tolist()
GoalsAgainst_List = Table2006["Goals Against"].tolist() + Table2010["Goals Against"].tolist() + Table2014["Goals Against"].tolist() + Table2018["Goals Against"].tolist()

#Debug Lista
#print(GoalsFor_List)
#print(GoalsAgainst_List)

media_GoalsFor = np.mean(GoalsFor_List)
media_GoalsAgainst = np.mean(GoalsAgainst_List)

#Debug da media
print(f"A media de gols marcados foi {media_GoalsFor}")
print(f"A media de gols sofridos foi {media_GoalsAgainst}")

DP_goalsFor = np.std(GoalsFor_List)
DP_goalsAgainst = np.std(GoalsAgainst_List)

#Debug do Desvio Padrao
print(f"O desvio padrão de gols marcados foi:{DP_goalsFor:.2f}")
print(f"O desvio padrão de gols sofridos foi:{DP_goalsAgainst:.2f}")

floor_GoalsFor = media_GoalsFor - 3*DP_goalsFor
ceil_GoalsFor = media_GoalsFor + 3*DP_goalsFor

floor_GoalsAgainst = media_GoalsAgainst - 3*DP_goalsAgainst
ceil_GoalsAgainst = media_GoalsAgainst + 3*DP_goalsAgainst

#Debug limites superiores e inferiores
print(f"O limite superior de gols marcados foi de: {ceil_GoalsFor:.2f}")
print(f"O limite inferior de gols marcados foi de: {floor_GoalsFor:.2f}")
print(f"O limite superior de gols sofridos foi de: {ceil_GoalsAgainst:.2f}")
print(f"O limite inferior de gols sofridos foi de: {floor_GoalsAgainst:.2f}")

#Grafico Goals For
line = GoalsFor_List
plt.title("Gráfico de gols marcados por time")
plt.plot(line, "ko-")
plt.axhline(y=floor_GoalsFor, color="crimson", linestyle="dashed")  #Definindo os limites superior e inferior
plt.axhline(y=ceil_GoalsFor, color="crimson", linestyle="dashed")
plt.show()

#Grafico Goals Against
line = GoalsAgainst_List
plt.title("Gráfico de gols sofridos por time")
plt.plot(line, "ko-")
plt.axhline(y=floor_GoalsAgainst, color="crimson", linestyle="dashed") #Definindo os limites superior e inferior
plt.axhline(y=ceil_GoalsAgainst, color="crimson", linestyle="dashed")
plt.show()