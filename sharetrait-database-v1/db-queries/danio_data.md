# question-query for danio_data view

## Question

**Danio**:

### *Is there any sharetrait dataset that deals with Danio genus? If yes, specify which datasets are published and in which repository can i find them and what type of trait is measured"*

## Query Reference

Name : [danio_data.sql](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharetrait-database-v1/db-queries/danio_data.sql)

Description: searchers for all the datasets that specified a population belonging to the Danio group. It also specifies which of these datasets are published in available repositories and which type of trait does the study deal with?

## Query template

This query template can be used directly from the sqlite3 window prompt or SQLiteStudio. More informartion how to query from the two options, please read our description [#how-to-access-and-use-the-db](https://github.com/ShareTraitProject/ShareTraitDatabase/edit/main/sharatrait-database-v1/db-export/README.md#how-to-access-and-use-the-db)

```sql
Select distinct dataset.dataset_pk, dataset.title_dataset, dataset.dataset_publisher, dataset.doi_dataset, dataset.year_publication, population.species_reported, measurement.trait_type
from dataset, describe, population, taxonomic_label, ref_taxonomy, contains, individual, measurement
where ref_taxonomy.genus_name = "Danio" AND ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk AND taxonomic_label.population_pk = population.population_pk AND population.population_pk = describe.population_pk AND describe.dataset_pk = dataset.dataset_pk
AND population.population_pk = contains.population_pk AND contains.individual_pk = individual.individual_pk AND individual.individual_pk = measurement.individual_pk
```


## View the Query output

 1. Open the terminal and use the sqlite3 command to run the query file in sql format against the sharetrait database you have stored locally. Make sure you have the paths for where the database is stored and the info path where the query is stored.

```
sqlite3 /path/to/ST_all.db < /path/to/danio_data.sql
```

  2. you can also save the sql query view in the same folder where the database is saved. In this case:

```
sqlite3 ST_all.db < danio_data.sql
```

  3. you can verify by the view by connecting to sharetrait database and check if the query view exists

```
sqlite3 .schema danio_data
```

  4. Now you can run the query by using a SELECT command on the view master-query. For example to view the output of the Danio_data table view: 

```sql
SELECT * FROM danio_data;
```

You can also of course view this data select directly in the SQLStudio by selecting the table "danio_data".

  5. you can save by using the .output command else Tools -> Export -> Query Result in SQLiteStudio [^1].

 ```
      sqlite> .headers on
      sqlite> .mode csv
      sqlite> .output /path/to/danio_data-output.csv
      sqlite> 
 ```

A version of the query output is found here: [danio_data-output.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/danio_data-output.csv)
  
## Comments

- A dataset in sharetratait database version 1.0 include and you can query and view data from datasets that are also not published. Please read the type attributes [columns attributes from the sharetrait tables](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-attributes-definition.csv) that you can add in the select and add them in your query. 
---

[^1]: Export SQLite database to a CSV file using SQliteStudio: https://www.sqlitetutorial.net/sqlite-export-csv/
