import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy.sql import text
import xml.etree.ElementTree as ET
import glob

# Specify the path to the TMX files
tmx_files = glob.glob("C:\\Users\\SUMIT SINGH RAJPOOT\\OneDrive\\Documents\\ar-en.tmx\\*.tmx")

# Define the XML namespace for the 'xml' prefix
xml_namespace = {'xml': 'http://www.w3.org/XML/1998/namespace'}

# Initialize lists to store English and Arabic texts
english_texts = []
arabic_texts = []

# Parse the TMX files and extract translation pairs
for tmx_file in tmx_files:
    tree = ET.parse(tmx_file)
    root = tree.getroot()

    for tu in root.findall('.//body/tu'):
        english_text = tu.find(".//tuv[@xml:lang='en']/seg", namespaces=xml_namespace).text
        arabic_text = tu.find(".//tuv[@xml:lang='ar']/seg", namespaces=xml_namespace).text
        english_texts.append(english_text)
        arabic_texts.append(arabic_text)

# Create a DataFrame
df = pd.DataFrame({'English': english_texts, 'Arabic': arabic_texts})

# Create a database connection
conn = sqlalchemy.create_engine('mssql+pyodbc://DESKTOP-0I578T1\SQLEXPRESS/TMX_Translation?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')

# Create the table 
query = ("""
CREATE TABLE  tmx_work1(
    English NVARCHAR(max),
    Arabic NVARCHAR(max) COLLATE Arabic_CI_AS
);
""")
with conn.connect() as connection:
    connection.execute(text(query))

# Write the DataFrame to the database
df.to_sql("tmx_work1", con=conn, if_exists="replace", index=False, dtype={'English': sqlalchemy.NVARCHAR(), 'Arabic': sqlalchemy.NVARCHAR()})
