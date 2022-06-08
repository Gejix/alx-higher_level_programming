#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numera = 0
    denorm = 0

    for tupl in my_list:
        numera += tupl[0] * tupl[1]
        denorm += tupl[1]

    return (numera / denorm)
