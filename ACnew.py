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
    return ([x, 'n'])


def f1_nlogn(x):
    return ([x * math.log10(x), 'nlogn'])


def f1_sqrt_n(x):
    return ([math.sqrt(x), 'sqrt n'])


def f1_sqrt_n_cube(x):
    return ([pow(x, 1.5), 'n^1.5'])


def f1_n_pow_2over3(x):
    return ([pow(x, 2 / 3), 'n^(2/3)'])


# functions to mean time to recover

def f2_1_over_n(x):
    return ([1 / x, '1/n'])


def f2_1_over_nlogn(x):
    return ([1 / (x * math.log10(x)), '1/nlogn'])


def f2_1_over_sqrt_n(x):
    return ([1 / math.sqrt(x), '1/(sqrt n)'])


def f2_1_over_sqrt_n_cube(x):
    return ([pow(x, -1.5), '1/n^(1.5)'])


def f2_1_over_n_pow_2over3(x):
    return ([pow(x, -2 / 3), '1/n^(2/3)'])


# lists of column tags and their content
nodes = list(range(2, 101))
availabilityClassHW = [3, 4, 5, 6]
availabilityClassSW = [3, 4, 5, 6]
mttrSW = [3600, 1800, 300, 60, 30]
function1 = [f1_n, f1_nlogn, f1_sqrt_n, f1_sqrt_n_cube, f1_n_pow_2over3]
function2 = [f2_1_over_n, f2_1_over_nlogn, f2_1_over_sqrt_n, f2_1_over_sqrt_n_cube, f2_1_over_n_pow_2over3]

# list containing all the scenarios with its overall availability
data = []

for i in itertools.product(nodes, availabilityClassHW, availabilityClassSW, mttrSW, function1, function2):
    scenario = list(i)
    # getting the availability of the hardware for the availability class for hardware
    aClassHW = availability(scenario[1])
    # getting the availability of the software for the availability class for software
    aClassSW = availability(scenario[2])
    # calculate the availability of the regarding scenario
    overallAvailability = pow((aClassHW * mttf_sw(aClassSW, scenario[3]) * scenario[4](scenario[0])[0] /
                               (mttf_sw(aClassSW, scenario[3]) * scenario[4](scenario[0])[0] + scenario[3] *
                                scenario[5](scenario[0])[0])), scenario[0])
    # function 1 naming
    scenario[4] = scenario[4](0.1)[1]
    # function 2 naming
    scenario[5] = scenario[5](0.1)[1]
    overallAvailabilityClass = availabilityClass(overallAvailability)
    scenario.append(overallAvailabilityClass)
    data.append(scenario)

# data here should be the list containing all the data

df = pd.DataFrame(data, columns=['Nodes', 'HW Availability', 'SW Availability', 'MTTR SW', 'function 1',
                                 'function 2', 'Overall availability'])
print(df.head())
df.to_csv('Availability.csv')

# isClass_3 = df['a_sw'] == 3
# filtered_data = data[isClass_3]
#
# print(filtered_data.head())