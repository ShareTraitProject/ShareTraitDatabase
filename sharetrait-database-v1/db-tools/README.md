# build-sharetrait-db : building and running the sharetrait database v1

This document explains how to set up and build the sharetrait-database-v1 in your desktop.
A python script creates the sharetrait databse using the set of tables used in version1. 

---
## Prerequisites

Before running `build-sharetraid-db-v1.py`, make sure you have:

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
Please note that in order to run the queries without creating python scripts, it is highly recommended to install SQL








