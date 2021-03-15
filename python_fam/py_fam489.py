#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/h392x566/Project_Folder/genetic_project/genetic_disease/famdata/Fam489_genotypes_VQSR.vcf.gz'
#########################
row0=["Index","CHROM",'Start',"REF","ALT","FORMAT","sample489","sample4891","sample48910","sample48911","sample4892","sample4893","sample4894","sample4895","sample4896","sample4897","sample4898","OmniAffected GT 0/0","OmniAffected GT 0/1","OmniAffected GT 1/1","OmniUnaffected GT 0/0","OmniUnaffected GT 0/1","OmniUnaffected GT 1/1"]
csvfile = file('./FamCsv/Fam489.csv', 'wb')
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
    ar0=''
    ar1=''
    ar2=''
    ar3 =''
    ar4=''
    ar5=''
    pos = 0
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
    
    #489 ar0 M9806 1
    if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[0]['GT'] in '0/1' or record.samples[0]['GT'] in '0|1' or record.samples[0]['GT'] in '1/2' or record.samples[0]['GT'] in '1|2' or record.samples[0]['GT'] in '2/3':
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



    #4891 ar1 M9807 1
    if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[1]['GT'] in '0/1' or record.samples[1]['GT'] in '0|1' or record.samples[1]['GT'] in '1/2' or record.samples[1]['GT'] in '1|2' or record.samples[1]['GT'] in '2/3':
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

    #48910 ar4 M9805 0
    if record.samples[2]['GT'] in '0/0' or record.samples[2]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[2]['GT'] in '0/1' or record.samples[2]['GT'] in '0|1' or record.samples[2]['GT'] in '1/2' or record.samples[2]['GT'] in '1|2'or record.samples[2]['GT'] in '2/3':
        u01 = u01 + 1
        
    if record.samples[2]['GT'] in '1/1' or record.samples[2]['GT'] in '1|1' or record.samples[2]['GT'] in '2/2' or record.samples[2]['GT'] in '2|2' or record.samples[2]['GT'] in '3/3':
        u11 = u11 + 1
        
    for i in record.samples[2].data:
        list2.append(str(i))
        if (len(list2) == 9)|(len(list2)==15):
            list2.append('')
        else:
            list2.append(':')
    ar2 = "".join(list2)
    #49811 ar5 M9804 1
    if record.samples[3]['GT'] in '0/0' or record.samples[3]['GT'] in './.':
        a00 = a00 + 1
       
    if record.samples[3]['GT'] in '0/1' or record.samples[3]['GT'] in '0|1' or record.samples[3]['GT'] in '1/2' or record.samples[3]['GT'] in '1|2' or record.samples[3]['GT'] in '2/3':
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


    #4892 1
    if record.samples[4]['GT'] in '0/0' or record.samples[4]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[4]['GT'] in '0/1' or record.samples[4]['GT'] in '0|1' or record.samples[4]['GT'] in '1/2' or record.samples[4]['GT'] in '1|2' or record.samples[4]['GT'] in '2/3':
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

    #4893 1
    if record.samples[5]['GT'] in '0/0' or record.samples[5]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[5]['GT'] in '0/1' or record.samples[5]['GT'] in '0|1' or record.samples[5]['GT'] in '1/2' or record.samples[5]['GT'] in '1|2' or record.samples[5]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[5]['GT'] in '1/1' or record.samples[5]['GT'] in '1|1' or record.samples[5]['GT'] in '2/2' or record.samples[5]['GT'] in '2|2' or record.samples[5]['GT'] in '3/3' or record.samples[5]['GT'] in '3|3':
        a11 = a11 + 1
        
    for i in record.samples[5].data:
        list5.append(str(i))
        if (len(list5) == 9)|(len(list5)==15):
            list5.append('')
        else:
            list5.append(':')
    ar5 = "".join(list5)

    #4894 ar2 M9810 0
    if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[6]['GT'] in '0/1' or record.samples[6]['GT'] in '0|1' or record.samples[6]['GT'] in '1/2' or record.samples[6]['GT'] in '1|2' or record.samples[6]['GT'] in '2/3':
        u01 = u01 + 1
        
    if record.samples[6]['GT'] in '1/1' or record.samples[6]['GT'] in '1|1' or record.samples[6]['GT'] in '2/2' or record.samples[6]['GT'] in '2|2' or record.samples[6]['GT'] in '3/3':
        u11 = u11 + 1
        
    for i in record.samples[6].data:
        list6.append(str(i))
        if (len(list6) == 9)|(len(list6)==15):
            list6.append('')
        else:
            list6.append(':')
    ar6 = "".join(list6)
    
    
    #4895 0
    if record.samples[7]['GT'] in '0/0' or record.samples[7]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[7]['GT'] in '0/1' or record.samples[7]['GT'] in '0|1' or record.samples[7]['GT'] in '1/2' or record.samples[7]['GT'] in '1|2' or record.samples[7]['GT'] in '2/3':
        u01 = u01 + 1
        
    if record.samples[7]['GT'] in '1/1' or record.samples[7]['GT'] in '1|1' or record.samples[7]['GT'] in '2/2' or record.samples[7]['GT'] in '2|2' or record.samples[7]['GT'] in '3/3':
        u11 = u11 + 1
        
    for i in record.samples[7].data:
        list7.append(str(i))
        if (len(list7) == 9)|(len(list7)==15):
            list7.append('')
        else:
            list7.append(':')
    ar7 = "".join(list7)

    #4896 1
    if record.samples[8]['GT'] in '0/0' or record.samples[8]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[8]['GT'] in '0/1' or record.samples[8]['GT'] in '0|1' or record.samples[8]['GT'] in '1/2' or record.samples[8]['GT'] in '1|2' or record.samples[8]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[8]['GT'] in '1/1' or record.samples[8]['GT'] in '1|1' or record.samples[8]['GT'] in '2/2' or record.samples[8]['GT'] in '2|2' or record.samples[8]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[8].data:
        list8.append(str(i))
        if (len(list8) == 9)|(len(list8)==15):
            list8.append('')
        else:
            list8.append(':')
    ar8 = "".join(list8)

    #4897 1
    if record.samples[9]['GT'] in '0/0' or record.samples[9]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[9]['GT'] in '0/1' or record.samples[9]['GT'] in '0|1' or record.samples[9]['GT'] in '1/2' or record.samples[9]['GT'] in '1|2' or record.samples[9]['GT'] in '2/3':
        a01 = a01 + 1

    if record.samples[9]['GT'] in '1/1' or record.samples[9]['GT'] in '1|1' or record.samples[9]['GT'] in '2/2' or record.samples[9]['GT'] in '2|2' or record.samples[9]['GT'] in '3/3':
        a11 = a11 + 1
    for i in record.samples[9].data:
        list9.append(str(i))
        if (len(list9) == 9)|(len(list9)==15):
            list9.append('')
        else:
            list9.append(':')
    ar9 = "".join(list9)

# 4898 ar3 M9814 1
    if record.samples[10]['GT'] in '0/0' or record.samples[10]['GT'] in './.':
        a00 = a00 + 1
       
    if record.samples[10]['GT'] in '0/1' or record.samples[10]['GT'] in '0|1' or record.samples[10]['GT'] in '1/2' or record.samples[10]['GT'] in '1|2' or record.samples[10]['GT'] in '2/3':
        a01 = a01 + 1
  
    if record.samples[10]['GT'] in '1/1' or record.samples[10]['GT'] in '1|1' or record.samples[10]['GT'] in '2/2' or record.samples[10]['GT'] in '2|2' or record.samples[10]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[10].data:
        list10.append(str(i))
        if (len(list10) == 9)|(len(list10)==15):
            list10.append('')
        else:
            list10.append(':')
    ar10 = "".join(list10)


    new=record.CHROM
    pos=record.POS
    i_d = str(pos)+new
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
#    print pos,ar1,a00,a01,a11,u00,u01,u11
    writer.writerow([i_d,new,pos,ref,alt,forma,ar0,ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,a00,a01,a11,u00,u01,u11])
