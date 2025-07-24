# documentation folder for sharetrait database version 1.0.0

- name of folder: `db-documentation`
- folder type: informative documents and diagrams for sharetrait database
- file formats: csv, pdf, png

## folder description

This folder contains information about the definition and description of the components of the database.
The components refer to the tables and field characteristics of the tables constituting the ShareTrait DataBase version 1.0.0

## file list name and description for the db-documentation folder

| file_name | format | file_description |
| :--- | --- | :--- |
| ShareTrait-database-attributes-definition.csv | csv | data dictionary, complete list of 196 attributes definitions belonging to the 21 tables of sharetrait db as listed in db-tables (share link) |
| ShareTrait-database-documentation-v20250723.pdf | PDF | version n. 20250723 of the description of the conceptual model for the design and development of the database |
| ShareTrait-database-schema-v1.png | png | sharetrait database schema for version 1.0.0, last modified 2024-11-02. This is a download png format of the original file made with the online diagram software draw.io, version 24.8.4  |
| ShareTrait-database-tables-overview.csv | csv | information regarding the amount of attributes and records for each database table |
| ShareTrait-dataset-database-mapping.csv | csv | [sharetrait dataset](https://github.com/ShareTraitProject/ShareTrait/blob/main/ShareTrait_DB/v1.0.0/3_release/ShareTrait_MetaData_v1.0.0.csv) attribute mapping to the sharetrait database v1.0.0 attributes |

### definition of headers in file sharatrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv

- file name: `ShareTrait-database-attributes-definition.csv`
- file url: [github-ref-definition](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv)
- file description:
  
| column_name | column_definition |
| :--- | :--- |
| table_refnum | reference internal id used to reference to [ShareTrait-database-tables-overview.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-tables-overview.csv) specifications and characteristics |
| category_name | name of category as defined in [ShareTrait-database-documentation-v20250723.pdf](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-documentation-v20250723.pdf) and used in sharetrait database version 1.0.0 |
| table_name | name of table as defined in [ShareTrait-database-documentation-v20250723.pdf](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-documentation-v20250723.pdf) and for the data dictionary, [ShareTrait-database-attributes-definition.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) and used in sharetrait database version 1.0.0 |
| attribute_name | name of attribute as given and used in sharetrait database version 1.0 |
| type | type of attribute. THis provides the following : if it is either a primary key or foreign key attribute, and the specifications that can be {VARCHAR, TEXT, INT and DECIMAL}. For date we use Text type at the moment |
| requirement | specifications of the attribute. Possible values {Mandatory} or {Optional}. Mandatory is a required field to be always provided and cannot be NULL, and Optional is a condition that is not mandatory, so it is not always required. Usually it is related to a specification of a record |
| definition | short description of what the attribute provides |
| sharetrait_dataset_col_name | reference to column_name of sharetrait dataset as referenced in [ShareTrait_MetaData_v1.0.0.csv](https://github.com/ShareTraitProject/ShareTrait/blob/main/ShareTrait_DB/v1.0.0/3_release/ShareTrait_MetaData_v1.0.0.csv) |
| example_value | actual possible value type that can exist in sharetrait database version 1.0.0 |

### definition of headers in sharatrait-database-v1/db-documentation/ShareTrait-database-overview.csv

- file name: `ShareTrait-database-overview.csv`
- file url: [github-ref-overview](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-tables-overview.csv)
- file description:
  
| column_name | column_definition |
| :--- | :--- |
| table | table reference internal id used to map to [ShareTrait-attributes-definition.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) |
| table name | sharetrait database version 1.0 table name as defined in [ShareTrait-attributes-definition.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) |
| attribute count (with pks/fks) | number of metadata fields and keys (primar or foreign keys) belonging to the table |
| number of records | number of records (i.e. rows) contained for each table |

### definition of headers in sharatrait-database-v1/db-documentation/ShareTrait-dataset-database-mapping.csv

- file name: `ShareTrait-dataset-database-mapping.csv`
- file url: [github-ref-mapping](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-dataset-database-mapping.csv)
- file description:
  
| column_name | column_definition |
| :--- | :--- |
| sharetrait_dataset_col_name | this column name is the reference to [sharetrait dataset metadata definition csv](https://github.com/ShareTraitProject/ShareTrait/blob/main/ShareTrait_DB/v1.0.0/3_release/ShareTrait_MetaData_v1.0.0.csv) header label |
| sharetrait db attribute | this column name refers to the attribute label as defined in [sharetrait database attribute](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) header attribute label |

### definition of annotation used in sharatrait-database-v1/db-documentation/ShareTrait-database-schema-v1.png

- file name: `ShareTrait-database-schema-v1.png`
- file url: [github-ref-schema](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-schema-v1.png)
- file description:
the annotations and constraints provided in the schema refer to the complete documentation description in [ShareTrait-database-documentation-v20250723.pdf](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-documentation/ShareTrait-database-documentation-v20250723.pdf)







