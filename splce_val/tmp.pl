#!/usr/bin/perl -w
use strict;

# converts SAM alignment file to genomic intervals

my $file = shift;   # the SAM file input

print "#Query_ID\tQuery_begin\tQuery_end\tRef_ID\tRef_begin\tRef_end\tMap_Qual\n";
open my $IN, "<$file" or die "Cannot open file: $!\n";
while(<$IN>) {
  next if /^\@/;
  chomp;
  my @decom = split /\t+/, $_;
  # analyze the CIGAR string
  my @numb = split /\D+/, $decom[5];
  my @type = split /\d+/, $decom[5]; 
  shift @type;
  #print "@numb\n";
  #print "@type\n";
  # computes the aligned region using the following rules
  #Op BAM Description Consumes_query Consumes_reference
  #M 0 alignment match (can be a sequence match or mismatch) yes yes
  #I 1 insertion to the reference yes no
  #D 2 deletion from the reference no yes
  #N 3 skipped region from the reference no yes
  #S 4 soft clipping (clipped sequences present in SEQ) yes no
  #H 5 hard clipping (clipped sequences NOT present in SEQ) no no
  #P 6 padding (silent deletion from padded reference) no no
  #= 7 sequence match yes yes
  #X 8 sequence mismatch yes yes
  my $r_begin = 0; my $r_end = 0;                   # read interval
  my $g_begin = $decom[3]; my $g_end = $decom[3];   # genome interval
  for(my $i = 0; $i < scalar(@numb); ++ $i) {
    #print "$type[$i]  $numb[$i]\n";
    if($type[$i] eq 'S')  {
      # we expect the soft clipping to happen only on boundaries of the read
      # if it is at the beginning, we need to shift the read begin and end
      # if it is at the end, nothing needs to be done
      if($r_begin == 0)  {
        $r_begin += $numb[$i];
        $r_end += $numb[$i];
      }
    } elsif($type[$i] eq 'M' || $type[$i] eq '=' || $type[$i] eq 'X') {
      # we extend both the query and the genome
      $r_end += $numb[$i] - 1;
      $g_end += $numb[$i] - 1;
    } elsif($type[$i] eq 'I') {
      $r_end += $numb[$i] - 1;
    } elsif($type[$i] eq 'D') {
      $g_end += $numb[$i] - 1;
    }
    #print "$r_begin $r_end  $g_begin  $g_end\n";
  }
  print "$decom[0]\t$r_begin\t$r_end\t$decom[2]\t$g_begin\t$g_end\t$decom[4]\n";
  #die;
}
close $IN;
