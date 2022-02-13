
import os

def get_ann_dict(ann_file):
    f1 = open(ann_file,'r')
    lines1 = f1.readlines()

    dict1 = {}
    str1 = []

    for line1 in lines1:
        gene_id = line1.split('\t')[15]
        infor = ';'.join(line1.strip().split('\t'))

        str1.append([gene_id,infor])

    print(str1)
    for key,val in str1:
        dict1.setdefault(key,[]).append(val)

    return dict1





def get_output(input_file1,ann_file,output_file):

    dict1 = get_ann_dict(ann_file)

    # print(dict1)

    f1 = open(input_file1,'r')
    f2 = open(output_file,'w')

    lines1 = f1.readlines()

    for line1 in lines1:

        loc = line1.split('\t')[0]

        gene_id = line1.split('\t')[-1].split(';')[1].split(':')[1]

        infor = dict1[gene_id]

        f2.write(loc + '\t' + gene_id + '\t' + '\t'.join(infor) + '\n')

    f1.close()
    f2.close()









input_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/output_result'

ann_file1 = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/For_Annotation_Purposes/Aureus_GCF_000013425.1_ASM1342v1_AnnotationFiles/GCF_000013425.1_ASM1342v1_feature_table.txt'
ann_file2 = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/For_Annotation_Purposes/Epidermidis_GCF_006094375.1_ASM609437v1_AnnotationFiles/GCF_006094375.1_ASM609437v1_feature_table.txt'


files = os.listdir(input_path)

print(files)
for file in files:
    if '.txt' not in file:
        input_file = input_path + '/' + file + '/' + file + '_output.bed'
        output_file = input_path + '/' + file + '/' + file + '_output_annotation.bed'

        if 'Aur' in file:
            get_output(input_file, ann_file1, output_file)
        if 'Epix' in file:
            get_output(input_file, ann_file2, output_file)