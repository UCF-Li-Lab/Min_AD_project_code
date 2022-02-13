
import pandas as pd

def get_common_mutation(file1):
    f1 = open(file1,'r')

    lines1 = f1.readlines()

    list1 = []
    for line1 in lines1:
        if '>' not in line1:
            list1.append(line1.strip())


    print(file1.split('/')[-2])
    real_snp = list(set(list1))

    f2 = open('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/Byrd_paper/Aureus/NC_007795.1/result_new_version_cutoff_score3_3_4.5/n1_nodes_vector.bed','r')
    lines2 = f2.readlines()

    list2 = []
    for line2 in lines2:
        node = line2.split('\t')[0]
        nul = node.split('_')[0]
        loc = node.split('_')[1]
        list2.append(nul + ',' + loc)

    pre_snp = list(set(list2))

    common_node = list(set(real_snp).intersection(set(pre_snp)))

    return common_node


def do_stat(list1,list2):

    common = list(set(list1).intersection(set(list2)))

    common_num = len(common)
    num_all = len(list(set(list1)))

    ave = '%s/%s=%s' % (common_num,num_all,round(100*common_num/num_all,2)) + '%'

    return ave


import os

input_path = '/media/saidi/Elements/Project/Project_for_Min/MSMS_AD_part/Byrd_result/Aureus'

files = os.listdir(input_path)

list_all = []
index1 = []
for file in files:
    input_file = input_path + '/' + file + '/mutation_file'

    list1 = get_common_mutation(input_file)

    list_all.append(list1)
    index1.append(file)

data = []

for i in list_all:
    temp = []
    for j in list_all:
        per = do_stat(i,j)
        temp.append(per)

    data.append(temp)

df = pd.DataFrame(data,index=index1,columns=index1)

df.to_csv('/media/saidi/Elements/Project/Project_for_Min/MSMS_AD_part/Byrd_result/Aureus_statistics/known_strain_per_with_MSMS_n1.bed',sep = '\t')





