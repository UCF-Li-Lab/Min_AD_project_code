



import os
from collections import Counter

input_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/output_result_seperate'


files = os.listdir(input_path)

def get_gene_list(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()

    list1 = []

    for line1 in lines1:
        gene_id = line1.split('\t')[1]
        list1.append(gene_id)

    return list(set(list1))

def get_common_list(file_list):

    list_all = []
    for i in file_list:
        list1 = get_gene_list(i)
        list_all += list1

    result = Counter(list_all)

    list_unique = []
    list_at_least_2 = []
    for key,val in result.items():
        if val >1:
            list_at_least_2.append(key)

        else:
            list_unique.append(key)


    return [list_unique,list_at_least_2]


def get_output(file1,file2,list_unique):
    f1 = open(file1,'r')
    lines1 = f1.readlines()

    f2 = open(file2,'w')

    for line1 in lines1:
        gene = line1.split('\t')[1]
        if gene in list_unique:
            f2.writelines(line1)

    f1.close()
    f2.close()


Aur_list = []
Epix_list = []
for file in files:
    if '.txt' not in file:
        input_file = input_path + '/' + file + '/' + file + '_output_annotation.bed'
        if 'Aur' in file:
            Aur_list.append(input_file)
        if 'Epix' in file:
            Epix_list.append(input_file)

Aur_unique = get_common_list(Aur_list)[0]
Aur_common = get_common_list(Aur_list)[1]

Epix_unique = get_common_list(Epix_list)[0]
Epix_common = get_common_list(Epix_list)[1]


f1 = open(input_path + '/Aur_gene_at_least_two.txt','w')
f1.write('\n'.join(Aur_common))

f2 = open(input_path + '/Epix_gene_at_least_two.txt','w')
f2.write('\n'.join(Epix_common))


for file in files:
    if '.txt' not in file:
        input_file = input_path + '/' + file + '/' + file + '_output_annotation.bed'
        output_file = input_path + '/' + file + '/' + file + '_output_annotation_gene_unique.bed'



        if 'Aur' in file:
            get_output(input_file, output_file, Aur_unique)
        if 'Epix' in file:
            get_output(input_file, output_file, Epix_unique)