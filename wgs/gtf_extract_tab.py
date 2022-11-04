# pip install gtfparse, pandas, pysam
# python3 gtf_extract.py match_tab SIRV_E2C.gtf 
from distutils.command.build import build
from gtfparse import read_gtf
import numpy as np
import pandas as pd
import sys
import pysam


def exonCount(truth,df):
    d_exon = {}
    d_aln = {}
    for i in truth.index:
        zoom_truth = pd.Interval(truth.loc[i, 'start'],truth.loc[i, 'end'],closed='both')
        d_exon[i] = 0
        d_aln[i] = 0
        for j in df.index:
            zoom_df = pd.Interval(df.loc[j, 'sstart'],df.loc[j, 'send'],closed='both')
            if str(truth.loc[i, 'seqname']) == str(df.loc[j, 'sseqid']) and zoom_truth.overlaps(zoom_df) and truth.loc[i, 'start'] <= df.loc[j, 'sstart'] and df.loc[j, 'send'] <= truth.loc[i, 'end'] :
                d_exon[i] = d_exon[i] +1
            if str(truth.loc[i, 'seqname']) == str(df.loc[j, 'sseqid']) and zoom_truth.overlaps(zoom_df) :
                d_aln[i] = d_aln[i] +1
    exon_count_ = 0
    # exon_num = 0
    for key, val in d_exon.items():
        if val > 0:
            exon_count_ = exon_count_ + 1
            # exon_num = val + exon_num
    aln_count_1 = 0
    aln_num_1 = 0
    for key, val in d_aln.items():
        if val > 0:
            aln_count_1 = aln_count_1 + 1
            # aln_num_1 = val + aln_num_1
    return (exon_count_,aln_count_1)

match_file = sys.argv[1]
gtf_file = sys.argv[2]
columns=['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
df_tab = pd.read_csv(match_file,header=None,sep = '\t',names=columns)
df_gtf = read_gtf(gtf_file)
print(df_gtf)
print(df_tab)
(exon_count_,aln_count_1) = exonCount(df_gtf,df_tab)
print("total mapped to exon, mapped to exon = ",exon_count_)
print("Not algined to exon = ",len(df_gtf) - aln_count_1)

