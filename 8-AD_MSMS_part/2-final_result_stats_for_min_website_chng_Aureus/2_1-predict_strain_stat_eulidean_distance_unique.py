
from collections import Counter

def get_real_mutation(file1):
    f1 = open(file1,'r')

    lines1 = f1.readlines()

    list1 = []
    for line1 in lines1:
        if '>' not in line1:
            list1.append(line1.strip())
    return list1

def get_strain_list():
    f1 = open('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final/NC_007795.1/final_result_current/n1_nodes_vector_original.bed','r')
    lines1 = f1.readlines()

    list1 = []
    for line1 in lines1:
        node = line1.split('\t')[0]
        nul = node.split('_')[1]
        loc = node.split('_')[2]
        list1.append(nul + ',' + loc)

    return list1

def get_strain_dict():
    f1 = open('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final/NC_007795.1/final_result_current/R_strain_step11_test_original.bed','r')
    lines1 = f1.readlines()

    dict1 = {}

    all_list = []

    for line1 in lines1:
        strain_name = line1.split('\t')[0]
        node_list = [eval(i) for i in line1.split('\t')[-1].strip()[1:-1].split(', ')]

        node_list1 = []

        for node in node_list:
            nul = node.split('_')[0]
            loc = node.split('_')[1]
            name = nul + ',' + loc
            node_list1.append(name)

        all_list += node_list1
        dict1[strain_name] = node_list1


    common_list = []

    result = Counter(all_list)

    for key,val in result.items():
        if val > 1:
            common_list.append(key)

    dict2 = {}

    for key,val in dict1.items():

        val1 = [i for i in val if i not in common_list]
        dict2[key] = val1

    return dict2

def do_statistics(dict1):

    num1_list = []
    for key,val in dict1:
        num1_list.append(len(val))

    return num1_list


def get_vector_dict():
    f1 = open(
        '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final/NC_007795.1/final_result_current/n1_nodes_vector_original.bed',
        'r')
    lines1 = f1.readlines()

    dict1 = {}
    for line1 in lines1:
        node = line1.split('\t')[0]
        node_name = node.split('_')[0] + ',' + node.split('_')[1]
        fre_list = [float(i) for i in line1.split('\t')[-1].strip()[1:-1].split(', ')]

        dict1[node_name] = fre_list

    return dict1


def get_euclidean_distance(vector1, vector2):
    from scipy.spatial import distance
    dst = distance.euclidean(vector1, vector2)
    return dst

import pandas as pd

def get_stat(pairs):
    vector_dict = get_vector_dict()

    dis_list = []
    # print(vector_dict)
    for i in pairs:
        # print(i)
        v1 = vector_dict[i[0]]
        v2 = vector_dict[i[1]]
        dis = get_euclidean_distance(v1, v2)
        dis_list.append(dis)

    result = pd.Series(dis_list).describe()

    return [round(i,3) for i in list(result)]



import itertools


dict1 = get_strain_dict()

print(dict1.keys())

data = []

index1 = ['strain1','strain2','strain3','strain4','strain5','strain6','strain7']

columns1 = ['count','mean','std','min','25%','50%','75%','max']

for key,val in dict1.items():
    list1 = val
    print(key,len(val),len(list(set(val))))
    pair1 = list(itertools.combinations(list1,2))
    data.append(get_stat(pair1))

print(data)

df = pd.DataFrame(data,index=index1,columns=columns1)

df.to_csv('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final/NC_007795.1/final_result_current/predicted_distance_stat_unique_original',sep='\t')








