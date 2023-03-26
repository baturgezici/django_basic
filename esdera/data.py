# %%
import pandas as pd
import sqlite3


cnx = sqlite3.connect('db.sqlite3')

df = pd.read_csv('data.csv')


df.to_sql('data', cnx, if_exists='replace', index=True, index_label="id", dtype={"installed": "BOOLEAN"})
# %%
