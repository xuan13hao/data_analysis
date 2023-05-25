library(dada2); packageVersion("dada2")
path <- "/home/h392x566/Project_Folder/2023_Umar/2023_Umar/data/analysis_data/data_prepare"

fnFs <- sort(list.files(path, pattern="_R1_001.fastq", full.names = TRUE))
fnRs <- sort(list.files(path, pattern="_R2_001.fastq", full.names = TRUE))
sample.names <- sapply(strsplit(basename(fnFs), "_S.*_"), `[`, 1)
# sample.name <- gsub("_.*", "", basename(fnFs))
sample.names

filtFs <- file.path(path, "filtered", paste0(sample.names, "_F_filt.fastq.gz"))
filtRs <- file.path(path, "filtered", paste0(sample.names, "_R_filt.fastq.gz"))
out <- filterAndTrim(fnFs, filtFs, fnRs, filtRs, truncLen=c(290,270),
                     maxN=0, truncQ=2, rm.phix=TRUE,
                     compress=TRUE, multithread=TRUE, trimLeft = c(15,20), verbose = TRUE)
#
errF <- learnErrors(filtFs, multithread=TRUE)
errR <- learnErrors(filtRs, multithread=TRUE)
derepFs <- derepFastq(filtFs, verbose=TRUE)
derepRs <- derepFastq(filtRs, verbose=TRUE)
names(derepFs) <- sample.names
names(derepRs) <- sample.names
dadaFs <- dada(derepFs, err=errF, multithread=TRUE)
dadaRs <- dada(derepRs, err=errR, multithread=TRUE)
mergers <- mergePairs(dadaFs, derepFs, dadaRs, derepRs, verbose = TRUE)
seqtab <- makeSequenceTable(mergers)
dim(seqtab)
table(nchar(getSequences(seqtab)))
seqtab.nochim <- removeBimeraDenovo(seqtab, method="consensus", multithread=TRUE, verbose=TRUE)
dim(seqtab.nochim)
sum(seqtab.nochim)/sum(seqtab)
getN <- function(x) sum(getUniques(x))
track <- cbind(out, sapply(dadaFs, getN), sapply(dadaRs, getN), sapply(mergers, getN), rowSums(seqtab.nochim))
colnames(track) <- c("input", "filtered", "denoisedF", "denoisedR", "merged", "nonchim")
rownames(track) <- sample.names
head(track)

# taxa <- assignTaxonomy(seqtab.nochim, "/home/ben0522/Data/16s/tax/silva_nr_v138_train_set.fa.gz", multithread=TRUE)
taxa <- assignTaxonomy(seqtab.nochim, "/home/Database/SILVA/silva_nr_v132_train_set.fa.gz", multithread=TRUE)
taxa <- addSpecies(taxa, "/home/Database/SILVA/silva_species_assignment_v132.fa.gz")

#taxa <- assignTaxonomy(seqtab.nochim, "/home/ben0522/Data/16s/tax/gg_13_8_train_set_97.fa.gz", multithread=TRUE)
#taxa <- addSpecies(taxa, "/home/ben0522/Data/16s/tax/rdp_species_assignment_14.fa.gz")

library(tidyr)
library(data.table)
temp <- as.data.table(taxa)
temp_taxa <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), unlist(temp[,4]), unlist(temp[,5]), unlist(temp[,6]), unlist(temp[,7]), sep=";")
kingdom <- unlist(temp[,1])
phylum <- paste(unlist(temp[,1]), unlist(temp[,2]), sep=";")
class <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), sep=";")
order <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), unlist(temp[,4]), sep=";")
family <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), unlist(temp[,4]),  unlist(temp[,5]), sep=";")
genus <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), unlist(temp[,4]), unlist(temp[,5]), unlist(temp[,6]), sep=";")
species <- paste(unlist(temp[,1]), unlist(temp[,2]), unlist(temp[,3]), unlist(temp[,4]), unlist(temp[,5]), unlist(temp[,6]), unlist(temp[,7]), sep=";")

kingdom_table <- seqtab.nochim
kingdom_header <- c(kingdom)
colnames(kingdom_table) <- kingdom_header
write.csv(t(kingdom_table), "kingdom_table_taxa.csv")

phylum_table <- seqtab.nochim
phylum_header <- c(phylum)
colnames(phylum_table) <- phylum_header
write.csv(t(phylum_table), "phylum_table_taxa.csv")

class_table <- seqtab.nochim
class_header <- c(class)
colnames(class_table) <- class_header
write.csv(t(class_table), "class_table_taxa.csv")

order_table <- seqtab.nochim
order_header <- c(order)
colnames(order_table) <- order_header
write.csv(t(order_table), "order_table_taxa.csv")

family_table <- seqtab.nochim
family_header <- c(family)
colnames(family_table) <- family_header
write.csv(t(family_table), "family_table_taxa.csv")

genus_table <- seqtab.nochim
genus_header <- c(genus)
colnames(genus_table) <- genus_header
write.csv(t(genus_table), "genus_table.csv")

species_table <- seqtab.nochim
species_header <- c(species)
colnames(species_table) <- species_header
write.csv(t(species_table), "species_table_taxa.csv")


# # output
# asv_seqs <- colnames(seqtab.nochim)
# asv_headers <- vector(dim(seqtab.nochim)[2], mode="character")

# for (i in 1:dim(seqtab.nochim)[2]) {
#   asv_headers[i] <- paste(">ASV", i, sep="_")
# }

#   # making and writing out a fasta of our final ASV seqs:
# asv_fasta <- c(rbind(asv_headers, asv_seqs))
# write(asv_fasta, "ASVs.fa")

#   # count table:
# asv_tab <- t(seqtab.nochim)
# row.names(asv_tab) <- sub(">", "", asv_headers)
# write.table(asv_tab, "ASVs_counts.tsv", sep="\t", quote=F, col.names=NA)

#   # tax table:
# asv_tax <- taxa
# row.names(asv_tax) <- sub(">", "", asv_headers)
# write.table(asv_tax, "ASVs_taxonomy.tsv", sep="\t", quote=F, col.names=NA)
