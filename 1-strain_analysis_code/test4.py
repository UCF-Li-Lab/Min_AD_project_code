
from Bio.Emboss.Applications import NeedleCommandline

def needle_align_code(query_seq, target_seq):
    needle_cline = NeedleCommandline(asequence="asis:" + query_seq,
                                     bsequence="asis:" + target_seq,
                                     aformat="simple",
                                     gapopen=10,
                                     gapextend=0.5,
                                     outfile='stdout'
                                     )
    out_data, err = needle_cline()
    out_split = out_data.split("\n")
    print(out_split[25])
    # p = re.compile("\((.*)\)")
    # return p.search(out_split[25]).group(1).replace("%", "")


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


file1 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/input_strain'
file2 = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_data/known_strain_0'

# seq1 = getstrainseq(file1)[1]
# seq2 = getstrainseq(file2)[1]

seq1 = 'aaabbbcccc'
seq2 = 'bccccaaaaa'

needle_align_code(seq1,seq2)