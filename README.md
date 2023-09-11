# Data_Engineer_Ass
# TMX Data Pipeline
This data pipeline allows to parse TMX files containing translation pairs (English and Arabic) and store them in a SQL Server database.

## Prerequisites

Before running the pipeline, ensure to have the following prerequisites installed:

- Python (3.x recommended)
- SQL Server (with necessary permissions)
- Required Python libraries: `xml.etree.ElementTree`, `pandas`, `pyodbc`, `sqlalchemy`

## Installation

1. Clone or download this project to the local machine.

2. Place the TMX files in the `data/` directory.

3. Install the required Python libraries by running the following command:

   ```bash
   pip install pandas pyodbc sqlalchemy
## Usage
Parsing TMX Files
To parse TMX files and create a translation pairs text file, run the following command:
python scripts/parse_tmx.py
This will create a translation_pairs.txt file in the project directory.
## Setting Up SQL Server
  Make sure you have SQL Server installed and running.
  Configure your SQL Server connection in scripts/sql_setup.py
server_name = 'ServerName'
database_name = 'DatabaseName'
## Viewing Data
You can view the data in  SQL Server table using SQL Server Management Studio (SSMS) or by executing SQL queries. Example SQL query to view data:
SELECT * FROM tmx_work;
