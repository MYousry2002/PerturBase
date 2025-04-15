#!/usr/bin/Rscript
###Converts the meta data csv into sql commands

##libs
library(stringr)

##Functions
#takes the start of a sql command and the metadata table
#returns a sql command to fill experiments table
Experiments <- function(exp_SQL, meta){
  #for each exp
  exps <- unique(meta$experiment)
  for(e in 1:length(exps)){
    #add insert values
    exp_SQL <- paste(
      exp_SQL,
      '("',
      exps[e], '", "',
      exps[e], '", "', 
      'Cleary Lab"',
      '), ',
      sep = ''
      )
  }
  #replace final ',' with ';' in sql
  exp_SQL <- str_replace(exp_SQL, ', $', ';')
  return(exp_SQL)
}

#takes the start of a sql command and the metadata table
#returns a sql command to fill channel meta data table
Channels <- function(chl_SQL, meta) {
  #get experiments so the index can be used to find ExpID
  exps <- unique(meta$experiment)
  #for each channel
  for (i in 1:nrow(meta)) {
    #get expid
    Exp_ID <- which(exps == meta[i,1])
    
    #fill data
    chl_SQL <- paste(
      chl_SQL,
      '(',
      Exp_ID, ', ',
      '"RNA", ',
      meta[i,3], ', ',
      meta[i,4], ', ',
      meta[i,5], ', ',
      meta[i,6], ', ',
      meta[i,7], ', ',
      meta[i,8], ', ',
      meta[i,9],
      '), ',
      sep = ''
    )
  }
  #replace final ',' with ';' in sql
  chl_SQL <- str_replace(chl_SQL, ', $', ';')
  return(chl_SQL)
}


##Execution
#get args
args <- commandArgs(trailingOnly = TRUE)
meta_path <- args[1]
#load meta data
meta <- read.csv('meta_qc.csv')[-1] # -1 removes pointless numer column

#build template commands
exp_SQL <- 'INSERT INTO Experiment (Name, Treatment, Source) VALUES '
chl_SQL <- 'INSERT INTO ChannelMetaData (ExpID, Type, Ncells, Nfeatures_avg, nCount_avg, Mito_avg, Ribo_avg, nFeature_avg_cite, nCount_avg_cite) VALUES '

#run and output metadata 
exp_SQL <-Experiments(exp_SQL, meta)
chl_SQL <- Channels(chl_SQL, meta)

write(exp_SQL, 'Fill_Experiments.sql')
write(chl_SQL, 'Fill_Channels.sql')

