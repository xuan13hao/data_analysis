

from Bio import SeqIO
import re

Codon_Table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def separate_genome_into_files():
    f = open("hg38.fa.gz","r",encoding="utf-8")
    fwrite = open("t",'w',encoding="utf-8")
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            fwrite.close()
            fwrite = open("hg38/" + line[1:], 'w',encoding="utf-8")
        else:
            fwrite.write(line)


def read_gene(name):
    f = open("hg38.fa.gz")
    start = False
    gene_sequences = ''
    for line in f:
        line = line.strip()
        if start:
            if line.startswith('>'):
                f.close()
                break
            else:
                gene_sequences += line
        if line[1:] == name:
            start = True

    return gene_sequences


def table_mapping(gene):
    transformed_gene = ''
    for triplet in re.findall('...', gene):
        transformed_gene += Codon_Table[triplet]
    return transformed_gene


def transform_gene(chrome, exon_start, exon_end, exon):
    f_gene = open("hg38/" + chrome)
    gene = f_gene.readline()
    gene = gene[exon_start:exon_end].upper()
    return table_mapping(gene[exon:])


def parsing_table_annotations():
    f = open("hg_annotation")
    fwrite = open("output.fa", 'w')
    chrome = []
    for i, line in enumerate(f):
        line = line.split()
        if i == 0:
            title_dict = dict()
            for j, element in enumerate(line):
                title_dict.update({element: j})
            print(title_dict)
        else:
            chrom = line[title_dict['chrom']]
            name = line[title_dict["name"]] + ":" + line[title_dict["name2"]]
            strand = line[title_dict["strand"]]
            exonStarts = [int(x) for x in line[title_dict['exonStarts']].split(',')[:-1]]
            exonEnds = [int(x) for x in line[title_dict['exonEnds']].split(',')[:-1]]
            exonFrames = [int(x) for x in line[title_dict['exonFrames']].split(',')[:-1]]
            exonFrames_valid = [x == -1 for x in exonFrames]

            if chrom not in chrome:
                chrome.append(chrome)
                f_gene = open("hg38/" + chrom)
                gene = f_gene.readline()
            elif (chrom in chrome) and (chrom != chrome[-1]):
                f_gene = open("hg38/" + chrom)
                gene = f_gene.readline()
            if all(exonFrames_valid):
                continue
            else:
                fwrite.write(">" + name + '\n')
                end_codon = False
                for i, exon in enumerate(exonFrames):
                    if exon != -1:
                        if strand == '+':
                            gene_chip = gene[exonStarts[i]:exonEnds[i]].upper()
                        # print(gene_chip[exon:][exonStarts[i] - 5:exonStarts[i] + 5])
                        elif strand == '-':
                            gene_chip = gene[exonEnds[i]:exonStarts[i]:-1].upper()
                            gene_chip = gene_chip.translate(str.maketrans({'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C'}))
                        transformed_gene = ''
                        for triplet in re.findall('...', gene_chip[exon:]):
                            # if Codon_Table[triplet] != '*':
                            transformed_gene += Codon_Table[triplet]
                            # else:
                            #     end_codon = True
                            #     break
                        fwrite.write(transformed_gene)
                        # if end_codon:
                        #     break

                fwrite.write('\n')
            print(chrom + '-> ' + name)
            if strand == '+':
                break
            # print(strand)
            # print(exonStarts)
            # print(exonEnds)
            # print(exonFrames)
    f.close()
    fwrite.close()


if __name__ == '__main__':
    # parsing_table_annotations()

    for seq_record in SeqIO.parse("hg38.fa", "fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))
    # separate_genome_into_files()
