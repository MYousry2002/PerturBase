# Example R script: rds_to_csv.R
args <- commandArgs(trailingOnly=TRUE)
rds_file <- args[1]
csv_output <- args[2]

data <- readRDS(rds_file)
data_df <- as.data.frame(data)
write.csv(data_df, csv_output, row.names=FALSE)