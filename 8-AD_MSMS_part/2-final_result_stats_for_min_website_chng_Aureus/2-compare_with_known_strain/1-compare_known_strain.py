
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

    f2 = open('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/n1_nodes_vector.bed','r')
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


f1 = '/media/saidi/Elements/Project/Project17_1_MSMS/real_data/From_Min/Chang_paper/ref_genome_used/Aureus_compared_with_known_strain/Aureus_with_CN1_uid217769/mutation_file'
f2 = '/media/saidi/Elements/Project/Project17_1_MSMS/real_data/From_Min/Chang_paper/ref_genome_used/Aureus_compared_with_known_strain/Aureus_with_JH1_uid58457/mutation_file'
f3 = '/media/saidi/Elements/Project/Project17_1_MSMS/real_data/From_Min/Chang_paper/ref_genome_used/Aureus_compared_with_known_strain/Aureus_with_MSHR1132_uid89393/mutation_file'
f4 = '/media/saidi/Elements/Project/Project17_1_MSMS/real_data/From_Min/Chang_paper/ref_genome_used/Aureus_compared_with_known_strain/Aureus_with_MSSA476_uid57841/mutation_file'
f5 = '/media/saidi/Elements/Project/Project17_1_MSMS/real_data/From_Min/Chang_paper/ref_genome_used/Aureus_compared_with_known_strain/Aureus_with_ST398_uid59247/mutation_file'


list1 = get_common_mutation(f1)
list2 = get_common_mutation(f2)
list3 = get_common_mutation(f3)
list4 = get_common_mutation(f4)
list5 = get_common_mutation(f5)

list_all = [list1,list2,list3,list4,list5]

data = []
index1 = ['CN1_uid217769','JH1_uid58457','MSHR1132_uid89393','MSSA476_uid57841','ST398_uid59247']

for i in list_all:
    temp = []
    for j in list_all:
        per = do_stat(i,j)
        temp.append(per)

    data.append(temp)

df = pd.DataFrame(data,index=index1,columns=index1)

df.to_csv('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/known_strain_per.bed',sep = '\t')





