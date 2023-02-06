
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface

global X, Y

class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        arquivoClasses = open('path', 'r')
        #criando lista com os nomes e tags
        nomes = []
        #armazenando os nomes dos datasets e as tags na lista nomes
        for i in arquivoClasses:
            nomes.append(i[0:len(i)-1].split(' '))
        arquivoClasses.close()
        nomesnp = np.array(nomes)    #armazenando textos
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

        

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return nomesnp.shape[0]

    def get(self, idx: int) -> Tuple[Any, int]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        return X[idx], Y[idx]
