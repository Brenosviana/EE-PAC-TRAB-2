

from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np

global k


def dist(x1,x2):
    d = (x1 - x2)
    d = d**2
    return d.sum()

def kMaisProximos(self, x):
    k = 17
    ds = []
    
    for i in self.dataset:
        ds.append(dist(x,i))

    dsnp = np.zeros((dsnp.shape[0], 2))
    dsnp[:,0] = self.dataset[:,0]
    dsnp[:,1] = np.array(ds)
    dsnp[dsnp[:,1].argsort()]

    return max(dsnp[:,0:self.k],key = dsnp[:,0:self.k].count) 


    

class KnnClassifier(ClassifierInterface):
    def __init__(self, k : int) -> None:
        super().__init__()
        self.k = k
        
    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        
        self.dataset = np.array(train_dataset)
        pass

    def predict(self, test_dataset: DatasetInterface) -> List[int]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        resultado = []
        dados = test_dataset
        for i in range(test_dataset.size()):
            resultado.append(kMaisProximos(self,test_dataset.get(i)))

        return resultado
