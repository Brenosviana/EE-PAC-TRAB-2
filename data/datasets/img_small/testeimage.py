import cv2
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

#criando uma lista auxiliar para armazenar os os valores das imagens
Xlist = []

#percorrendo todas as imagens do aquivo
for i in nomesnp[:,0]:
    Xlist.append(cv2.imread(i,0).flatten())

#obtendo arays de featues e targets
X = np.array(Xlist)
Y = nomesnp[:,1]

#obtendo arrray com dataset completo, onde a primeira coluna é target
dataset = np.zeros((X.shape[0], X.shape[1]+1))
dataset[:,0] = Y
dataset[:,1:] = X


print(dataset.shape)
