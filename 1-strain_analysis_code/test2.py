import random
import os
# f1 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_data/predicted_strain','r')
#
# lines1 = f1.readlines()
# seq_list = []
# for line1 in lines1:
#     if '>' not in line1:
#         seq_list.append(line1.strip())
#
# seq = ''.join(seq_list)

input_path = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_data'
output_path = '/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/similar_known_strains/test_data1'
files = os.listdir(input_path)

for file in files:
    input_file = input_path + '/' + file
    output_file = output_path + '/known_strain_' + str(files.index(file))
    f1 = open(input_file,'r')
    f2 = open(output_file,'w')

    lines1 = f1.readlines()
    for line1 in lines1:
        if '>' in line1:
            f2.write('>' + 'known_strain_' + str(files.index(file)) + '\n')
        else:
            f2.writelines(line1)
    f1.close()
    f2.close()