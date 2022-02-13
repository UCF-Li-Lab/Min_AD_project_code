
import pandas as pd
import itertools

def get_stat(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    list1 = []

    for line1 in lines1:

        val = float(line1.split('\t')[-1].strip())
        list1.append(val)

    result = pd.Series(list1)

    sta_list = list(result.describe())

    # ['count','mean','std','min','25%','50%','75%','max']
    return [round(i,3) for i in sta_list]




f1 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/CN1_uid217769_distance_unique.bed'
f2 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/JH1_uid58457_distance_unique.bed'
f3 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/MSHR1132_uid89393_distance_unique.bed'
f4 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/MSSA476_uid57841_distance_unique.bed'
f5 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/ST398_uid59247_distance_unique.bed'


columns1 = ['count','mean','std','min','25%','50%','75%','max']

index1 = ['CN1_uid217769','JH1_uid58457','MSHR1132_uid89393','MSSA476_uid57841','ST398_uid59247']


data = []

data.append(get_stat(f1))
data.append(get_stat(f2))
data.append(get_stat(f3))
data.append(get_stat(f4))
data.append(get_stat(f5))


df = pd.DataFrame(data,index=index1,columns=columns1)

df.to_csv('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/dis_stat_unique.bed',sep = '\t')












