
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.centroids = []

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        Y = data[:,0]
        X = data[:,1:]
        unique_classes = np.unique(Y)
        centroids = []
        for c in unique_classes:
            class_data = X[Y == c]
            centroid = np.mean(class_data, axis=0)
            centroids.append(centroid)
        return np.array(centroids)


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
         # calcula a distância euclidiana entre cada ponto e cada centroide
        distances = np.sqrt(np.sum((dataset[:, np.newaxis, :] - centroids)**2, axis=-1))
        # retorna o índice do centroide mais próximo para cada ponto
        return np.argmin(distances, axis=-1)
        
