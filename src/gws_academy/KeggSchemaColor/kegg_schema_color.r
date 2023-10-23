specie = "rno"
pathway_id = "00010"
type_gene_id = "entrez"
column_gene_id = "Gene_id"
column_control = "Control"
column_wild = "Wild"

# Load required packages
library(pathview)
# Read the source csv file with header, row names and comma separator
microarray <- read.csv(source_paths[1], header = TRUE, sep = ",")
#copy dataset
microGlobal = microarray

#compute fold_change
fold_change <- microGlobal[column_wild]/microGlobal[column_control]
# Calculer le log2 du fold change
log2_fold_change <- log2(fold_change)

# Ajouter la colonne du log2 du fold change au dataframe
microGlobal$log2_fold_change <- log2_fold_change

pv.out <- pathview(gene.data = microGlobal, cpd.data = NULL,gene.idtype = type_gene_id, pathway.id = pathway_id, species = specie)


# Write the csv file into the result folder
result_path <- "result.csv"
write.csv(microGlobal, file = result_path, row.names = TRUE, col.names = TRUE)

image_path <- paste0(specie,pathway_id,".pathview.multi.png")
target_paths <- c(result_path, image_path)