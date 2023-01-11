# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:54:35 2023

@author: User2
"""
# fetch the data from oracle database
import cx_Oracle
import pandas as pd

#credentials
host_name = "xyzab"
port_number = 1234
service_name = "sdfghj"
user_name = "ankit.kumar"
password = "ankit@123"

dsn_tns = cx_Oracle.makedsn(host_name, port_number, service_name=service_name)
conn = cx_Oracle.connect(user=user_name, password=password, dsn=dsn_tns, encoding="UTF-8")
print("Oracle Client has been connected...")

query = """
		Write you query here
	"""
print("the query is: ",query)
df_qry = pd.read_sql(query, con=conn)
conn.close()
df_qry.to_csv('test.csv', index=False)
print("dataset has been created!")
