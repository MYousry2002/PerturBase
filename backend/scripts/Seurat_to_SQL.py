#!/usr/bin/env python3

###Extracts the data from metadata csv and a seurat file to add to db

#load modules
import argparse
import subprocess
import mdb_helper_functions as helpers

#get args

parser = argparse.ArgumentParser()
parser.add_argument('seurat_path')
parser.add_argument('experiment')
parser.add_argument('last_cmid')
parser.add_argument('username')
parser.add_argument('password')
args = parser.parse_args()

#create queries
subprocess.call(['Rscript', 'Seurat_to_SQL.R', args.experiment, args.last_cmid, args.meta_csv_path])

#run queries
connection, cursor = helpers.connect_database(
      "bioed-new.bu.edu", 
      4253, 
      "Team10", 
      args.username,
      args.password
      ) #only username and password differ between runs

#get list of query names
with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read()
# split by comma and strip whitespace, filter out empty strings
strings = [s.strip() for s in names.split(',') if s.strip()]

#execute all queries
for query in queries:
        helpers.execute_query(query)

#close out
cursor.close()
connection.close()


