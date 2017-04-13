import pandas as pd
import pandas.io.sql as psql
import psycopg2

conn = psycopg2.connect(
    "dbname='dbsys6016' user=%s host=%s password=%s" % (user, host, password))
primary = psql.read_sql(
    "SELECT * FROM usa_primary", conn)
len(primary)
