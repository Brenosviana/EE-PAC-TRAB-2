import numpy as np


#abrindo arquivo 
arquivoClasses = open('train.txt', 'r')
#criando lista com os nomes e tags
nomes = []
#armazenando os nomes dos datasets e as tags na lista nomes
for i in arquivoClasses:
    nomes.append(i[0:len(i)-1].split(' '))
arquivoClasses.close()
nomesnp = np.array(nomes)

#armazenando textos
textos = []
listaTextos = []

for i in nomesnp[:,0]:
    texto = open(i, 'r')
    for j in texto:
        textos.append(j)
    texto.close()

aux = np.array(sorted(str(textos).split(' ')))
aux = np.unique(aux)
aux1 = np.array(aux)
#aux é o vetor base para criar os vetores numéricos

X = np.zeros((nomesnp.shape[0], aux1.shape[0]))
Y = np.array(nomesnp[:,1])

for i in range(nomesnp.shape[0]):
    linhaBruta = open(nomesnp[i,0],'r')
    for j in linhaBruta:
        palavrasLinha = np.array(sorted(str(j).split(' ')))
        #print(palavrasLinha)
        for k in palavrasLinha:
            #verifica frequencia de cada palavra 
            X[i] = X[i] + (aux1 == k)*1
    linhaBruta.close()

#retorna dataset completo, com as tags na primeira coluna

dataset = np.empty((X.shape[0], X.shape[1]+1))
dataset[:,0] = (Y == 'inf')*1 + (Y == 'at2')*2 + (Y == 'pot')*3
dataset[:,1:] = X
    
print(dataset)





        
        
