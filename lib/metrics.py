import numpy as np

def accuracy_score(y_true, y_predict):
    """计算y_true和accy_predict之间的准确率"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum(y_true == y_predict) / len(y_true)