import argparse
import os, sys
# Initialize parser

'''
python similar_to_known_strain_pairwise.py --input_strain_loc input_strain_file --known_strain_loc known_strain_loc --output_path  output_path
'''


parser = argparse.ArgumentParser()

parser.add_argument('--input_strain_loc', help='Give a unique sample name',
                    default=None)
parser.add_argument('--known_strain_loc', help='Give a unique sample name',
                    default=None)
parser.add_argument('--output_path', help='all the comparison result',
                    default=True)

args = parser.parse_args()

# input_strain_loc = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/input_strains_file_loc'
# known_strain_loc = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/known_strains_file_loc'
# output_path = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_result'


input_strain_loc = args.input_strain_loc
known_strain_loc = args.known_strain_loc
output_path = args.output_path

print('input_strain_loc:')
print(input_strain_loc)
print('known_strain_loc:')
print(known_strain_loc)
print('output file')
print(output_path)




############### get the mismatch of two sequences##################
def distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strain lengths are not equal!")
    else:
        return sum(1 for (a, b) in zip(str1, str2) if a != b)
############### get the known strain file location#################
def getKnownStrain(known_strain_loc):
    loc_list = []
    f1 = open(known_strain_loc,'r')
    lines1 = f1.readlines()
    for line1 in lines1:
        loc_list.append(line1.strip())
    return loc_list

############ get the similar percentage of two strain ###########
def getPer(str1,str2):
    dis  = distance(str1,str2)
    per = 1- (dis/len(str1))
    return per

############ get the strain sequence ################

def getstrainseq(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    lines1 = ''.join(lines1).split('>')
    input_seq_name = lines1[1].split('\n')[0]
    input_seq = ''.join(lines1[1].split('\n')[1:-1])
    known_seq_name = lines1[2].split('\n')[0]
    known_seq = ''.join(lines1[2].split('\n')[1:-1])

    return [input_seq_name,input_seq,known_seq_name,known_seq]

############## get merged strain files #################
def getmergedfile(input_strain_list,known_strain_loc_list):
    for input_file in input_strain_list:
        name = os.path.split(input_file)[-1]
        for file1 in known_strain_loc_list:
            filenames = [input_file,file1]
            with open(file1 + '_merged_' + name, 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        outfile.write(infile.read())

############### get alignment of two strain ##############
def getalign(input_strain_list,known_strain_loc_list):
    getmergedfile(input_strain_list,known_strain_loc_list)
    for input_strain in input_strain_list:
        name = os.path.split(input_strain)[-1]
        for file in known_strain_loc_list:
            command = 'time mafft --thread 8 --auto %s > %s' % (file + '_merged_' + name ,file + '_align_' + name)
            os.system(command)
            os.remove(file + '_merged_' + name)





########## do comparison ################



input_strain_list = getKnownStrain(input_strain_loc)
known_strain_list = getKnownStrain(known_strain_loc)
getalign(input_strain_list,known_strain_list)

for input_strain in input_strain_list:
    name = os.path.split(input_strain)[-1]
    per_list = []
    for loc in known_strain_list:
        loc_align = loc + '_align_' + name
        known_strain_name = getstrainseq(loc_align)[2]
        known_strain_seq = getstrainseq(loc_align)[3]
        input_seq = getstrainseq(loc_align)[1]

        per = getPer(input_seq,known_strain_seq)

        per_list.append(known_strain_name + '--' + str(per))

    per_list_sorted = sorted(per_list,key=lambda x:float(x.split('--')[1]),reverse=True)

    f2 = open(output_path + '/' + name + '_to_known_strains_percentage','w')
    for i in per_list_sorted:
        f2.write(i.split('--')[0] + '\t' + i.split('--')[1] + '\n')

    f2.close()

####### remove the align files #############
for input_strain in input_strain_list:
    name = os.path.split(input_strain)[-1]
    for loc in known_strain_list:
        loc_align = loc + '_align_' + name
        os.remove(loc_align)