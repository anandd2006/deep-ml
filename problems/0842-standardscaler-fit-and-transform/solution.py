import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    m_train=np.mean(X_train,axis=0)
    s_train=np.std(X_train,axis=0)
     
    
    z=np.zeros(X_test.shape)
    for j in range(X_test.shape[1]):
        for i in range(X_test.shape[0]):
            if(s_train[j]==0):
                z[i][j]=X_test[i][j]-m_train[j]
            else:
                z[i][j]=(X_test[i][j]-m_train[j])/s_train[j]

    return z


