


import os
import pandas as pd

def read_file(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()

    dict1 = {}

    for line1 in lines1:
        loc = line1.split('\t')[0]
        A_fre = line1.split('\t')[1]
        C_fre = line1.split('\t')[2]
        G_fre = line1.split('\t')[3]
        T_fre = line1.split('\t')[4].strip()

        dict1['A' + ',' + loc] = int(A_fre)
        dict1['C' + ',' + loc] = int(C_fre)
        dict1['G' + ',' + loc] = int(G_fre)
        dict1['T' + ',' + loc] = int(T_fre)

    return dict1



def get_predict_SNPdict(predict_path):
    files = [i for i in os.listdir(predict_path) if 'txt' not in i]
    dict1 = {}
    for file in files:
        input_file = predict_path + '/' + file + '/' + file + '_haplotypes'
        input_file1 = predict_path + '/' + file + '/filter_polymorphic_sites'

        fre_dict = read_file(input_file1)

        file_tail = os.path.split(input_file)[1].split('_')[0]
        f1 = open(input_file,'r')
        lines1 = f1.readlines()
        lines1 = ''.join(lines1).split('>')[1:]

        for line1 in lines1:
            strain = file_tail + '--' + line1.split('\n')[0]
            SNPs = line1.split('\n')[1:-1]
            SNPs_fre = [fre_dict[i] for i in SNPs]
            aver = round(sum(SNPs_fre)/len(SNPs_fre),4)
            dict1[strain] = str(aver)

    return dict1



input_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/MixtureSResults_ByrdandChngPooledDataset'


predict_strain = get_predict_SNPdict(input_path)

output_file = input_path + '/strain_coverage.txt'

f2 = open(output_file,'w')

f2.write('strain_name' + '\t' + 'coverage' + '\n')
for key,val in predict_strain.items():
    f2.write(key + '\t' + val + '\n')

f2.close()














