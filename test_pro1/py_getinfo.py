#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
# File path####################################
filename = r'../Fam300_genotypes_VQSR_1.vcf.gz'
#########################
row0=[" ","POS","ID","REF","ALT","QUAL","FILTER","INFO.AC","INFO.AF","INFO.AN","INFO.BaseQRankSum","INFO.DP","INFO.ExcessHet","INFO.FS","INFO.MLEAC","INFO.MLEAF","INFO.MQ","INFO.MQRANKSUM","INFO.QD","INFO.ReadPosRankSum","INFOSQR","INFO.VQSL0D","INFO.culprit","A-0/0","A-0/1","A-1/1","U-0/0","U-0/1","U-1/1"]
#import xlwt
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
af=''
vcf_reader = vcf.Reader(filename=filename) 
#record = next(vcf_reader)
for record in vcf_reader:  
       # print ",".join(str(record.INFO['AC']) for i in record.INFO['AC'])
       # print record.INFO['AF']
        for row in record.INFO['AF']:
         #   af.append(row)
            print row
       # print record.INFO['FS']
       # print record.INFO['ExcessHet']
       # print record.INFO['AN']


