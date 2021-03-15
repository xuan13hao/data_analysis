# -*- coding: utf-8 -*-
import csv
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


filename = '/home/xuan/Desktop/fam300annovar/AnoFam489.csv'
df= pd.read_csv(filename,encoding = "utf-8")
j1= df[(df['Func.refGene'].astype(str) != 'intergenic') & (df['Func.refGene'].astype(str) != 'intronic')&(df['Func.refGene'].astype(str) != 'ncRNA_intronic')&((df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_all'].astype(str) == "–"))]
#j2= (df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05)
#j3= (df['1000g2015aug_all'].astype(str) == "–")
#sub=df[j1&(j2|j3)]
#sub1=df[(df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05)| (df['1000g2015aug_all'] in "–")]
#sub=df[df['1000g2015aug_all'].astype(str) == "–"]
#j1=df[(df['Func.refGene'].astype(str) != 'intergenic') & (df['Func.refGene'].astype(str) != 'intronic')]
print j1
j1.to_csv('./ann_489data.csv', index=False, sep=',', quoting=csv.QUOTE_NONNUMERIC) 
