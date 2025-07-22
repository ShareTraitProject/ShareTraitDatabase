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

## folder overview

SharetraitDatabase v1 [repo](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1) contains the following structure and files list
```
ShareTraitProject/
├── otherrepos
├── ShareTraitDatabase/
|   ├── README.md
|   ├── LICENSE
|   ├── other-development-folders
│   ├── sharatrait-database-v1.0/
│   │   ├── db-documentation/
│   │       ├── ShareTrait-database-attributes-definition.csv
│   │       ├── ShareTrait-database-documentation-v20241108.pdf
│   │       ├── ShareTrait-database-schema-v1.png
│   │       ├── ShareTrait-database-tables-overview.csv
│   │       ├── ShareTrait-dataset-database-mapping.csv
│   │       ├── README.md
│   │   ├── db-export/
│   │       ├── ST_all.db
│   │       ├── README.md
│   │   ├── db-queries/
│   │       ├── master-query.sql
│   │       ├── query1.sql
│   │       ├── query2.sql
│   │       ├── README.md
│   │   ├── db-tables/
│   │       ├── acclimation_describe.csv
│   │       ├── acclimation-specification.csv
│   │       ├── chamber-describe.csv
│   │       ├── condition.csv
│   │       ├── contains.csv
│   │       ├── dataset.csv
│   │       ├── describe.csv
│   │       ├── experiment_setup.csv
│   │       ├── individual.csv
│   │       ├── located_in.csv
│   │       ├── manuscript.csv
│   │       ├── measurement.csv
│   │       ├── occurrence.csv
│   │       ├── place.csv
│   │       ├── population.csv
│   │       ├── publication.csv
│   │       ├── ref_taxonomy.csv
│   │       ├── respiratory_chamber.csv
│   │       ├── site.csv
│   │       ├── taxonomic_label.csv
│   │       ├── trait.csv
│   │       ├── README.md

---
```
### other

for any more information regarding the files shared, please contact Irene
