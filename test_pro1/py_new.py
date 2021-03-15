#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/xuan/genetic_disease/test/Fam300_genotypes_VQSR_1.vcf'
#########################
row0=["CHROM","POS","REF","ALT","FORMAT","M3328.processed.vcf","M3329.processed.vcf","M3622,processed.vcf","Affected GT 0/0","Affected GT 0/1","Affected GT 1/1","Unaffected GT 0/0","Unaffected GT 0/1","Unaffected GT 1/1"]
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
#########################
vcf_reader = vcf.Reader(filename=filename) 
record = next(vcf_reader)
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
    pos=''
    list1 = []
    list2 = []
    list3 = []
    altlist = []
    new=record.CHROM
    if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
        a00 = a00 + 1
        ar0 = '-'
    if record.samples[0]['GT'] in '0/1':
        a01 = a01 + 1
        for i in record.samples[0].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar0 = "".join(list1)
    if record.samples[0]['GT'] in '1/1':
        a11 = a11 + 1
        for i in record.samples[0].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar0 = "".join(list1)
    if record.samples[0]['GT'] in '2/2' or record.samples[0]['GT'] in '2/3':
        for i in record.samples[0].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar0 = "".join(list1)
    if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
        a00 = a00 + 1
        ar1 = '-'
    if record.samples[1]['GT'] in '0/1':
        a01 = a01 + 1
        for i in record.samples[1].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar1 = "".join(list1)
    if record.samples[1]['GT'] in '1/1':
        a11 = a11 + 1
        for i in record.samples[1].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar1 = "".join(list1)
    if record.samples[1]['GT'] in '2/2' or record.samples[1]['GT'] in '2/3':
        for i in record.samples[1].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar1 = "".join(list1)
    if record.samples[2]['GT'] in '0/0' or record.samples[2]['GT'] in './.':
        u00 = u00 + 1
    if record.samples[2]['GT'] in '0/1':
        u01 = u01 + 1
    if record.samples[2]['GT'] in '1/1':
        u11 = u11 + 1
    if record.samples[3]['GT'] in '0/0' or record.samples[3]['GT'] in './.':
        u00 = u00 + 1
    if record.samples[3]['GT'] in '0/1':
        u01 = u01 + 1
    if record.samples[3]['GT'] in '1/1':
        u11 = u11 + 1
    if record.samples[4]['GT'] in '0/0' or record.samples[4]['GT'] in './.':
        a00 = a00 + 1
    if record.samples[4]['GT'] in '0/1':
        a01 = a01 + 1
    if record.samples[4]['GT'] in '1/1':
        a11 = a11 + 1
    if record.samples[5]['GT'] in '0/0' or record.samples[5]['GT'] in './.':
        a00 = a00 + 1
        ar2 = '-'
    if record.samples[5]['GT'] in '0/1':
        a01 = a01 + 1
        for i in record.samples[5].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar2 = "".join(list1)
    if record.samples[5]['GT'] in '1/1':
        a11 = a11 + 1
        for i in record.samples[5].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar2 = "".join(list1)
    if record.samples[5]['GT'] in '2/2' or record.samples[5]['GT'] in '2/3':
        for i in record.samples[5].data:
            list1.append(str(i))
            if (len(list1) == 9)|(len(list1)==15):
                list1.append('')
            else:
                list1.append(':')
        ar2 = "".join(list1)
    if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
        a00 = a00 + 1
    if record.samples[6]['GT'] in '0/1':
        a01 = a01 + 1
    if record.samples[6]['GT'] in '1/1':
        a11 = a11 + 1
    pos=record.POS
    ref=record.REF
    for r in record.ALT:
        altlist.append(str(r))
    alt="".join(altlist)
    forma=record.FORMAT
#    print a00,a01,a11,u00,u01,u11,ar0,ar1,ar2
    writer.writerow([new,pos,ref,alt,forma,ar0,ar1,ar2,a00,a01,a11,u00,u01,u11])
