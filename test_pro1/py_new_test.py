#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/xuan/genetic_disease/test/Fam300_genotypes_VQSR_1.vcf'
#########################
row0=["CHROM","POS","REF","ALT","FORMAT","M3328.processed.vcf","M3329.processed.vcf","M3622,processed.vcf","Num_Group1","Num_Group2"]
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
#########################
vcf_reader = vcf.Reader(filename=filename) 
record = next(vcf_reader)
for record in vcf_reader:  
    a00=''
    a01=''
    a11=''
    af0=0
    uaf=0
    temp=''
    list1 = []
    list2 = []
    list3 = []
    altlist = []
    new=record.CHROM
    if (str(record.samples[0]['GT']) in str('0/0')) or (str(record.samples[0]['GT']) in str('./.')):
        a00 = '-'
    else:
        af0 = af0+1
        for i in record.samples[0].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        a00 = "".join(list1)

    if (str(record.samples[1]['GT']) in str('0/0')) or (str(record.samples[1]['GT']) in str('./.')):
        a01 = '-'
    else:
        for i in record.samples[1].data:
            list2.append(str(i))
            if (len(list2) == 9)|(len(list2)==15):
                list2.append('')
            else:
                list2.append(':')
        a01 = "".join(list2)


    if (str(record.samples[3]['GT']) in str('0/0')) or (str(record.samples[3]['GT']) in str('./.')):
        a11 = '-'
    else:
        af0 = af0+1
        for i in record.samples[3].data:
            list3.append(str(i))
            if (len(list3) == 9)|(len(list3)==15):
                list3.append('')
            else:
                list3.append(':')
        a11 = "".join(list3)


    pos=record.POS
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
    writer.writerow([new,pos,ref,alt,forma,a00,a01,a11,af0,uaf])
