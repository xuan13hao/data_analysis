# pip install gtfparse, pandas, pysam
# python3 gtf_extract.py alig_SIRV.sam SIRV_E2C.gtf 

from distutils.command.build import build
from gtfparse import read_gtf
import numpy as np
import pandas as pd
import sys
import pysam
import re
from Bio import SeqIO

# >ENSANIT00000000002.1_431_929_0:0:0_1:0:0_0/1
def readReadName(input_file):
    reads_list = []
    colums = ['seqname','start','end']
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
    return df_gtf


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
    for key, val in d_exon.items():
        if val > 0:
            exon_count_ = exon_count_ + 1
    aln_count_1 = 0
    for key, val in d_aln.items():
        if val > 0:
            aln_count_1 = aln_count_1 + 1
    return (exon_count_,aln_count_1)

def build_sam_pd(samfile):
    colums = ['qseqid','qstart','qend','sseqid','sstart','send','Map_Qual'] 
    df_sam = []
    for read in samfile.fetch():
        if read.reference_name == None:
            qs = 0
            qe = 0
            rs = 0
            re = 0
        else:
            qs = read.query_alignment_start + 1
            qe = read.query_alignment_end + 1
            rs = read.reference_start + 1
            re = read.reference_end + 1
        record = [read.query_name,qs,qe,read.reference_name,rs,re,read.mapping_quality]
        df_sam.append(record)
    df = pd.DataFrame(df_sam, columns=colums)
    return df

match_file = sys.argv[1]
gtf_file = sys.argv[2]
samfile = pysam.AlignmentFile(match_file, "r")
df_gtf = read_gtf(gtf_file)
df_sam = build_sam_pd(samfile)
print(df_gtf)
print(df_sam)
(e_num,aln_count_1) = exonCount(df_gtf,df_sam)
print("exon num, align num = ",e_num,aln_count_1)
print("Not algined to exon = ",len(df_gtf) - aln_count_1)
