# build-sharetrait-db : building and running the sharetrait database v1

`build-sharetrait-db.py` creates a local version of the database template and imports all the data tables in the database. 
The purpose of `build-sharetrait-db.py` is to run a local version of sharetrait database version 1.0. 
This document explains how to set up and build the sharetrait-database-v1 in your desktop.

---
## Pre-requirements

Before running `build-sharetraid-db-v1.py`, make sure you have the following:

1. Python 3 installed
   
   - Go to [Python Download page](https://www.python.org/downloads/) to download the latest version (Python3 >3.0). Python 3.9.6 was used to create `build-sharetrait-db-v1.py`.
   - you can check if it is installed by running
  ```bash
  python3 --version
  ```

2. Python dependencies - Pandas python package
   
   - pandas is ised for reading and processing the data tables. Install it by using:
  
  ```bash
  pip install pandas
  ```

The script also uses sqlite3 and os, which are included in Python’s standard library — no additional installation is needed for these.

## Setup

1. Create a database folder locally
   
   - in your computer, create a new folder with the database name. For instance, the db folder name can be `sharetrait-db`, but you can call it the way you want
     
2. Go to db-tools page and download `build-sharetrait-db-v1.py` and save it in the sharetrait-db local folder.

3. Save the `build-sharetrait-db-v1.py` in the `sharetrait-db` local folder.
   
4. Create a sub-folder in `sharetrait-db` folder called `table-folder`.
   
5. Download the 21 tables to be imported in the database. The tables are found in the [db-tables folder](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-tables) of this repository.
   
6. you can download the tables by cloning this repository and save the table files in the `table-folder`. More information on how to do this found in GitHub documentation [cloning-a-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Run the script

1. Go to the terminal and go to the directory where the script is located in the system.

   ```bash
   cd /Users/username/path/sharetrait-db/
   ```

2. Run the script

  ```bash
  python3 build-sharetrait-db-v1.py
  ```

The script will create the full database `ST_all.db` and read the tables and import them in the database. 
The local version `ST_all.db` created is the same provided in the [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-export) folder 

## Output

A structured database file `ST_all.db` containing the imported data is found in the same folder where the script is located. 
The script also runs two query tests to see if the data was imported correctly. 
To run more queries please take a look at the [db-queries](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-queries) folder.



---
> [!NOTE] 
Please note that in order to run the queries without creating python scripts, it is highly recommended to install SQLite, follow instructions in the [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-export). For more information and support please contact Irene




