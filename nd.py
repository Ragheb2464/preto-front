from operator import itemgetter, attrgetter
import numpy as np
import time


def GetUndominatedSet(T, B):
    if len(B) == 0:
        return B
    # no element in B canot dominate T, so search only in B
    for i in range(len(T)):
        undominated = (B > T[i]).any(1)
        B = B[undominated[:]]
        if len(B) == 0:
            break

    return list(B)


''' call main func with your data and it will return the Pareto front set'''


def Main(data):
    len_p = len(data)
    if len_p == 1:
        return data
    else:
        idx = round(len_p / 2)
        T = Main(data[:idx])
        B = Main(data[idx:])
        M = T + GetUndominatedSet(T, np.array(B))

        return M
