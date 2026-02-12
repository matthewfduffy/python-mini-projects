# connect to a SQL Server to pull a query

# ---SETUP---
# Search for ODBC Connection Administrator
# Add a new User DSN with your server details and then test the connection
# Install pyodbc -> pip install pyodbc
# Import pandas and pyodbc
# ---END SETUP---

import pandas as pd
import pyodbc

query = "SELECT * FROM Table1"
connection = pyodbc.connect("DSN=YOUR_DSN_NAME")
df = pd.read_sql_query(query, connection)