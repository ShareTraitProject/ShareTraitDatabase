## db templates for testing

### general information about the db versions

please follow the sharetrait-database versions for fixed versions of sharetrait
all db versions are provided with db extension and sql version, using same naming

### overview of development versions used for testing sections of database 

| dev folder | db version |  comment | model ref | table ref |
| --- | ---- | --- | ---  | --- |
| STdb_v01 | STdb_v01.sql | [STdb_v01.6sql](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/db/STdb_v01) | db sql test version 1.6 for sharetrait, only entities for S,T,E are complete | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTrait_categories_0-9-4-MOLTES_v0.2.2.drawio.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v01) |
| STdb_v01 | STdb_v01.db | [STdb_v01.db](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/db/STdb_v01) | db test version 1.6 for sharetrait, only entities for S,T,E are complete | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTrait_categories_0-9-4-MOLTES_v0.2.2.drawio.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v01) |
| stdb-all | STdb-all-v02.db | [STdb-all-v02.db](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/db/stdb-all/stdb-all-v02.db) | db version test for sharetrait with empty templates | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTraitDB-DOMELT-v1.0.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v02) |
| stdb-all | STdb-all-v02.sql | [STdb-all-v02.sql](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/db/stdb-all/stdb-all-v02.sql) | db version test for sharetrait with empty templates | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTraitDB-DOMELT-v1.0.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v02) |
| stdb-all | stdb-all-v1.0.0.db | [STdb-all-v02.db](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/db/stdb-all/stdb-all-v1.0.0.db) | db version test for sharetrait with complete trait list dev, ,et_rate, fec | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTraitDB-DOMELT-v1.0.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v02) |
| stdb-all | stdb-all-v1.0.0.sql | [STdb-all-v02.sql](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/db/stdb-all/stdb-all-v1.0.0.sql) | sql db version test for sharetrait with complete trait list dev, met_rate, fec | [model ref](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/diagrams/ShareTraitDB-DOMELT-v1.0.png) | [table ref](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/tables/table_values_v02) |

### db version software

all db versions were exported by using SQLiteStudio v3.4.4 

### sync with sharetrait db

- current web application [#syncing-with-sharetraitdatabase](https://github.com/ShareTraitProject/ShareTraitWebsite?tab=readme-ov-file#syncing-with-sharetraitdatabase) refers to development version (Syncing with ShareTraitDatabase) having url ../ShareTraitDatabase/db/stdb-all/stdb-all-v1.0.0.db. Please refer to the release version database `sharatrait-database-v1`

> [!NOTE] 
Please note that this db folder contains development versions of the database. For the latest version, please refer to the latest database release folder. Current: [sharatrait-database-v1](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1), last modified on 2025-07-23
