
import random







f1 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/test_data/known_mutation_file','r')
f2 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/test_data/MixtureS_prediction1','w')
f3 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/test_data/MixtureS_prediction2','w')
f4 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/test_data/MixtureS_prediction3','w')
f5 = open('/media/saidi/Elements/Project/Project17_mixtureS_from_Xin_orginal/latest/MixtureS/Ming/three_codes_v3/similar_mutations_between_strains_v1/test_example/test_data/MixtureS_prediction4','w')

lines1 = f1.readlines()




for line1 in lines1:
    if '>' in line1:
        f2.writelines('>prediction1_strain_' + line1.strip().split('_')[-1] + '\n')
        f3.writelines('>prediction2_strain_' + line1.strip().split('_')[-1] + '\n')
        f4.writelines('>prediction3_strain_' + line1.strip().split('_')[-1] + '\n')
        f5.writelines('>prediction4_strain_' + line1.strip().split('_')[-1] + '\n')

    else:
        A = line1.strip().split(',')[0]
        loc = line1.strip().split(',')[1]

        random.seed(int(loc))
        A_list = ['A','C','G','T']
        print(A_list)
        random.shuffle(A_list)
        print(A_list)

        f2.write(A_list[0] + ',' + loc + '\n')
        f3.write(A_list[1] + ',' + loc + '\n')
        f4.write(A_list[2] + ',' + loc + '\n')
        f5.write(A_list[3] + ',' + loc + '\n')


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()


