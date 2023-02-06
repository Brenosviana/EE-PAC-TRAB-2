
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import numpy as np
import cv2




class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
            # em uma lista
        #abrindo arquivo 
        arquivoClasses = open(path, 'r')
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
            pathSplit = path.split('/')
            flat = np.array(cv2.imread(  pathSplit[0] + '/' +pathSplit[1] +'/'+ pathSplit[2] + '/'+ i,0))
            Xlist.append(flat.flatten())

        #obtendo arays de featues e targets
        self.X = np.array(Xlist)
        self.Y = nomesnp[:,1]
        

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)

        return int(self.X.shape[0])

    def get(self, idx: int) -> Tuple[Any, int]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        return self.X[idx], self.Y[idx]



