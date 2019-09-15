import math
import pandas as pd
import itertools


def mttf_sw(a_sw, mttr_sw):
    return (a_sw * mttr_sw / (1 - a_sw))


def availabilityClass(availability):
    return (math.floor(-math.log10(1 - availability)))


def availability(availabilityClass):
    return (1 - (pow(10, -availabilityClass)))


# functions for mean time to failure

def f1_n(x):
    return (x)


def f1_nlogn(x):
    return (x * math.log10(x))


def f1_sqrt_n(x):
    return (math.sqrt(x))


def f1_sqrt_n_cube(x):
    return (pow(x, 1.5))


def f1_n_pow_2over3(x):
    return (pow(x, 2 / 3))


# functions to mean time to recover

def f2_1_over_n(x):
    return (1 / x)


def f2_1_over_nlogn(x):
    return (1 / (x * math.log10(x)))


def f2_1_over_sqrt_n(x):
    return (1 / math.sqrt(x))


def f2_1_over_sqrt_n_cube(x):
    return (pow(x, -1.5))


def f2_1_over_n_pow_2over3(x):
    return (pow(x, -2 / 3))


# lists of column tags and their content
nodes = list(range(2, 101))
availabilityClassHW = [3, 4, 5, 6]
availabilityClassSW = [3, 4, 5, 6]
mttrSW = [3600, 1800, 300, 60, 30]
function1 = [f1_n, f1_nlogn, f1_sqrt_n, f1_sqrt_n_cube, f1_n_pow_2over3]
function2 = [f2_1_over_n, f2_1_over_nlogn, f2_1_over_sqrt_n, f2_1_over_sqrt_n_cube, f2_1_over_n_pow_2over3]

data = []

for i in itertools.product(nodes, availabilityClassHW, availabilityClassSW, mttrSW, function1, function2):
    '''
    nodes_count = temp[0]
    avialability_hw = temp[1]
    avialability_sw = temp[2]
    mttr_sw = temp[3]
    f1 = temp[4]
    f2 = temp[5]
    availability
    '''

    scenario = list(i)
    # getting the availability of the hardware for the availability class for hardware
    aClassHW = availability(scenario[1])
    # getting the availability of the software for the availability class for software
    aClassSW = availability(scenario[2])
    # calculate the availability of the regarding scenario
    overallAvailability = pow((aClassHW * mttf_sw(aClassSW, scenario[3]) * scenario[4](scenario[0]) /
                               (mttf_sw(aClassSW, scenario[3]) * scenario[4](scenario[0]) + scenario[3] *
                                scenario[5](scenario[0]))), scenario[0])
    overallAvailabilityClass = availabilityClass(overallAvailability)
    scenario.append(overallAvailabilityClass)
    data.append([scenario[0], scenario[1], scenario[2], scenario[3], scenario[4].__name__, scenario[5].__name__, overallAvailabilityClass]) # I have fixed so that you can see function name

# data here should be the list containing all the data

df = pd.DataFrame(data, columns=['Nodes', 'HW Availability', 'SW Availability', 'MTTR SW', 'function 1',
                                 'function 2', 'Overall availability'])
print(df.head())
df.to_csv('AvailabilityS.csv')

# isClass_3 = df['a_sw'] == 3
# filtered_data = data[isClass_3]
#
# print(filtered_data.head())