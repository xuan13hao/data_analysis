#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/h392x566/Project_Folder/genetic_project/genetic_disease/famdata/Fam315_genotypes_VQSR.vcf.gz'
#########################
row0=["Index","CHROM","Start","REF","ALT","FORMAT","sample31530","sample31532","sample31533","sample31534","OmniAffected GT 0/0","OmniAffected GT 0/1","OmniAffected GT 1/1","OmniUnaffected GT 0/0","OmniUnaffected GT 0/1","OmniUnaffected GT 1/1"]
csvfile =file('./FamCsv/Fam315c.csv', 'wb')
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

    
    #31530 0
    if record.samples[15]['GT'] in '0/0' or record.samples[15]['GT'] in './.':
        u00 = u00 + 1

    if record.samples[15]['GT'] in '0/1' or record.samples[15]['GT'] in '0|1' or record.samples[15]['GT'] in '1/2'  or record.samples[15]['GT'] in '1|2':
        u01 = u01 + 1
        
    if record.samples[15]['GT'] in '1/1' or record.samples[15]['GT'] in '1|1' or record.samples[15]['GT'] in '2/2' or record.samples[15]['GT'] in '2|2' or record.samples[15]['GT'] in '3/3':
        u11 = u11 + 1
        
    for i in record.samples[15].data:
        list15.append(str(i))
        if (len(list15) == 9)|(len(list15)==15):
            list15.append('')
        else:
            list15.append(':')
    ar15 = "".join(list15)
    
    
    #31532 M3293 0
    if record.samples[16]['GT'] == '0/0' or record.samples[16]['GT'] == './.':
        u00 = u00 + 1

    if record.samples[16]['GT'] in '0/1' or record.samples[16]['GT'] in '0|1' or record.samples[16]['GT'] in '1/2' or record.samples[16]['GT'] in '1|2':
        u01 = u01 + 1
        
    if record.samples[16]['GT'] in '1/1' or record.samples[16]['GT'] in '1|1' or record.samples[16]['GT'] in '2/2' or record.samples[16]['GT'] in '3/3' or record.samples[16]['GT'] in '2|2':
        u11 = u11 + 1
        
    for i in record.samples[16].data:
        list16.append(str(i))
        if (len(list16) == 9)|(len(list16)==15):
            list16.append('')
        else:
            list16.append(':')
    ar16 = "".join(list16)
    
    
    # 31533 M3294 1
    if record.samples[17]['GT'] in '0/0' or record.samples[17]['GT'] in './.':
        a00 = a00 + 1
       
    if record.samples[17]['GT'] in '0/1' or record.samples[17]['GT'] in '0|1' or record.samples[17]['GT'] in '1/2' or record.samples[17]['GT'] in '1|2':
        a01 = a01 + 1
 
    if record.samples[17]['GT'] in '1/1' or record.samples[17]['GT'] in '1|1' or record.samples[17]['GT'] in '2/2' or record.samples[17]['GT'] in '2|2' or record.samples[17]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[17].data:
        list17.append(str(i))
        if (len(list17) == 9)|(len(list17)==15):
            list17.append('')
        else:
            list17.append(':')
    ar17 = "".join(list17)

    #31534 1
    if record.samples[18]['GT'] in '0/0' or record.samples[18]['GT'] in './.':
        a00 = a00 + 1
       
    if record.samples[18]['GT'] in '0/1' or record.samples[18]['GT'] in '0|1' or record.samples[18]['GT'] in '1/2' or record.samples[18]['GT'] in '1|2':
        a01 = a01 + 1

    if record.samples[18]['GT'] in '1/1' or record.samples[18]['GT'] in '1|1' or record.samples[18]['GT'] in '2/2' or record.samples[18]['GT'] in '2|2' or record.samples[18]['GT'] in '3/3':
        a11 = a11 + 1
        
    for i in record.samples[18].data:
        list18.append(str(i))
        if (len(list18) == 9)|(len(list18)==15):
            list18.append('')
        else:
            list18.append(':')
    ar18 = "".join(list18)


    pos=record.POS
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
    i_d = str(pos)+new
#    print pos,ar2,a00,a01,a11,u00,u01,u11
    writer.writerow([i_d,new,pos,ref,alt,forma,ar15,ar16,ar17,ar18,a00,a01,a11,u00,u01,u11])
