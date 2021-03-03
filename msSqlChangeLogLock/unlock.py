#!/usr/bin/env python2
 
import os
import sys
import pymssql # DB-API interface to Microsoft SQL Server for Python

# SQL Query Variables
query1 = """
UPDATE DATABASECHANGELOGLOCK
SET LOCKED = 0,
    LOCKGRANTED = NULL,
    LOCKEDBY = NULL
WHERE ID = 1
"""
query2 = """
SELECT ID FROM DATABASECHANGELOGLOCK;
"""

# Run Queries Function
def run_queries(hostname, database, user, password, port):
  # Cursor up one line
	sys.stdout.write("\033[F")

  # MS SQL Connection
	connection = pymssql.connect(
		server=hostname,
		database=database,
		user=user,
		password=password,
		port=port
	)
	 
	# Execution Process
	cursor = connection.cursor()
	cursor.execute(query1)
	connection.commit()
	cursor.execute(query2)
	 
	# Output
	print("--- Queries Complete")
	if cursor.fetchone()[0] == 1:
	    print("--- DATABASE changelog lock value is 1")
	else:
	    print("--- WARNING changelog lock value is 0")
	 
	# Closing connection
	connection.close()

# If you want to change this to python3, just remember to change raw_input to input
run_queries(raw_input("Database Server Name: "), raw_input("Database: "), "deploy_user", raw_input("Password: "), str(1433))
