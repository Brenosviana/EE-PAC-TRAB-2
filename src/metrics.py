
from typing import List


def accuracy(true_classes: List[int], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    predict = np.array(predicted_classes)
    trueC = np.array(true_classes)
    
    return ((predict == trueC).sum())/trueC.shape[0]
