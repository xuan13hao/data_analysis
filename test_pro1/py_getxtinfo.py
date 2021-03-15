#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import vcf
import csv
import codecs
import numpy as np
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
########################################
with open('/home/h392x566/genetic_project/genetic_disease/Fam300_csv.csv', 'rb') as f:
    reader = csv.reader(f)
    for r in reader:
        print r
"""
f = codecs.open('../../TableTest.hg19_multianno.txt', mode='r', encoding='utf-8')
line=f.readline()
list1=[]
vcf_reader = vcf.Reader(filename=filename) 
while line:
    a = line.split()
    b = a[0:2]  # 这是选取需要读取的位数
    list1.append(b) # 将其添加在列表之中
    line = f.readline()
f.close()
 
for i in list1:
    print(i)




#record = next(vcf_reader)##############
for record in vcf_reader:  
            print record.INFO['AF']
            print record.INFO['DP']
            print record.INFO['FS']
            print record.INFO['ExcessHet']
            print record.INFO['AN']

#########################################
"""
