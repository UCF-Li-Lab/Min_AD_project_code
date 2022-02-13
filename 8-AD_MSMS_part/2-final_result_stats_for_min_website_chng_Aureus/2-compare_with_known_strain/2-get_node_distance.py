
import pandas as pd
import itertools
def get_vector_dict():
    f1 = open('/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/n1_nodes_vector.bed','r')
    lines1 = f1.readlines()

    dict1 ={}
    for line1 in lines1:
        node = line1.split('\t')[0]
        node_name = node.split('_')[0] + ',' + node.split('_')[1]
        fre_list = [float(i) for i in line1.split('\t')[-1].strip()[1:-1].split(', ')]

        dict1[node_name] = fre_list

    return dict1





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

def get_euclidean_distance(vector1, vector2):
     from scipy.spatial import distance
     dst = distance.euclidean(vector1, vector2)
     return dst



def get_output(file1,pairs):
    vector_dict = get_vector_dict()
    f1 = open(file1,'w')

    for i in pairs:
        v1 = vector_dict[i[0]]
        v2 = vector_dict[i[1]]
        dis = get_euclidean_distance(v1,v2)
        f1.write(str(i) + '\t' + str(dis) + '\n')

    f1.close()





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



pair1 = list(itertools.combinations(list1,2))
pair2 = list(itertools.combinations(list2,2))
pair3 = list(itertools.combinations(list3,2))
pair4 = list(itertools.combinations(list4,2))
pair5 = list(itertools.combinations(list5,2))



f1 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/CN1_uid217769_distance.bed'
f2 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/JH1_uid58457_distance.bed'
f3 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/MSHR1132_uid89393_distance.bed'
f4 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/MSSA476_uid57841_distance.bed'
f5 = '/media/saidi/Elements/Project/Project17_1_MSMS/testing_real/Min_data/chang_paper/Aureus_final_new_version/NC_007795.1/result_new_version_cutoff_score3_3_4.5/compared_with_known_strain/ST398_uid59247_distance.bed'


get_output(f1,pair1)
get_output(f2,pair2)
get_output(f3,pair3)
get_output(f4,pair4)
get_output(f5,pair5)











