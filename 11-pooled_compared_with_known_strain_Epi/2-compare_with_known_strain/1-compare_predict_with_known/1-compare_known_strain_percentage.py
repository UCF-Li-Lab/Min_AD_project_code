
import os
import pandas as pd

def read_file(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()

    list1 = []

    for line1 in lines1[1:]:
        if line1.split(',')[0] != '.':
            list1.append(line1.strip())

    return list1

def get_known_strains(known_strain_path):
    files = os.listdir(known_strain_path)

    dict1 = {}
    for file in files:

        input_file = known_strain_path + '/' + file + '/mutation_file'

        snp_list = read_file(input_file)

        dict1[file] = snp_list

    return dict1

def get_predict_SNPdict(file1):
    file_tail = os.path.split(file1)[1].split('_')[0]
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    lines1 = ''.join(lines1).split('>')[1:]
    dict1 = {}
    for line1 in lines1:
        strain = file_tail + '--' + str(round(float(line1.split('\n')[0]),4))
        SNPs = line1.split('\n')[1:-1]
        dict1[strain] = SNPs

    return dict1

def do_stat(list1,list2):

    common = list(set(list1).intersection(set(list2)))

    common_num = len(common)
    num_all = len(list(set(list1)))

    print(common)

    ave = '%s/%s=%s' % (common_num,num_all,round(100*common_num/num_all,2)) + '%'

    return ave


known_strain_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/Epi_compared_with_known_strain/known_SNPs'

predict_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/MixtureSResults_ByrdandChngPooledDataset'

output_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/Epi_compared_with_known_strain/prediction_compared_with_known_snps'

known_strain_dict = get_known_strains(known_strain_path)

files = [i for i in os.listdir(predict_path) if 'Epi' in i]


for file in files:

    input_file = predict_path + '/' + file + '/' + file + '_haplotypes'

    output_path1 = output_path + '/' + file

    if os.path.exists(output_path1) == False:
        os.makedirs(output_path1)

    output_file = output_path1 + '/predicted_strain_per.bed'
    output_file1 = output_path1 + '/predicted_strain_per_heatmap.bed'
    predict_strain = get_predict_SNPdict(input_file)

    data = []
    data1 = []
    for key, val in predict_strain.items():
        temp = []
        temp1 = []
        for key1,val1 in known_strain_dict.items():
            per1 = do_stat(val, val1)
            per2 = do_stat(val1, val)
            temp.append((per1,per2))
            temp1.append(per1.split('=')[1].split('%')[0])

        data.append(temp)
        data1.append(temp1)

    index1 = list(predict_strain.keys())
    columns1 = list(known_strain_dict.keys())
    df = pd.DataFrame(data, index=index1, columns=columns1)
    df1 = pd.DataFrame(data1, index=index1, columns=columns1)

    df.to_csv(output_file,sep='\t')
    df1.to_csv(output_file1, sep='\t')










