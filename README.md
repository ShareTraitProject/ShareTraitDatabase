# ShareTrait DataBase SQL

This repository contains the ShareTrait DataBase (STDB) SQL of [ShareTrait Project Data](https://github.com/ShareTraitProject).
The ShareTrait Database is a structured SQL-based database designed to store structured information and retrieve trait-based biological data obtained from ShareTrait: a data portal for making trait data interoperable and reusable [ShareTrait](https://github.com/ShareTraitProject/ShareTrait). 

## Latest release version
Last modified: 2025-09-25

The most recent release of this repository is archived in [Zenodo](https://zenodo.org).  

- **Release Title:** sharetrait-db v1.0.0 
- **Version:** v1.0.0  
- **Database Reference:** ShareTraitDatabase 
- **Release DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16537297.svg)](https://doi.org/10.5281/zenodo.16537297)
- **Published on:** 2025-07-28
- **GitHub Release:** [![GitHub Release](https://img.shields.io/github/v/release/ShareTraitProject/ShareTraitDatabase?color=blue&logo=github)](https://github.com/ShareTraitProject/ShareTraitDatabase/releases/tag/v1.0.0)  

This release snapshot contains the validated dataset, metadata, and code associated with version **v1.0.0**.  
Please use the [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16537297.svg)](https://doi.org/10.5281/zenodo.16537297) when citing this resource in publications.
The ShareTrait DataBase (STDB) SQL – version 1.0.0 includes the database schema, database tables, queries, and scripts needed to set up the ShareTrait database locally. 

## Repository Structure

The SharetraitDatabase repository is structured as follows. Only the ShareTraitDatabase repository is described

```
ShareTraitProject/
├── ShareTrait
├── ShareTraitDatabase/
|   ├── README.md
|   ├── CITATION.cff
|   ├── CONTRIBUTORS
|   ├── LICENSE
|   ├── db
│   │   ├── STdb_v01/
│   │   ├── stdb-all/
│   │   ├── README.md
|   ├── diagrams
|   ├── documentation
|   ├── mappings
│   │   ├── attribute_mapping_v02/
│   │   ├── attribute_mappings_v01/
│   │   ├── dataset-db-attributes-mapping-v1/
│   │   ├── README.md
|   ├── queries
│   ├── sharatrait-database-v1/
│   │   ├── db-documentation/
│   │   ├── db-export/
│   │   ├── db-publish/
│   │   ├── db-queries/
│   │   ├── db-tables/
│   │   ├── db-tools/
|   ├── tables

---
```

## Repository general description

Hereby we describe the general content found for each folder of the directory. Please make sure you look at the **README.md** files within each sub-folder for more information regarding the file content and usage. 

| folder name | description | last modified |
| :--- | :--- | :--- | 
| [db](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/db) | sharetrait database sql test versions  | 2024-06-12 |
| [diagrams](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/diagram) | database sketch backup schemas and models versions | 2024-08-18 |
| [documentation](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/documentation) | definitions and description of the ER model | 2024-08-01 |
| [mappings](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/mappings) | mappings for aligning db attributes to sharetrait previous versions | 2024-11-05 |
| [queries](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/queries) | questions queries mapping for selecting data | 2024-09-13 |
| [sharetrait-database-v1*](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1) | v1.0.0 of sharetrait database | 2025-07-25 |
| [tables](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables) | list of data files to populate database | 2024-11-04 |

## General release version overview

The folder [sharetrait-database-v1](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1) includes the complete data package prepared for release version. The sharetrait-database-v1, v1.0.0 is complete of: relational schema, organised data tables, and supporting documentation to allow local setup and use of the database. In addition to the full documentation of the design and implementation, version 1.0.0 includes tools and content that facilitate direct data access, integration, and query sharetrait data. 
Please refer to the **README.md** files within each sub-folder for detailed guidance on file content and usage.

### sharetrait-database-v1 folder overview structure 

The sharetrait-database-v1 folder as referred in this release version [![GitHub Release](https://img.shields.io/github/v/release/ShareTraitProject/ShareTraitDatabase?color=blue&logo=github)](https://github.com/ShareTraitProject/ShareTraitDatabase/releases/tag/v1.0.0), this includes the following components:

- db-documentation/: 
Contains documentation, schema design, database component definitions, dictionaries, and mappings to the ShareTrait dataset. 
- db-export/:
Provides the ShareTrait database in SQL format for version 1.0.0. 
- db-queries/:
Includes example SQL queries based on biological research questions. 
- db-tables/:
Contains CSV files with data values and mappings for importing into the ShareTrait tables. 
- db-publish/:
Lists documentation and files used in publications linked to this database version. 
- db-tools/:
Includes Python scripts for creating and interacting with the database. 

Access and usage of the DB and SQL files

Please follow the instructions provided in the repository’s documentation and the specific folders' README.md files.
Start with the documentation found in the folders db-export/ and db-tools/ for database setup.





---
> [!NOTE] 
Please note that this repository is active.
> For the latest version, please refer to the latest database release folder v1.0.0 [![GitHub Release](https://img.shields.io/github/v/release/ShareTraitProject/ShareTraitDatabase?color=blue&logo=github)](https://github.com/ShareTraitProject/ShareTraitDatabase/releases/tag/v1.0.0)  
release version maps to the bu folder: [sharetrait-database-v1](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1), last modified on 2025-07-23


