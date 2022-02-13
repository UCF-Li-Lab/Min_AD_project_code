import argparse
import os, sys

'''
python get_similar_strain.py --input input_file_loc --ref genome_file --output  output_file
'''


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', help='Give a unique sample name',
                    default=None)
parser.add_argument('--ref', help='whole genome sequence',
                    default=None)
parser.add_argument('--output', help='all the comparison result',
                    default=True)

args = parser.parse_args()

input_file = args.input
ref = args.ref
output_file = args.output

print('input file:')
print(input_file)
print('ref:')
print(ref)
print('output file')
print(output_file)


# input_file = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/test_data/test_haplotypes'
# ref = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/test_data/GCF_000016525.1_ASM1652v1_genomic.fna'
# output_file = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/result/test1_strain_seq'

##### get ref seq dict[location] = 'A' or 'C' or 'G' or 'T' #########
def getref(file1):
    f1 = open(file1,'r')
    lines1 = f1.readlines()
    dict1 = {}
    seq_list = []
    for line1 in lines1:
        if '>' not in line1:
            seq_list.append(line1.strip())
    seq = ''.join(seq_list)

    for i in range(len(seq)):
        dict1[i] = seq[i]

    return dict1

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

####### get output strain seq #########

def getoutput(input_file,ref,output_file):

    SNP_dict = getSNPdict(input_file)

    f1 = open(output_file,'w')

    for key,vals in SNP_dict.items():
        ref_dict = getref(ref)
        for val in vals:
            loc = int(val.split(',')[1])
            snp = val.split(',')[0]
            ref_dict[loc]=snp

        strain_seq_list = []
        for key1,val1 in ref_dict.items():
            strain_seq_list.append(val1)
        strain_seq = ''.join(strain_seq_list)

        f2 = open(output_file + '_' + key.split('__')[-1],'w')

        f1.write('>' + key + '\n')
        f2.write('>' + key + '\n')
        for i in range(0,len(strain_seq),80):
            seq = strain_seq[i:i+80]
            f1.write(seq + '\n')
            f2.write(seq + '\n')

        f2.close()

    f1.close()

getoutput(input_file,ref,output_file)





