#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path
filename = r'/home/h392x566/Project_Folder/genetic_project/genetic_disease/famdata/Fam310_genotypes_VQSR.vcf.gz'
# Generate CSV colume
row0=["Index","CHROM","Start","REF","ALT","FORMAT","sample310","sample3101","sample31010","OmniAffected GT 0/0","OmniAffected GT 0/1","OmniAffected GT 1/1","OmniUnaffected GT 0/0","OmniUnaffected GT 0/1","OmniUnaffected GT 1/1"]
csvfile = file('./FamCsv/Fam310_11_16.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
# Filter VCF Data
vcf_reader = vcf.Reader(filename=filename) 
#record = next(vcf_reader)
for record in vcf_reader:  
    a00=0
    a01=0
    a11=0
    af0=0
    u00=0
    u01=0
    u11=0
    uaf=0

    # ar0=''
    # ar1=''
    # ar2=''
    # ar3=''
    # ar4=''
    # ar5=''
    # ar6=''

    pos=''

    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    altlist = []
    new=record.CHROM

#310 1
    if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[0]['GT'] in '0/1' or record.samples[0]['GT'] in '0|1' or record.samples[0]['GT'] in '2/3' or record.samples[0]['GT'] in '1/2' or record.samples[0]['GT'] in '1|2' or record.samples[0]['GT'] in '3/4':
        a01 = a01 + 1

    if record.samples[0]['GT'] in '1/1' or record.samples[0]['GT'] in '1|1' or record.samples[0]['GT'] in '2/2'or record.samples[0]['GT'] in '3|3':
        a11 = a11 + 1
    for i in record.samples[0].data:
        list0.append(str(i))
        if (len(list0) == 9)|(len(list0)==15):
            list0.append('')
        else:
            list0.append(':')
    ar0 = "".join(list0)


#  #310001 0
#     if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
#         u00 = u00 + 1

#     if record.samples[1]['GT'] in '0/1' or record.samples[1]['GT'] in '0|1' or record.samples[1]['GT'] in '1/2'  or record.samples[1]['GT'] in '1|2':
#         u01 = u01 + 1
  
#     if record.samples[1]['GT'] in '1/1' or record.samples[1]['GT'] in '1|1' or record.samples[1]['GT'] in '2/2' or record.samples[1]['GT'] in '2|2' or record.samples[1]['GT'] in '3/3' or record.samples[1]['GT'] in '3|3':
#         u11 = u11 + 1

#     for i in record.samples[1].data:
#         list1.append(str(i))
#         if (len(list1) == 9)|(len(list1)==15):
#             list1.append('')
#         else:
#             list1.append(':')
#     ar1 = "".join(list1)
    
    
# #310010 1
#     if record.samples[2]['GT'] in '0/0' or record.samples[2]['GT'] in './.':
#         a00 = a00 + 1

#     if record.samples[2]['GT'] in '0/1'or record.samples[2]['GT'] in '0|1' or record.samples[2]['GT'] in '1/2' or record.samples[2]['GT'] in '2/3':
#         a01 = a01 + 1

#     if record.samples[2]['GT'] in '1/1' or record.samples[2]['GT'] in '1|1' or record.samples[2]['GT'] in '2/2' or record.samples[2]['GT'] in '2|2' or record.samples[2]['GT'] in '3|3' or record.samples[2]['GT'] in '3/3':
#         a11 = a11 + 1

#     for i in record.samples[2].data:
#         list2.append(str(i))
#         if (len(list2) == 9)|(len(list2)==15):
#             list2.append('')
#         else:
#             list2.append(':')
#     ar2 = "".join(list2)


 #3101 1
    if record.samples[3]['GT'] in '0/0' or record.samples[3]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[3]['GT'] in '0/1'or record.samples[3]['GT'] in '0|1' or record.samples[3]['GT'] in '1/2' or record.samples[3]['GT'] in '1|2': 
        a01 = a01 + 1

    if record.samples[3]['GT'] in '1/1' or record.samples[3]['GT'] in '1|1' or record.samples[3]['GT'] in '2/2' or record.samples[3]['GT'] in '2|2' or record.samples[3]['GT'] in '3/3':
        a11 = a11 + 1
 
    for i in record.samples[3].data:
        list3.append(str(i))
        if (len(list3) == 9)|(len(list3)==15):
            list3.append('')
        else:
            list3.append(':')
    ar3 = "".join(list3)



#31010 1
    if record.samples[4]['GT'] in '0/0' or record.samples[4]['GT'] in './.':
        a00 = a00 + 1
 
    if record.samples[4]['GT'] in '0/1' or record.samples[4]['GT'] in '0|1' or record.samples[4]['GT'] in '1/2' or record.samples[4]['GT'] in '1|2':
        a01 = a01 + 1

    if record.samples[4]['GT'] in '1/1' or record.samples[4]['GT'] in '1|1' or record.samples[4]['GT'] in '2/2' or record.samples[4]['GT'] in '2|2' or record.samples[4]['GT'] in '3/3':
        a11 = a11 + 1

    for i in record.samples[4].data:
        list4.append(str(i))
        if (len(list4) == 9)|(len(list4)==15):
            list4.append('')
        else:
            list4.append(':')
    ar4 = "".join(list4)



    pos=record.POS
    ref=record.REF
    i_d = str(pos)+new
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
#    print a00,a01,a11,u00,u01,u11
    writer.writerow([i_d,new,pos,ref,alt,forma,ar0,ar3,ar4,a00,a01,a11,u00,u01,u11])
