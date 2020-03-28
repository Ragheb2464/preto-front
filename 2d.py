from operator import itemgetter, attrgetter
import numpy as np
import time


def TwoDimensions(data):
    sorted_data = sorted(data, key=itemgetter(0, 1), reverse=True)
    pareto_idx = list()
    pareto_idx.append(0)
    cutt_off = sorted_data[0][1]
    for i in range(1, len(sorted_data)):
        if sorted_data[i][1] > cutt_off:
            pareto_idx.append(i)
            cutt_off = sorted_data[i][1]
    return pareto_idx
