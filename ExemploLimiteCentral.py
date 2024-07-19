# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:42:38 2024

@author: ASGUNZI
"""

import matplotlib.pyplot as plt
import numpy as np


#Bernoulli
p = 0.99  #Sucesso = 1


nVariaveis= 1000 #Numero de variáveis somadas
nTrials =1000 #Numero de amostras
vetorSomas =[]

for i in range(nTrials):
    soma = 0
    for i in range(nVariaveis):
        if np.random.rand(1) <=p:
            soma +=1 #Se sucesso, soma 1
    
    vetorSomas.append(soma)
            

# Create a histogram
plt.hist(vetorSomas, bins=30, edgecolor='black')

# Add a title and labels
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
