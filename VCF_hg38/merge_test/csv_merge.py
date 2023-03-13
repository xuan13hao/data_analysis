#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd

df1 = pd.read_csv(r'/home/xuan/genetic_disease/python_fam/FamCsv/Fam489.csv', encoding='utf8')#读取第一个文件

df2 = pd.read_csv(r'/home/xuan/genetic_disease/test/Index_CSV_filter/Fam489ANOVAR.csv', encoding='utf8')#读取第二个文件
#df1.join(df2, on='policyID')
#df1['Start'] = df1['Start'].astype(float)
print df1['Index'].dtypes
#print df2['Start'].astype(str).dtypes
print df2['Index'].dtypes
#df['Num_Detections'] = pd.to_numeric(df['Num_Detections'], errors='coerce')
#df1['Start'] = pd.to_numeric(df1['Start'], errors='coerce')
#df2['Start'] = pd.to_numeric(df2['Start'], errors='coerce')
#print df1['Start'].dtypes
#df2['Start'] = df2['Start'].astype(float)

#out = pd.merge(df1,df2,on=['Start','Start'],how='inner')
#print df1['Pos']

#print out

#out = pd.join(df2, df1, on=None, how='left', lsuffix='policyID', rsuffix='policyID',sort=False)
#out.to_csv(r'/home/xuan/famdata/newFamcsv/Fam489new_0701.csv',encoding='utf8')
#outfile=pd.merge(df1, df2, left_on='policyID',, how='inner')
out = pd.merge(df1, df2,  left_on='Index', right_on='Index',how='inner')#文件合并 left_on左侧DataFrame中的列或索引级别用作键。right_on 右侧
print out
out.to_csv(r'/home/xuan/famdata/newFamcsv/Fam489_08_14.csv', index=False,encoding='utf8')#输出文件
