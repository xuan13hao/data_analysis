mbSet<-Init.mbSetObj()
mbSet<-SetModuleType(mbSet, "mdp")
mbSet<-ReadSampleTable(mbSet, "NEC_Colon_C.csv");
mbSet<-Read16SAbundData(mbSet, "NEC_WT_C_COLON_genus.csv","text","SILVA","T","false");
mbSet<-SanityCheckData(mbSet, "text");
mbSet<-SanityCheckSampleData(mbSet);
mbSet<-SetMetaAttributes(mbSet, "1")
mbSet<-PlotLibSizeView(mbSet, "norm_libsizes_0","png");
mbSet<-CreatePhyloseqObj(mbSet, "text","SILVA","T" , "false")
mbSet<-ApplyAbundanceFilter(mbSet, "prevalence", 4, 0.2);
mbSet<-ApplyVarianceFilter(mbSet, "iqr", 0.1);
mbSet<-PerformNormalization(mbSet, "rarewi", "colsum", "none", "true");
mbSet<-PlotHeatmap(mbSet, "heatmap_0", "norm", "row","euclidean","ward.D","bwm","Experiment","OTU","overview","F", "png","T","T","0.0","0.0", "0.0","0.0","F");
mbSet<-PlotHeatmap(mbSet, "heatmap_1", "norm", "row","euclidean","ward.D","bwm","Experiment","Genus","overview","F", "png","T","T","13.0","8.8", "3.6","12.2","F");
