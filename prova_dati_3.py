#prova_dati_3
#visualizza di dati di maschi (verde) e femmine (rosso)
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/mauriziog/data/main/istat_eta_2022.csv")

import matplotlib.pyplot as plt

# definiamo le dimensioni della finestra in pollici ed il dpi

from matplotlib.pyplot import figure
figure(figsize=(18,10), dpi=80)

x = df['Eta']
y = df['Maschi']
z = df['Femmine']
# plt.fill_between(x,y,color ='green', where =(y<20000))
plt.plot(x,y,'green')
plt.plot(x,z,'red')
