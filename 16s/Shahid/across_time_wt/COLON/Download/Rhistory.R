mbSet<-Init.mbSetObj()
mbSet<-SetModuleType(mbSet, "mdp")
mbSet<-ReadSampleTable(mbSet, "8-11-14-28_COLON_grp.csv");
mbSet<-Read16SAbundData(mbSet, "8-11-14-28_COLON_genus.csv","text","SILVA","T","false");
mbSet<-SanityCheckData(mbSet, "text");
mbSet<-SanityCheckSampleData(mbSet);
mbSet<-SetMetaAttributes(mbSet, "1")
mbSet<-PlotLibSizeView(mbSet, "norm_libsizes_0","png");
mbSet<-CreatePhyloseqObj(mbSet, "text","SILVA","T" , "false")
mbSet<-ApplyAbundanceFilter(mbSet, "prevalence", 4, 0.2);
mbSet<-ApplyVarianceFilter(mbSet, "iqr", 0.1);
mbSet<-PerformNormalization(mbSet, "rarewi", "colsum", "none", "true");
mbSet<-PlotHeatmap(mbSet, "heatmap_0", "norm", "row","euclidean","ward.D","bwm","DOL","OTU","overview","F", "png","T","T","0.0","0.0", "0.0","0.0","F");
mbSet<-PlotHeatmap(mbSet, "heatmap_1", "norm", "row","euclidean","ward.D","bwm","DOL","Genus","overview","F", "png","T","T","13.0","8.8", "3.4","12.0","F");
mbSet<-PlotAlphaData(mbSet, "filt","alpha_diver_0","Chao1","DOL","OTU", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_0","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PlotAlphaData(mbSet, "orig","alpha_diver_1","Chao1","DOL","Genus", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_1","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PlotAlphaData(mbSet, "filt","alpha_diver_2","Chao1","DOL","Genus", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_2","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PlotAlphaData(mbSet, "orig","alpha_diver_3","Chao1","DOL","Genus", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_3","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PerformBetaDiversity(mbSet, "beta_diver_0","PCoA","bray","expfac","DOL","none","OTU","Lactobacillus","Chao1", "yes", "adonis", "png", 72, "default", "false");
mbSet<-PCoA3D.Anal(mbSet, "PCoA","bray","OTU","expfac","DOL","Lactobacillus","Chao1","beta_diver3d_0.json")
mbSet<-PerformCategoryComp(mbSet, "OTU", "adonis","bray","DOL","false");
mbSet<-PerformBetaDiversity(mbSet, "beta_diver_1","NMDS","bray","expfac","DOL","none","Genus","A2","Chao1", "yes", "adonis", "png", 72, "default", "false");
mbSet<-PCoA3D.Anal(mbSet, "NMDS","bray","Genus","expfac","DOL","A2","Chao1","beta_diver3d_1.json")
mbSet<-PerformCategoryComp(mbSet, "Genus", "adonis","bray","DOL","false");
mbSet<-PlotHeatmap(mbSet, "heatmap_2", "raw", "row","euclidean","ward.D","bwm","DOL","Genus","overview","F", "png","T","T","13.0","8.8", "3.5","12.1","F");
mbSet<-PlotAlphaData(mbSet, "filt","alpha_diver_4","Chao1","DOL","Genus", "default", "png");
mbSet<-PlotAlphaBoxData(mbSet, "alpha_diverbox_4","Chao1","DOL","default", "png");
mbSet<-PerformAlphaDiversityComp(mbSet, "tt","DOL","false");
mbSet<-PlotHeatmap(mbSet, "heatmap_3", "norm", "row","euclidean","ward.D","bwm","DOL","Genus","detail","F", "png","T","T","13.0","8.8", "3.5","12.1","T");
mbSet<-PerformLefseAnal(mbSet,  0.1, "fdr", 2.0,  "DOL","F","NA","OTU");
mbSet<-PlotLEfSeSummary(mbSet, 15, "dot",  "bar_graph_0","png");
mbSet<-PlotLEfSeSummary(mbSet, 15, "bar",  "bar_graph_1","png");
mbSet<-PerformLefseAnal(mbSet,  0.1, "fdr", 2.0,  "DOL","F","NA","Genus");
mbSet<-PlotLEfSeSummary(mbSet, 15, "bar",  "bar_graph_2","png");
mbSet<-PerformLefseAnal(mbSet,  0.05, "raw", 2.0,  "DOL","F","NA","Genus");
mbSet<-PlotLEfSeSummary(mbSet, 15, "bar",  "bar_graph_3","png");
mbSet<-PerformLefseAnal(mbSet,  0.05, "raw", 2.0,  "DOL","F","NA","Genus");
mbSet<-PlotLEfSeSummary(mbSet, 15, "bar",  "bar_graph_4","png");
mbSet<-RF.Anal(mbSet, 500,7,1,"DOL","OTU")
mbSet<-PlotRF.Classify(mbSet, 15, "rf_cls_0","png", width=NA)
mbSet<-PlotRF.VIP(mbSet, 15, "rf_imp_0","png", width=NA)
mbSet<-RF.Anal(mbSet, 500,7,1,"DOL","Genus")
mbSet<-PlotRF.Classify(mbSet, 15, "rf_cls_1","png", width=NA)
mbSet<-PlotRF.VIP(mbSet, 15, "rf_imp_1","png", width=NA)
mbSet<-PlotRF.Classify(mbSet, 15, "rf_cls_2","png", width=NA)
mbSet<-PlotRF.VIP(mbSet, 15, "rf_imp_2","png", width=NA)
mbSet<-RF.Anal(mbSet, 500,7,1,"DOL","Genus")
mbSet<-PlotRF.Classify(mbSet, 15, "rf_cls_3","png", width=NA)
mbSet<-PlotRF.VIP(mbSet, 15, "rf_imp_3","png", width=NA)
