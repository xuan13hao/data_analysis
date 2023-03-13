#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/h392x566/Project_Folder/genetic_project/genetic_disease/famdata/Fam315_genotypes_VQSR.vcf.gz'
#########################
row0=["Index","CHROM","Start","REF","ALT","FORMAT","sample31520","sample31521","sample31522","sample31522001","sample31522002","sample31523","sample31523010","sample31524","OmniAffected GT 0/0","OmniAffected GT 0/1","OmniAffected GT 1/1","OmniUnaffected GT 0/0","OmniUnaffected GT 0/1","OmniUnaffected GT 1/1"]
csvfile =file('./FamCsv/Fam315b.csv', 'wb')
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
    ar3=''
    ar4=''
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
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    altlist = []
    new=record.CHROM

    
    

    #31520 0
    if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[6]['GT'] in '0/1' or record.samples[6]['GT'] in '0|1' or record.samples[6]['GT'] in '1/2':
        u01 = u01 + 1
        
    if record.samples[6]['GT'] in '1/1' or record.samples[6]['GT'] in '1|1' or record.samples[6]['GT'] in '2/2':
        u11 = u11 + 1
       
    for i in record.samples[6].data:
        list6.append(str(i))
        if (len(list6) == 9)|(len(list6)==15):
            list6.append('')
        else:
            list6.append(':')
    ar6 = "".join(list6)
    
    
    #31521 0
    if record.samples[7]['GT'] in '0/0' or record.samples[7]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[7]['GT'] in '0/1' or record.samples[7]['GT'] in '0|1' or record.samples[7]['GT'] in '1/2' or record.samples[7]['GT'] in '1|2':
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
    
    
    #31522 1
    if record.samples[8]['GT'] in '0/0' or record.samples[8]['GT'] in './.':
        a00 = a00 + 1
 
    if record.samples[8]['GT'] in '0/1' or record.samples[8]['GT'] in '0|1' or record.samples[8]['GT'] in '1/2' or record.samples[8]['GT'] in '1|2':
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

    #31522001 1
    if record.samples[9]['GT'] in '0/0' or record.samples[9]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[9]['GT'] in '0/1' or record.samples[9]['GT'] in '0|1' or record.samples[9]['GT'] in '1/2' or record.samples[9]['GT'] in '1|2':
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

    #31522002 M8988 1
    if record.samples[10]['GT'] in '0/0' or record.samples[10]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[10]['GT'] in '0/1' or record.samples[10]['GT'] in '0|1' or record.samples[10]['GT'] in '1/2' or record.samples[10]['GT'] in '1|2':
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

    #31523 1
    if record.samples[11]['GT'] in '0/0' or record.samples[11]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[11]['GT'] in '0/1' or record.samples[11]['GT'] in '0|1' or record.samples[11]['GT'] in '1/2' or record.samples[11]['GT'] in '1|2':
        a01 = a01 + 1
       
    if record.samples[11]['GT'] in '1/1' or record.samples[11]['GT'] in '1|1' or record.samples[11]['GT'] in '2/2'  or record.samples[11]['GT'] in '2|2' or record.samples[11]['GT'] in '3/3':
        a11 = a11 + 1
    for i in record.samples[11].data:
        list11.append(str(i))
        if (len(list11) == 9)|(len(list11)==15):
            list11.append('')
        else:
            list11.append(':')
    ar11 = "".join(list11)

    #31523010 1
    if record.samples[12]['GT'] in '0/0' or record.samples[12]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[12]['GT'] in '0/1' or record.samples[12]['GT'] in '0|1' or record.samples[12]['GT'] in '1/2'  or record.samples[12]['GT'] in '1|2':
        a01 = a01 + 1
       
    if record.samples[12]['GT'] in '1/1' or record.samples[12]['GT'] in '1|1' or record.samples[12]['GT'] in '2/2'  or record.samples[12]['GT'] in '2|2'  or record.samples[12]['GT'] in '3/3':
        a11 = a11 + 1
    for i in record.samples[12].data:
        list12.append(str(i))
        if (len(list12) == 9)|(len(list12)==15):
            list12.append('')
        else:
            list12.append(':')
    ar12 = "".join(list12)

    #31524 M3300 1
    if record.samples[13]['GT'] in '0/0' or record.samples[13]['GT'] in './.':
        a00 = a00 + 1
        
    if record.samples[13]['GT'] in '0/1' or record.samples[13]['GT'] in '0|1' or record.samples[13]['GT'] in '1/2' or record.samples[13]['GT'] in '1|2':
        a01 = a01 + 1
 
    if record.samples[13]['GT'] in '1/1' or record.samples[13]['GT'] in '1|1' or record.samples[13]['GT'] in '2/2' or record.samples[13]['GT'] in '2|2' or record.samples[13]['GT'] in '3/3':
        a11 = a11 + 1
 
    for i in record.samples[13].data:
        list13.append(str(i))
        if (len(list13) == 9)|(len(list13)==15):
            list13.append('')
        else:
            list13.append(':')
    ar13 = "".join(list13)
    
    


    pos=record.POS
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
    i_d = str(pos)+new
#    print pos,ar2,a00,a01,a11,u00,u01,u11
    writer.writerow([i_d,new,pos,ref,alt,forma,ar6,ar7,ar8,ar9,ar10,ar11,ar12,ar13,a00,a01,a11,u00,u01,u11])
