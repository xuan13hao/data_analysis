
/usr/bin/time -v ./minimap2/minimap2 -ax splice ./databases/minimap2/Accipiter_nisus.Accipiter_nisus_ver1.0.cdna.all.fa ./databases/minimap2/reas.fa > ./results/minimap2/minimap2_splice.sam
/usr/bin/time -v ./bwa/bwa mem ./databases/bwa/Accipiter_nisus.Accipiter_nisus_ver1.0.cdna.all.fa ./databases/bwa/reas.fa > ./results/bwa/bwa_splice.sam
/usr/bin/time -v ./hisat2/hisat2 -f -x ./databases/hisat2/genome -U ./databases/hisat2/reas.fa -S ./results/hisat2/hisat2_splice.sam