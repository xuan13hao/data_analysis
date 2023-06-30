# picrust2 

picrust2 with DADA2

## DADA2

asv_seqs <- colnames(seqtab.nochim)
asv_headers <- vector(dim(seqtab.nochim)[2], mode="character")

for (i in 1:dim(seqtab.nochim)[2]) {
  asv_headers[i] <- paste(">ASV", i, sep="_")
}

asv_fasta <- c(rbind(asv_headers, asv_seqs))
write(asv_fasta, "ASVs_Umar.fa")

asv_tab <- t(seqtab.nochim)
row.names(asv_tab) <- sub(">", "", asv_headers)
write.table(asv_tab, "ASVs_counts_Umar.tsv", sep="\t", quote=F, col.names=NA)

asv_tax <- taxa
row.names(asv_tax) <- sub(">", "", asv_headers)
write.table(asv_tax, "ASVs_taxonomy_Umar.tsv", sep="\t", quote=F, col.names=NA)

## Read placement
The first step of the workflow involves taking the study sequences and putting them into the pre-existing phylogenetic tree based on the 16S sequences from the reference genomes with the script place_seqs.py. As with all of the scripts in this workflow you can see the arguments and options for this tool by typing place_seqs.py --help. The default reference tree is based on full-length 16S sequences parsed from genomes in the Integrated Microbial Genomes database. The multiple-sequence alignment (MSA) of these reference 16S sequences is also required as input since it is required for the first placement step (done by HMMER). However, luckily for us this script automatically points to this MSA file that was included with our PICRUSt2 installation!
place_seqs.py -s ASVs_Umar.fa -o ASV_Umar.tre -p 4 --verbose
## Hidden-state prediction

Now that we have the study sequences placed in the reference tree we can proceed to the heart of the PICRUSt2 pipeline: hidden-state prediction (HSP). For each placed study sequence the predicted abundances of gene families of interest will be predicted, which below will be Enzyme Classification (E.C.) numbers.

We will also need to predict how many 16S copies are expected to be in the genome corresponding to each study sequence. Predicting how many 16S copies there are is important since this will be used in the next step to normalize the abundance of each sequence. We will also calculate the nearest-sequenced taxon index (NSTI), which is the measure of how distant each study sequence from the nearest reference sequence in the tree.

hsp.py -i 16S -t ASV_Umar.tre -o 16S_predicted.tsv -m mp -p 4 -n

Similarly, this command will generate predictions on how many copies of each gene family are found in each predicted genome. We wont bother calculating NSTI values again since it would be the same as above.

hsp.py -i EC -t ASV_Umar.tre -o EC_predicted.tsv -p 4 -m mp
hsp.py -i KO -t ASV_Umar.tre -o KO_predicted.tsv -p 4 -m mp

sort -k 3 16S_predicted.tsv

## Metagenome pipeline

metagenome_pipeline.py -i ASVs_counts_Umar.tsv \
                       -m 16S_predicted.tsv \
                       -f EC_predicted.tsv \
                       -o EC_metagenome_out
metagenome_pipeline.py -i ASVs_counts_Umar.tsv \
                       -m 16S_predicted.tsv \
                       -f KO_predicted.tsv \
                       -o KO_metagenome_out
## Infer MetaCyc pathway abundances and coverages based on predicted E.C. number abundances

pathway_pipeline.py -i EC_metagenome_out/pred_metagenome_unstrat.tsv.gz \
                    -o pathways_out \
                    --intermediate pathways_working \
                    -p 1
pathway_pipeline.py -i KO_metagenome_out/pred_metagenome_unstrat.tsv.gz \
                    -o KO_pathways_out \
                    --intermediate pathways_working \
                    -p 1

## Add descriptions as new column in gene family and pathway abundance tables

add_descriptions.py -i EC_metagenome_out/pred_metagenome_unstrat.tsv.gz -m EC \
                    -o EC_metagenome_out/pred_metagenome_unstrat_descrip.tsv.gz

add_descriptions.py -i pathways_out/path_abun_unstrat.tsv.gz -m METACYC \
                    -o pathways_out/path_abun_unstrat_descrip.tsv.gz

add_descriptions.py -i KO_metagenome_out/pred_metagenome_unstrat.tsv.gz -m KO \
                    -o KO_metagenome_out/pred_metagenome_unstrat_descrip.tsv.gz

## Plot


abundance_file <- "/home/xuan/BioinformaticTools/16s/picrust2/test.tsv"
metadata <- read_delim(
    "/home/xuan/BioinformaticTools/16s/picrust2/test_grp.csv",
    delim = "\t",
    escape_double = FALSE,
    trim_ws = TRUE
)


daa_results_df_annotated <- daa_results_df_annotated[!is.na(daa_results_df_annotated$pathway_name),]

daa_results_df_annotated$p_adjust <- round(daa_results_df_annotated$p_adjust,5)

low_p_feature <- daa_results_df_annotated[order(daa_results_df_annotated$p_adjust), ]$feature[1:20]

daa_results_list <-
  ggpicrust2(
    file = abundance_file,
    metadata = metadata,
    group = "Experiment",
    pathway = "EC",
    daa_method = "LinDA",
    p_values_bar = TRUE,
    order = "group",
    ko_to_kegg = FALSE,
    x_lab = "description",
    p.adjust = "BH",
    select = NULL,
    reference = NULL
  )