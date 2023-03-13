#-*- coding:utf-8 -*-
import vcf
import csv
import pandas as pd
# File path####################################
filename = r'../Fam300_genotypes_VQSR_1.vcf.gz'
csvfilename='../../Fam300_csv.csv'
list1=[]
with open(csvfilename,'rb') as cf:
       f_csv = csv.reader(cf)
       while 1:
           header=f_csv.next()
           print header 
