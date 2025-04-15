#!/usr/bin/Rscript
###Load a Seurat RDS
### extract meta data and counts
### return *.txt formatted sql commands to add to tables

##libs
library(Seurat)
library(SeuratObject)
library(stringr)

##Functions
#takes a partial sql insert data command (string)
# a single channel seurat object and the associated channel metadata Id
# returns sql string modified to add data to table
Fill_Counts_SQL <- function(sql, chnl, CMID){
  #get cell and feature names
  cell_names <- Cells(chnl)[1:100] #limiting to top 100 for now
  feat_names <- Features(chnl)[1:100]
  
  #for each cell
  for (i in 1:length(cell_names)) {
    #get all counts
    cnts <- as.numeric(
      FetchData(object = chnl,
                vars = c(feat_names),
                cells = cell_names[i],
                layer = 'counts'
      )
    )
    #for each feature
    for(j in 1:length(feat_names)){
      #create cell, feature, count string
      vals <- paste(
        '(',
        CMID, ', "',
        cell_names[i], '", "',
        feat_names[j], '", ',
        as.character(cnts[j]),
        '),',
        sep = ''
      )
      SQL <- paste(SQL, vals) #add to sql
    }
  }
  #replace final ',' with ';' in sql
  SQL <- str_replace(SQL, ',$', ';')
  
  #return modified string
  return(SQL)
}


#takes a seurat object and experiment id
#outputs a *.txt sql command for each channel
Seurat_to_SQL <- function(s, sql, EXP, lastCMID){
  query_names = ""
  #for each channel in s
  for (i in 1:length(s)) {
    #get channel ID by adding i + base 
    CMID <- lastCMID + i
    temp <- Fill_Counts_SQL(SQL, srt[[i]], as.character(CMID)) 
    name = paste(
      "Fill_Experiment_",
      EXP,
      '_Channel_', 
      as.character(CMID), 
      '.sql',
      sep = ''
    )
    query_names = paste(query_names, name, sep = ", ")
    write(temp, name)
  }
  write(query_names, "Fill_Counts.txt")
}

##Execution
#get args
args <- commandArgs(trailingOnly = TRUE)

EXP <- args[1] # current experiment
lastCMID <- as.integer(args[2]) #CMID to start off this channel
srt_path <- args[3]

#load data
srt <- readRDS(srt_path)

#build query
SQL <- 'INSERT INTO ChannelCounts (CMID, Cell_Name, Feature, Count) VALUES'

#run and output
Seurat_to_SQL(srt, SQL, EXP, lastCMID)
