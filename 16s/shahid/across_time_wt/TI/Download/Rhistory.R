mbSet<-Init.mbSetObj()
mbSet<-SetModuleType(mbSet, "mdp")
mbSet<-ReadSampleTable(mbSet, "11-14-28_TI.csv");
mbSet<-Read16SAbundData(mbSet, "11-14-28_COLON_genus.csv","text","SILVA","T","false");
mbSet<-SanityCheckData(mbSet, "text");
mbSet<-SanityCheckSampleData(mbSet);
mbSet<-SetMetaAttributes(mbSet, "1")
mbSet<-PlotLibSizeView(mbSet, "norm_libsizes_0","png");
mbSet<-CreatePhyloseqObj(mbSet, "text","SILVA","T" , "false")
mbSet<-ApplyAbundanceFilter(mbSet, "prevalence", 4, 0.2);
mbSet<-ApplyVarianceFilter(mbSet, "iqr", 0.1);
mbSet<-PerformNormalization(mbSet, "rarewi", "colsum", "none", "true");
mbSet<-PlotAlphaData(mbSet, "filt","alpha_diver_0","Chao1","DOL","OTU", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_0","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PlotAlphaData(mbSet, "orig","alpha_diver_1","Chao1","DOL","OTU", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_1","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PerformBetaDiversity(mbSet, "beta_diver_0","PCoA","bray","expfac","DOL","none","OTU","Lactobacillus","Chao1", "yes", "adonis", "png", 72, "default", "false");
mbSet<-PCoA3D.Anal(mbSet, "PCoA","bray","OTU","expfac","DOL","Lactobacillus","Chao1","beta_diver3d_0.json")
mbSet<-PerformCategoryComp(mbSet, "OTU", "adonis","bray","DOL","false");
mbSet<-PerformBetaDiversity(mbSet, "beta_diver_1","NMDS","bray","expfac","DOL","none","OTU","Lactobacillus","Chao1", "yes", "adonis", "png", 72, "default", "false");
mbSet<-PCoA3D.Anal(mbSet, "NMDS","bray","OTU","expfac","DOL","Lactobacillus","Chao1","beta_diver3d_1.json")
mbSet<-PerformCategoryComp(mbSet, "OTU", "adonis","bray","DOL","false");
mbSet<-PlotHeatmap(mbSet, "heatmap_0", "norm", "row","euclidean","ward.D","bwm","DOL","OTU","overview","F", "png","T","T","0.0","0.0", "0.0","0.0","F");
mbSet<-RF.Anal(mbSet, 500,7,1,"DOL","OTU")
mbSet<-PlotRF.Classify(mbSet, 15, "rf_cls_0","png", width=NA)
mbSet<-PlotRF.VIP(mbSet, 15, "rf_imp_0","png", width=NA)
mbSet<-PerformLefseAnal(mbSet,  0.1, "fdr", 2.0,  "DOL","F","NA","OTU");
mbSet<-PlotLEfSeSummary(mbSet, 15, "dot",  "bar_graph_0","png");
mbSet<-PlotLEfSeSummary(mbSet, 15, "bar",  "bar_graph_1","png");
