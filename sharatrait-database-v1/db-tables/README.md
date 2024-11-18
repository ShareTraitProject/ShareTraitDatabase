# tables of sharetrait database version 1.0.0

- the tables provided in db-tables folder are in csv version based on the dump sql command. For any other versions required please contact Irene 

## folder description

The list of tables belong to ShareTrait DB version 1.0.0. 
The tables are provided in a csv format and map to the table template names of [STDB-template-v1.sql]() - add?

## mapping table files to database table templates

*please note that all reference links belong to the sharetrait-database-v1 folder of this repo.*
- all db-table names and descriptions can be found in [ShareTrait-database-attributes-definition.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) of the documentation folder

- definition of headers in ShareTrait-database-attributes-definition.csv
  
| column_name | column_definition |
| :--- | --- |
| table_refnum | reference internal id used to reference to [ShareTrait-database-tables-overview.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-tables-overview.csv)) specifications and characteristics |
| category_name | name of category as defined in [ShareTrait-database-documentation-v20241108.pdf](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-documentation-v20241108.pdf) and used in sharetrait database version 1.0.0 |
| table_name | name of table as defined in [ShareTrait-database-documentation-v20241108.pdf](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-documentation-v20241108.pdf) and used in sharetrait database version 1.0.0 |
| attribute_name | name of attribute as given and used in sharetrait database version 1.0 |
| type | type of attribute. THis provides the following : if it is either a primary key or foreign key attribute, and the specifications that can be {VARCHAR, TEXT, INT and DECIMAL}. For date we use Text type at the moment |
| requirement | specifications of the attribute. Possible values {Mandatory} or {Optional}. Mandatory is a required field to be always provided and cannot be NULL, and Optional is a condition that is not mandatory, so it is not always required. Usually it is related to a specification of a record |
| definition | short description of what the attribute provides |
| sharetrait_dataset_col_name | reference to column_name of sharetrait dataset as referenced in [ShareTrait_MetaData_v1.0.0.csv](https://github.com/ShareTraitProject/ShareTrait/blob/main/ShareTrait_DB/v1.0.0/3_release/ShareTrait_MetaData_v1.0.0.csv) |
| example_value | actual possible value type that can exist in sharetrait database version 1.0.0 |

- append definition of other files
