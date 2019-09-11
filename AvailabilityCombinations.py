import numpy as np
import math
import pandas as pd
import itertools


def mttf_sw(a_sw, mttr_sw):
    return (a_sw * mttr_sw / (1 - a_sw))


def aclass(avail):
    return (math.floor(-math.log10(1 - avail)))


def avail(aclass):
    return (1 - (pow(10, -aclass)))


# functions for mean time to failure

def funcfail1(x):
    return (x)


def funcfail2(x):
    return (x * math.log10(x))


def funcfail3(x):
    return (math.sqrt(x))


def funcfail4(x):
    return (pow(x, 1.5))


def funcfail5(x):
    return (pow(x, 2 / 3))


# functions to mean time to recover

def funcrec1(x):
    return (1 / x)


def funcrec2(x):
    return (1 / (x * math.log10(x)))


def funcrec3(x):
    return (1 / math.sqrt(x))


def funcrec4(x):
    return (pow(x, -1.5))


def funcrec5(x):
    return (pow(x, -2 / 3))


# lists of column tags and their content
n_list = list(range(2, 100))
ahw_list = [3, 4, 5, 6]
asw_list = [3, 4, 5, 6]
mttrsw_list = [3600, 1800, 300, 60, 30]
f1_list = [funcfail1, funcfail2, funcfail3, funcfail4, funcfail5]
f2_list = [funcrec1, funcrec2, funcrec3, funcrec4, funcrec5]

# no of combinations
size = len(n_list)*len(ahw_list)*len(asw_list)*len(mttrsw_list)*len(f1_list)*len(f2_list)
avail_list = np.zeros(size)

# creating an 6D array for store availability values
availability = np.zeros(, size)

for n in n_list:
    for ahw in ahw_list:
        for asw in asw_list:
            for mttrsw in mttrsw_list:
                for f1 in f1_list:
                    for f2 in f2_list:
                        temp = pow(
                            (mttf_sw(asw, mttrsw) * f1(n) / (mttf_sw(asw, mttrsw) * f1(n) + mttrsw * f2(n))), n)
                        avail_list.append(temp)

for i in itertools.product(n_list, ahw_list, asw_list, mttrsw_list, f1_list, f2_list):
    print(list(i))

# data here should be the list containing all the data
df = pd.DataFrame(data, columns=['Nodes', 'a_hw', 'a_sw', 'mttr_sw', 'f1', 'f2', 'availability'])
print(df)
