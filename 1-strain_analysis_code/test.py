
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

f1 = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/test_data/GCF_000016525.1_ASM1652v1_genomic.fna'
f2 = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/result/test1_strain_seq_0.3'
f3 = '/media/saidi/Elements1/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/strain_seq/result/test1_strain_seq_0.7'

dict1 = getref(f1)
dict2 = getref(f2)
dict3 = getref(f3)

print(dict1[1006784])
print(dict2[1006784])
print(dict3[1006784])

