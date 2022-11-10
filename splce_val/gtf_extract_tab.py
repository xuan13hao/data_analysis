# pip install gtfparse, pandas, pysam, Biopython
# python3 gtf_extract.py match_tab SIRV_E2C.gtf 
from distutils.command.build import build
from gtfparse import read_gtf
import numpy as np
import pandas as pd
import sys
import re
from Bio import SeqIO

# >ENSANIT00000000002.1_431_929_0:0:0_1:0:0_0/1
def readReadName(input_file): # truth
    reads_list = []
    colums = ['seqname','start','end']
    truth = {}
    fasta_sequences = SeqIO.parse(open(input_file),'fasta')
    for fasta in fasta_sequences:
        seq_name = fasta.id
        #>(.*)_(.*)_(.*)_(.*)_(.*)_(.*)
        # m = re.match(r'(.*)_(.*)_(.*)_(.*)_(.*)_(.*)', name)
        m = re.match(r'(.*)_(.*)_(.*)_(.*)_(.*)_(.*)', seq_name)
        #print("ref_name = ",m.group(1),", start = ",m.group(2),", end = ",m.group(3))
        seq_name_list = [m.group(1),int(m.group(2)),int(m.group(3))]
        reads_list.append(seq_name_list)
    df = pd.DataFrame(reads_list, columns=colums)
    return df



def readTabularFormat(match_file):
    columns=['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
    df_tab = pd.read_csv(match_file,header=None,sep = '\t',names=columns)
    return df_tab

def readGTFFormat(gtf_file):
    df_gtf = read_gtf(gtf_file)
    # print(df_gtf['transcript_id'],'\t',df_gtf['start'],'\t',df_gtf['end'])
    return df_gtf

# def readsToGTFPosition(gtf_df,readname_df):



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

# match_file = sys.argv[1]
gtf_file = sys.argv[1]
fasta_file = sys.argv[2]
gtf_df = readGTFFormat(gtf_file)
# print(readTabularFormat(match_file))
read_df = readReadName(fasta_file)
flag_i = 0
flag_j = 0
grp_list = []
while flag_i != len(gtf_df) or flag_j != len(read_df):
    inteval_gtf = pd.Interval(gtf_df.loc[flag_i, 'start'],gtf_df.loc[flag_i, 'end'],closed='both')
    inteval_read = pd.Interval(read_df.loc[flag_j, 'start'],read_df.loc[flag_j, 'end'],closed='both')
    if gtf_df['gene_biotype'] == 'exon' and str(gtf_df.loc[flag_i, 'transcript_id']) == str(read_df.loc[flag_j, 'seqname']) and inteval_gtf.overlaps(inteval_read) and read_df.loc[flag_j, 'end'] <= gtf_df.loc[flag_i, 'end'] and read_df.loc[flag_j, 'start'] >= gtf_df.loc[flag_i, 'start']:
        flag_i = flag_i + 1
    else:
        flag_j = flag_j + 1
        flag_i = flag_i + 1


# columns=['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
# df_tab = pd.read_csv(match_file,header=None,sep = '\t',names=columns)
# df_gtf = read_gtf(gtf_file)
# print(df_gtf)
# print(df_tab)
# (exon_count_,aln_count_1) = exonCount(df_gtf,df_tab)
# print("total mapped to exon, mapped to exon = ",exon_count_)
# print("Not algined to exon = ",len(df_gtf) - aln_count_1)

