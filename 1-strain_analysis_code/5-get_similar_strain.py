import argparse
import os, sys

'''
python get_similar_strain.py --input input_file_loc --ref ref_file --output_path output_path
'''


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', help='Give a unique sample name',
                    default=None)
parser.add_argument('--ref', help='Give a ref file',
                    default=None)
parser.add_argument('--output_path', help='all the comparison result',
                    default=True)

args = parser.parse_args()

input_file_list = args.input
ref_file = args.ref
output_file1 = args.output_path + '/output1_similar_SNP'
output_file2 = args.output_path + '/output2_uniques_SNP'
output_file3 = args.output_path + '/output3_summary_info'

print(input_file_list)
print(ref_file)
print(output_file1)
print(output_file2)
print(output_file3)


# input_file_list = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/input_file_loc'
# ref_file = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/ref/ref.fna'
# output_file1 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/output/output1_similar_SNP'
# output_file2 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/output/output2_uniques_SNP'
# output_file3 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/output/output3_summary_info'


##### get all the input file location #########
def getFileList(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    list1 = []

    for line1 in lines1:
        list1.append(line1.strip())

    f1.close()

    return list1

##### get the ref location information #######
def getRef(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()

    ref_list = []

    for line1 in lines1[1:]:

        ref = line1.strip()
        ref_list.append(ref)

    ref_all = ''.join(ref_list)

    ref_dict = {}
    for i in range(len(ref_all)):

        ref_dict[str(i)] = ref_all[i]

    return ref_dict




####### get the SNPs in each file ##########
def getSNPdict(file1):
    file_tail = os.path.split(file1)[1]
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    lines1 = ''.join(lines1).split('>')[1:]
    dict1 = {}
    for line1 in lines1:
        strain = file_tail + '--' + line1.split('\n')[0]
        SNPs = line1.split('\n')[1:-1]
        dict1[strain] = SNPs

    return dict1


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res



###### put all the strains and their SNPs in a dict #######
def getDict_all(input_file_list):
    dict_all = {}
    for file1 in input_file_list:
        SNP_dict1 = getSNPdict(file1)
        dict_all = Merge(dict_all, SNP_dict1)

    loc_dict = {}
    str1 = []

    # print(dict_all)

    for key,val in dict_all.items():
        for i in val:
            A = i.split(',')[0]
            loc = i.split(',')[1]

            str1.append([loc,key + '--' + A])

    for key,val in str1:
        loc_dict.setdefault(key,[]).append(val)

    return [dict_all,loc_dict]

####### get output1 and output2, which is a matrix score #########
def getOutput(input_file_list,ref_file,output_file1,output_file2,output_file3):
    dict_all = getDict_all(input_file_list)[0]
    loc_all = getDict_all(input_file_list)[1]
    ref_dict = getRef(ref_file)

    f1 = open(output_file1, 'w')
    f2 = open(output_file2, 'w')
    f3 = open(output_file3, 'w')
    f1.write('location' + '\t' + 'ref_seq' + '\t' + 'SNP_in_strains' + '\n')
    f2.write('location' + '\t' + 'ref_seq' + '\t' + 'SNP_in_strains' + '\n')

    for key,val in loc_all.items():

        if len(val) > 1:
            f1.write(key + '\t' + ref_dict[key] + '\t' + '|'.join(val) + '\n')
        else:
            f2.write(key + '\t' + ref_dict[key] + '\t' + '|'.join(val) + '\n')


    for key,val in dict_all.items():
        total_SNP_positions = len(val)

        total_similar_pos = 0
        total_unique_pos = 0

        total_same_snps = []
        for i in val:
            A = i.split(',')[0]
            loc = i.split(',')[1]
            loc_snps = loc_all[loc]

            if len(loc_snps) >1:
                total_similar_pos +=1
            else:
                total_unique_pos +=1

            temp_list = []
            # print(loc_snps)
            for j in loc_snps:
                nul = j.split('--')[-1]
                if nul == A:
                    temp_list.append(j)

            total_same_snps.append([i,temp_list])

        f3.write('>' + key + '\n' + str(total_SNP_positions) + '|' + str(total_similar_pos) + '|' + str(total_unique_pos) + '|' + str(len([ i for i in total_same_snps if len(i[1]) >1])) + '\n')

        for i in total_same_snps:
            f3.write(i[0] + '\t' + '|'.join(i[1]) + '\n')

    f1.close()
    f2.close()
    f3.close()




input_file_list = getFileList(input_file_list)

getOutput(input_file_list,ref_file,output_file1,output_file2,output_file3)





