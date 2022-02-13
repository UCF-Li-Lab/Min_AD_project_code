# from Bio import pairwise2 as pw2
#
# first_seq = 'ATGGATCATTGA'
# second_seq = 'CATTGA'
#
# global_align = pw2.align.globalxx(first_seq, second_seq,score_only= True)
# print(global_align)
# print(global_align[0])
# print(global_align[0][0])
# print(global_align[0][1])

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
    print(global_align)
    return global_align


file1 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/input_strain'
file2 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_data/known_strain_0'

seq1 = getstrainseq(file1)[1]
seq2 = getstrainseq(file2)[1]

getalign(seq1,seq2)