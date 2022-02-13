import argparse
import os, sys

'''
python get_similar_strain.py --input input_file_loc --output1  output1 --output2 output2 --cutoff n
'''


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', help='Give a unique sample name',
                    default=None)
parser.add_argument('--output1', help='all the comparison result',
                    default=True)
parser.add_argument('--output2', help='all the comparison result with cutoff',
                    default=True)
parser.add_argument('--cutoff', help='Give a unique sample name',
                    default=True)

args = parser.parse_args()

input_file_list = args.input
output_file1 = args.output1
output_file2 = args.output2
cutoff = float(args.cutoff)

print(input_file_list)
print(output_file1)
print(output_file2)
print(cutoff)


# input_file_list = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/input_file_loc'
# output_file1 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/test_result/all_result'
# output_file2 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/test_result/all_result_cutoff'
# cutoff = 0.5

##### get all the input file location #########
def getFileList(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    list1 = []

    for line1 in lines1:
        list1.append(line1.strip())

    f1.close()

    return list1

####### get the SNPs in each file ##########
def getSNPdict(file1):
    file_tail = os.path.split(file1)[1]
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    lines1 = ''.join(lines1).split('>')[1:]
    dict1 = {}
    for line1 in lines1:
        strain = file_tail + '__' + line1.split('\n')[0]
        SNPs = line1.split('\n')[1:-1]
        dict1[strain] = SNPs

    return dict1

def getCommon(list1,list2):
    common_list = list(set(list1).intersection(set(list2)))
    return common_list


def getCommonPer(dict1,dict2):

    dict3 = {}
    for key1,val1 in dict1.items():
        for key2,val2 in dict2.items():
            common_list = getCommon(val1,val2)
            per = len(common_list)/len(val1)
            dict3[key1 + '--' + key2] = per


    return dict3

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res



###### put all the strains and their SNPs in a dict #######
def getDict_all(input_file_list):
    dict_all = {}
    for file1 in input_file_list:
        SNP_dict1 = getSNPdict(file1)
        for file2 in input_file_list:
            SNP_dict2 = getSNPdict(file2)
            per = getCommonPer(SNP_dict1, SNP_dict2)
            dict_all = Merge(dict_all, per)

    return dict_all

####### get output1, which is a matrix score #########
def getOutput1(input_file_list,output_file1):
    dict_all = getDict_all(input_file_list)
    all_strain_name = []
    for key in dict_all.keys():
        strain_name1 = key.split('--')[0]
        all_strain_name.append(strain_name1)

    all_strain_name = sorted(list(set(all_strain_name)),key=lambda x:x.split('__')[0])

    f1 = open(output_file1,'w')
    f1.write('strain__coverage' + '\t' + '\t'.join(all_strain_name) + '\n')

    for strain1 in all_strain_name:
        temp_per_list = []
        for strain2 in all_strain_name:
            per = dict_all[strain1 + '--' + strain2]
            temp_per_list.append(str(per))

        f1.write(strain1 + '\t' + '\t'.join(temp_per_list) + '\n')

    f1.close()

########## get the similar strains with cutoff #############
def getOutput2(input_file_list, output_file2,cutoff):
    dict_all = getDict_all(input_file_list)

    all_strain_name = []

    for key in dict_all.keys():
        strain_name1 = key.split('--')[0]
        all_strain_name.append(strain_name1)

    all_strain_name = sorted(list(set(all_strain_name)),key=lambda x:x.split('__')[0])

    f2 = open(output_file2, 'w')

    for strain1 in all_strain_name:
        temp_per_list = []
        for strain2 in all_strain_name:
            if strain1 != strain2:
                per = dict_all[strain1 + '--' + strain2]
                if per >= cutoff:
                    temp_per_list.append(strain2 + '----' + str(per))
        temp_per_list = sorted(temp_per_list,key=lambda x:x.split('----')[1],reverse=True)
        f2.write('>' + strain1 + '\n' + '\n'.join(temp_per_list) + '\n')

    f2.close()


input_file_list = getFileList(input_file_list)

getOutput1(input_file_list,output_file1)
getOutput2(input_file_list,output_file2,cutoff)




