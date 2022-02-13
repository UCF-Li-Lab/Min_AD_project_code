

f1 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test','r')

lines1 = f1.readlines()
lines1 = ''.join(lines1).split('>')

for i in lines1[1:]:
    seq_name = i.split('\n')[0]
    print(i.split('\n'))
    seq = ''.join(i.split('\n')[1:-1])
    # print(seq)