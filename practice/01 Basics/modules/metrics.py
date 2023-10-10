import numpy as np


def ED_distance(ts1, ts2):
    """
    Calculate the Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    ed_dist : float
        Euclidean distance between ts1 and ts2.
    """

    ed_dist = ((ts1 - ts2)**2).sum()**0.5

    return ed_dist


def norm_ED_distance(ts1, ts2):
    """
    Calculate the normalized Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    norm_ed_dist : float
        The normalized Euclidean distance between ts1 and ts2.
    """

    norm_ed_dist = 0

    
    n = len(ts1)
    a = np.dot(ts1,ts2) - n * ts1.mean() * ts2.mean()
    b = n * ts1.std()* ts2.std()
    
    norm_ed_dist = (2*n * (1- a/b))**0.5


    return norm_ed_dist


def DTW_distance(ts1, ts2, r=None):
    """
    Calculate DTW distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    r : float
        Warping window size.
    
    Returns
    -------
    dtw_dist : float
        DTW distance between ts1 and ts2.
    """

    dtw_dist = 0

    # INSERT YOUR CODE
    m = len(ts1)
    d = np.zeros((m,m))
    D = np.ones((m+1,m+1))
    D[0,0]=0
    for i in range(1, m+1):
        for j in range(1, m+1):
            d[i-1,j-1] = ED_distance(ts1[i-1], ts2[j-1])**2
            D[i,j] = d[i-1,j-1] + min(D[i-1,j], D[i,j-1], D[i-1,j-1])
    return D[m,m]
 