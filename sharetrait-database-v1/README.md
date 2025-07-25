# ShareTrait DataBase (STDB) SQL (version 1.2.0)

## pre-requirements

- please follow the instructions found in [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-export) folder for using sharetrait db locally.

## content for sharetrait database db-version 1.2.0 folder : [sharetrait-database-v1/](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1)

The sharetrait database v1 folder contains the following subfolders:
- [db-documentation](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-documentation): documentation, schema design and db components definition, mappings to sharetrait dataset
- [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-export): sharetrait sql format db version 1.0.0
- [db-queries](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-queries): queries based on biological questions
- [db-tables](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-tables): list of csv files containing the values to import and mapping to the sharetrait tables
- [db-publish](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-publish): list of documentation used for publications linked to sharetrait-database-v1
- [db-tools](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1/db-tools): list of py scripts for creating the database

## folder overview

SharetraitDatabase v1 [repo](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharetrait-database-v1) contains the following structure and files list
```
ShareTraitProject/
├── other-repos
├── ShareTraitDatabase/
|   ├── README.md
|   ├── LICENSE
|   ├── CONTRIBUTORS
|   ├── CITATION.cff
|   ├── other-development-folders
│   ├── sharatrait-database-v1.0/
│   │   ├── db-documentation/
│   │       ├── ShareTrait-database-attributes-definition.csv
│   │       ├── ShareTrait-database-documentation-v20250723.pdf
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
│   │       ├── acclimation_specification.csv
│   │       ├── chamber_describe.csv
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
│   │   ├── db-export/
│   │       ├── zenodo_20250207
│   │           ├── README.md
│   │           ├── CITATION.cff
│   │       ├── zenodo_20250724
│   │           ├── README.md
│   │           ├── CITATION.cff
│   │       ├── README.md
│   │   ├── db-tools/
│   │           ├── README.md
│   │           ├── LICENSE
│   │           ├── build-sharetrait-db-v1.py

---
```
### other

for any more information regarding the files shared, please contact Irene (@irenemartorelli)
