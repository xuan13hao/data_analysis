#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'/home/h392x566/genetic_project/genetic_disease/test/Fam300_genotypes_VQSR_1.vcf'
#########################
row0=[" ","POS","ID","REF","ALT","QUAL","FILTER","A-0/0","A-0/1","A-1/1","U-0/0","U-0/1","U-1/1","REF","ALT","QUAL","FILTER"]
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(row0)
#########################
str1=''
str2=''
str3=''
str4=''
str5=''
str6=''
pos=''
ID=''
ref=''
alt=''
qual=''
Filter=''
vcf_reader = vcf.Reader(filename=filename) 
record = next(vcf_reader)
for record in vcf_reader:  
        a00=''
        a01=''
        a11=''
        u00=''
        u01=''
        u11=''
        new=record.CHROM
        if record.samples[0]['GT'] in '0/0' or record.samples[0]['GT'] in './.':
            a00 = a00 + 1
        if record.samples[0]['GT'] in '0/1':
            a01 = a01 + 1
        if record.samples[0]['GT'] in '1/1':
            a11 = a11 + 1
        if record.samples[1]['GT'] in '0/0' or record.samples[1]['GT'] in './.':
            a00 = a00 + 1
        if record.samples[1]['GT'] in '0/1':
            a01 = a01 + 1
        if record.samples[1]['GT'] in '1/1':
            a11 = a11 + 1
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
        if record.samples[5]['GT'] in '0/1':
            a01 = a01 + 1
        if record.samples[5]['GT'] in '1/1':
            a11 = a11 + 1
        if record.samples[6]['GT'] in '0/0' or record.samples[6]['GT'] in './.':
            a00 = a00 + 1
        if record.samples[6]['GT'] in '0/1':
            a01 = a01 + 1
        if record.samples[6]['GT'] in '1/1':
            a11 = a11 + 1
        str1=str(a00)
        str2=str(a01)
        str3=str(a11)
        str4=str(u00)
        str5=str(u01)
        str6=str(u11)
        ref=record.REF
        alt=record.ALT
        forma=record.FORMAT
        print forma      
     #   writer.writerow([new,pos,ID,ref,alt,qual,Filter,str1,str2,str3,str4,str5,str6])

