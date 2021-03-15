# running trimmomatic
cd raw
# single-end
for i in *
do
java -jar /home/ben0522/toolkit/Trimmomatic-0.38/trimmomatic-0.38.jar \
  SE $i ../trimmed/$i \
  ILLUMINACLIP:/home/ben0522/toolkit/Trimmomatic-0.38/adapters/NexteraPE-PE.fa:2:30:10 \
  LEADING:30 \
  TRAILING:30 \
  SLIDINGWINDOW:4:30 \
  MINLEN:35 -threads 8;
done

# mapping the reads
cd ../trimmed/
for i in *gz;
do
j=$(echo $i | sed s/.fastq.gz//);
/home/ben0522/toolkit/star/bin/Linux_x86_64/STAR --runMode alignReads \
  --genomeDir /home/ben0522/Data/RNAseq/hg38 \
  --readFilesIn $i \
  --readFilesCommand zcat \
  --outFileNamePrefix $j \
  --outReadsUnmapped Fastq \
  --outFilterMultimapNmax 100 \
  --runThreadN 16;
done


# pair-end
# pair-end
cd PE
for i in *R1*;
do
  j=$(echo $i | sed s/_R1_001.fastq.gz//)_R2_001.fastq.gz;
  k=$(echo $i | sed s/_L002_R\._001.fastq.gz//);
  java -jar /home/ben0522/toolkit/Trimmomatic-0.38/trimmomatic-0.38.jar \
  PE $i $j \
  $k.read1.fq.gz $k.forward.unpaired.fq.gz \
  $k.read2.fq.gz $k.reverse.unpaired.fq.gz \
  ILLUMINACLIP:/home/ben0522/toolkit/Trimmomatic-0.38/adapters/NexteraPE-PE.fa:2:30:10 \
  LEADING:30 \
  TRAILING:30 \
  SLIDINGWINDOW:4:30 \
  MINLEN:35 -threads 8;
done

for i in *read1*;
do
  k=$(echo $i | sed s/.read1.fq.gz//);
  /home/ben0522/toolkit/star/bin/Linux_x86_64/STAR --runMode alignReads \
    --genomeDir /home/ben0522/Data/RNAseq/hg38 \
    --readFilesCommand zcat \
    --readFilesIn $k.read1.fq.gz $k.read2.fq.gz \
    --outFileNamePrefix $k \
    --outReadsUnmapped Fastq \
    --outFilterMultimapNmax 100 \
    --runThreadN 16;
done

# count the expression
cd ../mapping
for i in *Aligned.out.sam;
do j=$(echo $i | sed s/Aligned.out.sam//);
htseq-count $i /home/ben0522/Data/RNAseq/hg38/NCBI_RefSeq_hg38.gtf > $j.count;
done

# merge the counts into a matrix
cd count/
# [a,b,c,d] vs [1,2]
perl ../mergeCountMatrices.pl \
  --files N1_D425-HLX2-7-KO-1.count,N2_D425-HLX2-7-KO-2.count,D425LUC1_S15.count,D425LUC2_S19.count \
  --IDs D425_HLX2_7_KO_rep1,D425_HLX2_7_KO_rep2,D425_rep1,D425_rep2 \
  --out ../D425_HLX2_7_vs_D425.count.csv
# [3, 4] vs [5, 6]
perl ../mergeCountMatrices.pl \
  --files N5_HLX2-7-KO-Day30-1.count,N6_HLX2-7-KO-Day30-2.count,N3_D425-Day30-1_S7.count,N4_D425-Day30-3_S6.count \
  --IDs HLX2_7_KO_Day30_rep1,HLX2_7_KO_Day30_rep2,D425_Day30_rep1,D425_Day30_rep2 \
  --out ../HLX2_7_KO_Day30_vs_D425_Day30.count.csv
# [3, 4] vs [7, 8]
perl ../mergeCountMatrices.pl \
  --files N7_HLX2-7-KO-Day60-1.count,N8_HLX2-7-KO-Day60-2.count,N3_D425-Day30-1_S7.count,N4_D425-Day30-3_S6.count \
  --IDs HLX2_7_KO_Day60_rep1,HLX2_7_KO_Day60_rep2,D425_Day30_rep1,D425_Day30_rep2 \
  --out ../HLX2_7_KO_Day60_vs_D425_Day30.count.csv
# [5, 6] vs [7, 8]
perl ../mergeCountMatrices.pl \
  --files N7_HLX2-7-KO-Day60-1.count,N8_HLX2-7-KO-Day60-2.count,N5_HLX2-7-KO-Day30-1.count,N6_HLX2-7-KO-Day30-2.count \
  --IDs HLX2_7_KO_Day60_rep1,HLX2_7_KO_Day60_rep2,HLX2_7_KO_Day30_rep1,HLX2_7_KO_Day30_rep2 \
  --out ../HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.count.csv



# normalize the read counts
perl ../NormalizeCountMatrix.pl D425_HLX2_7_vs_D425.count.csv                > D425_HLX2_7_vs_D425.count.norm.csv
perl ../NormalizeCountMatrix.pl HLX2_7_KO_Day30_vs_D425_Day30.count.csv      > HLX2_7_KO_Day30_vs_D425_Day30.count.norm.csv
perl ../NormalizeCountMatrix.pl HLX2_7_KO_Day60_vs_D425_Day30.count.csv      > HLX2_7_KO_Day60_vs_D425_Day30.count.norm.csv
perl ../NormalizeCountMatrix.pl HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.count.csv > HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.count.norm.csv

# # get the names
perl ../MapCountMatrixName.pl D425_HLX2_7_vs_D425.count.norm.csv                ../hg38/RefSeq_hg38.all.tsv >  D425_HLX2_7_vs_D425.count.norm.name.csv
perl ../MapCountMatrixName.pl HLX2_7_KO_Day30_vs_D425_Day30.count.norm.csv      ../hg38/RefSeq_hg38.all.tsv >  HLX2_7_KO_Day30_vs_D425_Day30.count.norm.name.csv
perl ../MapCountMatrixName.pl HLX2_7_KO_Day60_vs_D425_Day30.count.norm.csv      ../hg38/RefSeq_hg38.all.tsv >  HLX2_7_KO_Day60_vs_D425_Day30.count.norm.name.csv
perl ../MapCountMatrixName.pl HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.count.norm.csv ../hg38/RefSeq_hg38.all.tsv >  HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.count.norm.name.csv

perl ../MapDEOutName.pl D425_HLX2_7_vs_D425.DE.csv                ../hg38/RefSeq_hg38.all.tsv > D425_HLX2_7_vs_D425.DE.name.csv
perl ../MapDEOutName.pl HLX2_7_KO_Day30_vs_D425_Day30.DE.csv      ../hg38/RefSeq_hg38.all.tsv > HLX2_7_KO_Day30_vs_D425_Day30.DE.name.csv
perl ../MapDEOutName.pl HLX2_7_KO_Day60_vs_D425_Day30.DE.csv      ../hg38/RefSeq_hg38.all.tsv > HLX2_7_KO_Day60_vs_D425_Day30.DE.name.csv
perl ../MapDEOutName.pl HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.DE.csv ../hg38/RefSeq_hg38.all.tsv > HLX2_7_KO_Day60_vs_HLX2_7_KO_Day30.DE.name.csv
