# ShareTrait DataBase SQL

This repository contains the ShareTrait DataBase (STDB) SQL of [ShareTrait Project Data](https://github.com/ShareTraitProject) 

## Repository Structure

The SharetraitDatabase repository is structured as follows. Only the ShareTraitDatabase repository is described

```
ShareTraitProject/
├── other-repos
├── ShareTraitDatabase/
|   ├── README.md
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
|   ├── mappings
│   ├── sharatrait-database-v1/
│   │   ├── db-documentation/
│   │   ├── db-export/
│   │   ├── db-queries/
│   │   ├── db-tables/
│   │   ├── db-export/
|   ├── tables

---
```

## Repository general description

Hereby we describe the general content found for each folder of the directory. Please make sure you look at the README.md of each folder for more information regarding the content of the files in the folders

| folder name | description | link | last modified |
| :--- | :--- | :--- | :--- | 
| db | sharetrait database sql versions  | [link](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/db) | 2024-06-12 |
| diagrams | database schemas and models versions  | [link](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/diagrams) | 2024-08-18 |
| documentation | definitions and description of the ER model | [link](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/documentation) | 2024-08-01 |
| mappings | mappings for aligning db attributes to sharetrait previous versions | [link](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/mappings)| 2024-11-05 |
| sharetrait-database-v1 | | | |
| tables | | | |







---

# ShareTrait DataBase (STDB) SQL version 1.2.0

## prerequirements

- please follow the instructions found in db-export folder for using sharetrait db locally.

## content for sharetrait database db-version 1.2.0 folder : sharatrait-database-v1/
<!---
Please make sure you update sharetrait database version 1.0 to database version 1.2.0 which will be the one to publish on zenodo
-->
The sharetrait database v1 folder contains the following subfolders:
- db-documentation: documentation, schema design and db components definition, mappings to sharetrait dataset
- db-export: sharetrait sql format db version 1.0.0
- db-queries: queries based on biological questions
- db-tables: list of csv files containing the values to import and mapping to the sharetrait tables
- db-publish: list of documentation used for publications linked to sharetrait-database-v1
### other

for any more information regarding the files shared, please contact Irene

---
> [!NOTE] 
Please note that this repository is active 
> For the latest version, please refer to the latest database release folder 
Current version: [sharatrait-database-v1](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1), last modified on 2025-07-23
