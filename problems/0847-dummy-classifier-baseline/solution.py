import numpy as np
from collections import Counter

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    if(strategy=="most_frequent"):
        value, count = np.unique(y_train,return_counts=True)
        most_frequent=value[np.argmax(count)]
        z=np.full(n_test,most_frequent)
        return z
    elif(strategy=="constant"):
        z=np.full(n_test,constant)
        return z
    elif(strategy=="uniform"):
        classes=np.unique(y_train)
        k=len(classes)
        v=[]
        for i in range(n_test):
            v.append(i%k)
        v=np.array(v)
        z=classes[v]
        return z
    elif strategy == "stratified":

        classes, counts = np.unique(y_train, return_counts=True)

        frequencies = counts / len(y_train)

        expected = frequencies * n_test

        allocation = np.floor(expected).astype(int)

        remaining = n_test - np.sum(allocation)

        fractions = expected - allocation

        # Sort by largest fractional part, breaking ties by smallest class
        order = sorted(
            range(len(classes)),
            key=lambda i: (-fractions[i], classes[i])
        )

        for i in range(remaining):
            allocation[order[i]] += 1

        z = []

        for i in range(len(classes)):
            z.extend([classes[i].item()] * allocation[i])

        return z