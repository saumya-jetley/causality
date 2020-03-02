'''Examples of organizer-provided metrics.
You can just replace this code by your own.
Make sure to indicate the name of the function that you chose as metric function
in the file metric.txt. E.g. mse_metric, because this file may contain more
than one function, hence you must specify the name of the function that is your metric.'''

import numpy as np
import scipy as sp
from sklearn.metrics import accuracy_score

def accuracy(solution, prediction):
    '''
        Compute balanced accuracy.
        Average accuracy on every class.
        Flatten 2D array (causality).
    '''
    if len(solution.shape) == 2:
        solution = solution.flatten()
        prediction = prediction.flatten()
    return accuracy_score(solution, prediction)
