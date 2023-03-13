#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/h392x566/Project_Folder/genetic_project/genetic_disease/famdata/genotypes_VQSR_Fam493.vcf.gz'
#########################
row0=["Index","CHROM","Start","REF","ALT","FORMAT","sample493","sample4931","sample49310","sample4932","sample49320","sample493211","sample49322","sample49323","sample49324","sample4933","sample4934","OmniAffected GT 0/0","OmniAffected GT 0/1","OmniAffected GT 1/1","OmniUnaffected GT 0/0","OmniUnaffected GT 0/1","OmniUnaffected GT 1/1"]
csvfile = file('./FamCsv/Fam493_11_16.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
#########################
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
    # ar3 =''
    # ar4=''
    # ar5=''
    pos=''
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    altlist = []
    new=record.CHROM
    #493 1
    if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[0]['GT'] in '0/1' or record.samples[0]['GT'] in '0|1' or record.samples[0]['GT'] in '1/2' or record.samples[0]['GT'] in '2/4' or record.samples[0]['GT'] in '1|2' or record.samples[0]['GT'] in '2/3':
        a01 = a01 + 1
        
    if record.samples[0]['GT'] in '1/1' or record.samples[0]['GT'] in '1|1' or record.samples[0]['GT'] in '2/2' or record.samples[0]['GT'] in '2|2' or record.samples[0]['GT'] in '3/3':
        a11 = a11 + 1

    for i in record.samples[0].data:
        list0.append(str(i))
        if (len(list0) == 9)|(len(list0)==15):
            list0.append('')
        else:
            list0.append(':')
    ar0 = "".join(list0)



    #4931 1
    if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
        a00 = a00 + 1
       
    if record.samples[1]['GT'] in '0/1' or record.samples[1]['GT'] in '0|1' or record.samples[1]['GT'] in '1/2' or record.samples[1]['GT'] in '2/4' or record.samples[1]['GT'] in '1|2' or record.samples[1]['GT'] in '2/3':
        a01 = a01 + 1
 
    if record.samples[1]['GT'] in '1/1' or record.samples[1]['GT'] in '1|1' or record.samples[1]['GT'] in '2/2' or record.samples[1]['GT'] in '2|2' or record.samples[1]['GT'] in '3/3':
        a11 = a11 + 1

    
    for i in record.samples[1].data:
        list1.append(str(i))
        if (len(list1) == 9)|(len(list1)==15):
            list1.append('')
        else:
            list1.append(':')
    ar1 = "".join(list1)

    #49310 1
    if record.samples[2]['GT'] in '0/0' or record.samples[2]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[2]['GT'] in '0/1' or record.samples[2]['GT'] in '0|1' or record.samples[2]['GT'] in '3/4' or record.samples[2]['GT'] in '4/6' or record.samples[2]['GT'] in '1|2' or record.samples[2]['GT'] in '1/2' or record.samples[2]['GT'] in '2/3':
        a01 = a01 + 1
 
    if record.samples[2]['GT'] in '1/1' or record.samples[2]['GT'] in '1|1' or record.samples[2]['GT'] in '2/2' or record.samples[2]['GT'] in '2|2' or record.samples[2]['GT'] in '3/3' or record.samples[2]['GT'] in '3|3':
        a11 = a11 + 1

    for i in record.samples[2].data:
        list2.append(str(i))
        if (len(list2) == 9)|(len(list2)==15):
            list2.append('')
        else:
            list2.append(':')
    ar2 = "".join(list2)

    #4932 1
    if record.samples[3]['GT'] in '0/0' or record.samples[3]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[3]['GT'] in '0/1' or record.samples[3]['GT'] in '0|1' or record.samples[3]['GT'] in '2/4' or record.samples[3]['GT'] in '3/4'  or record.samples[3]['GT'] in '1/2' or record.samples[3]['GT'] in '1|2' or record.samples[3]['GT'] in '2/3':
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


    #49320 1
    if record.samples[4]['GT'] in '0/0' or record.samples[4]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[4]['GT'] in '0/1' or record.samples[4]['GT'] in '0|1' or record.samples[4]['GT'] in '1/2' or record.samples[4]['GT'] in '1|2' or record.samples[4]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[4]['GT'] in '1/1' or record.samples[4]['GT'] in '1|1' or record.samples[4]['GT'] in '4/4' or record.samples[4]['GT'] in '2/2' or record.samples[4]['GT'] in '2|2' or record.samples[4]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[4].data:
        list4.append(str(i))
        if (len(list4) == 9)|(len(list4)==15):
            list4.append('')
        else:
            list4.append(':')
    ar4 = "".join(list4)

    # #493211 0
    # if record.samples[5]['GT'] in '0/0' or record.samples[5]['GT'] in './.':
    #     u00 = u00 + 1

    # if record.samples[5]['GT'] in '0/1' or record.samples[5]['GT'] in '0|1' or record.samples[5]['GT'] in '1/2' or record.samples[5]['GT'] in '3/4' or record.samples[5]['GT'] in '5/6' or record.samples[5]['GT'] in '2/3' or record.samples[5]['GT'] in '2/6' or record.samples[5]['GT'] in '1/4' or record.samples[5]['GT'] in '1/5':
    #     u01 = u01 + 1

    # if record.samples[5]['GT'] in '1/1' or record.samples[5]['GT'] in '1|1' or record.samples[5]['GT'] in '2/2' or record.samples[5]['GT'] in '2|2' or record.samples[5]['GT'] in '4/4' or record.samples[5]['GT'] in '5/5' or record.samples[5]['GT'] in '3/3':
    #     u11 = u11 + 1

    # for i in record.samples[5].data:
    #     list5.append(str(i))
    #     if (len(list5) == 9)|(len(list5)==15):
    #         list5.append('')
    #     else:
    #         list5.append(':')
    # ar5 = "".join(list5)

    #49322 1
    if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[6]['GT'] in '0/1' or record.samples[6]['GT'] in '0|1' or record.samples[6]['GT'] in '1/2' or record.samples[6]['GT'] in '1|2' or record.samples[6]['GT'] in '2/3' or record.samples[6]['GT'] in '3/5' or record.samples[6]['GT'] in '3/6' or record.samples[6]['GT'] in '4/5':
        a01 = a01 + 1

        
    if record.samples[6]['GT'] in '1/1' or record.samples[6]['GT'] in '1|1' or record.samples[6]['GT'] in '2/2' or record.samples[6]['GT'] in '5/5' or record.samples[6]['GT'] in '2|2' or record.samples[6]['GT'] in '3/3' or record.samples[6]['GT'] in '3|3':
        a11 = a11 + 1
        
    for i in record.samples[6].data:
        list6.append(str(i))
        if (len(list6) == 9)|(len(list6)==15):
            list6.append('')
        else:
            list6.append(':')
    ar6 = "".join(list6)

    #49323 0
    if record.samples[7]['GT'] in '0/0' or record.samples[7]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[7]['GT'] in '0/1' or record.samples[7]['GT'] in '0|1' or record.samples[7]['GT'] in '1/2' or record.samples[7]['GT'] in '3/5' or record.samples[7]['GT'] in '1|2' or record.samples[7]['GT'] in '2/3':
        u01 = u01 + 1

    if record.samples[7]['GT'] in '1/1' or record.samples[7]['GT'] in '1|1' or record.samples[7]['GT'] in '4/4' or record.samples[7]['GT'] in '6/6' or record.samples[7]['GT'] in '2/2' or record.samples[7]['GT'] in '2|2' or record.samples[7]['GT'] in '3/3':
        u11 = u11 + 1
    for i in record.samples[7].data:
        list7.append(str(i))
        if (len(list7) == 9)|(len(list7)==15):
            list7.append('')
        else:
            list7.append(':')
    ar7 = "".join(list7)

    #49324 1
    if record.samples[8]['GT'] in '0/0' or record.samples[8]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[8]['GT'] in '0/1' or record.samples[8]['GT'] in '0|1' or record.samples[8]['GT'] in '3/5' or record.samples[8]['GT'] in '3/4' or record.samples[8]['GT'] in '3/6' or record.samples[8]['GT'] in '1/2' or record.samples[8]['GT'] in '1|2' or record.samples[8]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[8]['GT'] in '1/1' or record.samples[8]['GT'] in '1|1' or record.samples[8]['GT'] in '2/2' or record.samples[8]['GT'] in '5/5' or record.samples[8]['GT'] in '4/4' or record.samples[8]['GT'] in '2|2' or record.samples[8]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[8].data:
        list8.append(str(i))
        if (len(list8) == 9)|(len(list8)==15):
            list8.append('')
        else:
            list8.append(':')
    ar8 = "".join(list8)

    #4933 0
    if record.samples[9]['GT'] in '0/0' or record.samples[9]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[9]['GT'] in '0/1' or record.samples[9]['GT'] in '0|1' or record.samples[9]['GT'] in '3/4' or record.samples[9]['GT'] in '3/6' or record.samples[9]['GT'] in '1/2' or record.samples[9]['GT'] in '1|2' or record.samples[9]['GT'] in '2/3':
        u01 = u01 + 1
        
    if record.samples[9]['GT'] in '1/1' or record.samples[9]['GT'] in '1|1' or record.samples[9]['GT'] in '5/5' or record.samples[9]['GT'] in '2/2' or record.samples[9]['GT'] in '2|2' or record.samples[9]['GT'] in '3/3':
        u11 = u11 + 1
        
    for i in record.samples[9].data:
        list9.append(str(i))
        if (len(list9) == 9)|(len(list9)==15):
            list9.append('')
        else:
            list9.append(':')
    ar9 = "".join(list9)
# 4934 1
    if record.samples[10]['GT'] in '0/0' or record.samples[10]['GT'] in './.':
        a00 = a00 + 1

    if record.samples[10]['GT'] in '0/1' or record.samples[10]['GT'] in '0|1' or record.samples[10]['GT'] in '3/6' or record.samples[10]['GT'] in '1/2' or record.samples[10]['GT'] in '1|2' or record.samples[10]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[10]['GT'] in '1/1' or record.samples[10]['GT'] in '1|1' or record.samples[10]['GT'] in '4/4' or record.samples[10]['GT'] in '5/5' or record.samples[10]['GT'] in '2/2' or record.samples[10]['GT'] in '2|2' or record.samples[10]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[10].data:
        list10.append(str(i))
        if (len(list10) == 9)|(len(list10)==15):
            list10.append('')
        else:
            list10.append(':')
    ar10 = "".join(list10)

    pos=record.POS
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
    i_d = str(pos)+new
#    print a00,a01,a11,u00,u01,u11
    writer.writerow([i_d,new,pos,ref,alt,forma,ar0,ar1,ar2,ar3,ar4,ar6,ar7,ar8,ar9,ar10,a00,a01,a11,u00,u01,u11])
