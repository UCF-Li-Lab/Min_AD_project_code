import argparse
import os, sys
# Initialize parser

'''
python similar_to_known_strain.py --input_strain --known_strain_loc input_file_loc --output  output_file
'''


# parser = argparse.ArgumentParser()
#
# parser.add_argument('--input_strain', help='Give a unique sample name',
#                     default=None)
# parser.add_argument('--known_strain_loc', help='Give a unique sample name',
#                     default=None)
# parser.add_argument('--output', help='all the comparison result',
#                     default=True)
#
# args = parser.parse_args()

input_file = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/input_strain'
known_strain_loc = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/known_strains_file_loc'
output_file = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_result/similar_strain_per'


# input_file = args.input_strain
# known_strain_loc = args.known_strain_loc
# output_file = args.output

print('input file:')
print(input_file)
print('known_strain_loc:')
print(known_strain_loc)
print('output file')
print(output_file)




############### get the mismatch of two sequences##################
def distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strand lengths are not equal!")
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
    seq_list = []
    for line1 in lines1:
        if '>' not in line1:
            seq_list.append(line1.strip())
    strain_name = lines1[0].strip()[1:]
    seq = ''.join(seq_list)

    return [strain_name,seq]

############### get alignment of two seq ##############
def getalign(first_seq,second_seq):
    from Bio import pairwise2 as pw2
    global_align = pw2.align.globalxx(first_seq, second_seq,score_only= True)
    return global_align

########## do comparison ################

input_strain_name = getstrainseq(input_file)[0]
input_strain = getstrainseq(input_file)[1]

per_list = []

known_strain_list = getKnownStrain(known_strain_loc)
for loc in known_strain_list:
    known_strain_name = getstrainseq(loc)[0]
    known_strain_seq = getstrainseq(loc)[1]
    align_seq = getalign(input_strain,known_strain_seq)
    print(align_seq)
    per = getPer(align_seq[0],align_seq[1])

    per_list.append(known_strain_name + '--' + str(per))

per_list_sorted = sorted(per_list,key=lambda x:float(x.split('--')[1]),reverse=True)

f2 = open(output_file,'w')
for i in per_list_sorted:
    f2.write(i.split('--')[0] + '\t' + i.split('--')[1] + '\n')

f2.close()


