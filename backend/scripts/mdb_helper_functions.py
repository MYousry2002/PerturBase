#!/usr/bin/env python3

###Helpers to handle mariadb runs in meta and seurat to sql scripts

#load modules
import mariadb

#functions
def read_query_file(filename):
        #open file, read lines and concatenate into one string
        f = open(filename, "r")
        query = ""
        for line in f:
                #omit lines that start with "--"
                if line[0:2] != "--": #could use regex but this is easier
                        #omit ends of lines including and beyond "--"
                        cleaned = line.split("--")[0]
                        #convert newline characters to blanks
                        cleaned = cleaned.replace("\n", " ")
                        query += cleaned

        return query

def connect_database(hostname, port_id, database, username, password):
    #connect to database on host
    connection = mariadb.connect(host=hostname,
            db=database, #note the database name
            user=username,
            passwd=password,
            port=int(port_id)
    )
    #create cursor object
    cursor = connection.cursor()

    return (connection, cursor)


def execute_query(cursor, query):
	#execute the query with try:  .. except:
	#on error, print the query and the error
    try:
            cursor.execute(query)
    except mariadb.Error as e:
            print("Error:")
            print(e)
            print("Query:")
            print(query)

    return "Query Executed"
