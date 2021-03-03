#!/usr/bin/env python3
 
import os
import sys
# DB-API interface to Microsoft SQL Server for Python
import pymssql
 
# User Interactive Variables
hostname = input("Database Server Name: ")
database = input("Database: ")
user = "deploy_user"
password = input("Password: ")
sys.stdout.write("\033[F") # Cursor up one line
port = str(1433)
 
# MS SQL Connection
connection = pymssql.connect(server=hostname,database=database,user=user,password=password,port=port)
 
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