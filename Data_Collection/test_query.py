import pandas as pd
import pandas.io.sql as psql
import psycopg2

conn = psycopg2.connect(
    "dbname='dbsys6016' user=%s host=%s password=%s" % (user, host, password))

    = psql.read_sql(
        "SELECT * FROM usa_primary", conn)
filter Rt
should we Rt?
x = primary[primary['source'].str.contains("google")]
primary['user_lang'].value_counts()
