import pandas as pd
import pyodbc,sqlalchemy,socket
from sqlalchemy.sql import text
# Specify the path to the input .txt file
input_file_path = 'C:\\Users\\SUMIT SINGH RAJPOOT\\OneDrive\\Documents\\Read_Tmx\\translation_pairs.txt'

# Initialize lists to store English and Arabic texts
english_texts = []
arabic_texts = []

# Read data from the input .txt file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("English: "):
            english_texts.append(lines[i][len("English: "):].strip())
            i += 1
        elif lines[i].startswith("Arabic: "):
            arabic_texts.append(lines[i][len("Arabic: "):].strip())
            i += 1
        else:
            # Skip lines that are not part of the translation pairs
            i += 1

# Create a DataFrame
df = pd.DataFrame({'English': english_texts, 'Arabic': arabic_texts})

# Display the DataFrame
# print(df.head(2))
conn = sqlalchemy.create_engine(f'mssql+pyodbc://DESKTOP-0I578T1\SQLEXPRESS/TMX_Translation?trusted_connetion=yes&driver=ODBC Driver 17 for SQL Server')
query = "CREATE TABLE tmx_work( English NVARCHAR(max),Arabic NVARCHAR(max) COLLATE Arabic_CI_AS);"
with conn.connect() as connection:
    connection.execute(text(query))
# conn.execute(text(query).execution_options(autocommit=True))
df.to_sql("tmx_work",con=conn,if_exists="replace",index=False,dtype={'English': sqlalchemy.NVARCHAR(), 'Arabic': sqlalchemy.NVARCHAR()})
# print(socket.gethostname())
