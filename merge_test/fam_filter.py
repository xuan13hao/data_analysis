# -*- coding: utf-8 -*-
import csv
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#filename = '/home/xuan/annova_csv/FAM_CSV/Fam300ANOVAR.csv'
filename1 = './test.csv'
#df= pd.read_csv(filename1,encoding = "utf-8")
df= pd.read_csv(filename1,encoding = "utf-8",delimiter="\t")
j1= df[(df['Func.refGene'].astype(str) != 'intergenic') & (df['Func.refGene'].astype(str) != 'intronic')&(df['Func.refGene'].astype(str) != 'ncRNA_intronic')&((df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_all'].astype(str) == "–"))&((df["1000g2015aug_afr"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_afr'].astype(str) == "–"))&((df["1000g2015aug_amr"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_amr'].astype(str) == "–"))&((df["1000g2015aug_eas"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_eas'].astype(str) == "–"))&((df["1000g2015aug_eur"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_eur'].astype(str) == "–"))&((df["1000g2015aug_sas"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05) | (df['1000g2015aug_sas'].astype(str) == "–"))]
#j2= (df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05)
#j3= (df['1000g2015aug_all'].astype(str) == "–")
#sub=df[j1&(j2|j3)]
#sub1=df[(df["1000g2015aug_all"].apply(pd.to_numeric, downcast='float', errors='coerce') < 0.05)| (df['1000g2015aug_all'] in "–")]
#sub=df[df['1000g2015aug_all'].astype(str) == "–"]
#j1=df[(df['Func.refGene'].astype(str) != 'intergenic') & (df['Func.refGene'].astype(str) != 'intronic')]
print j1
j1.to_csv('./test_f.csv', index=False, sep=',', quoting=csv.QUOTE_NONNUMERIC) 
