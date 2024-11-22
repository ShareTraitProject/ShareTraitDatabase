# question-query for Aphidius view

## Question

**Aphidius**:

### *Provide me all trait information for the genus "Aphidius" belonging to development trait type*


## Query Reference

Name : [Aphidius.sql](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/Aphidius.sql)

Description: selects all the trait measurements being part of development sharetrait type, indipendently of the characteristics and only linked to all the population belonging to the group "Aphidius"

## Query template

This query template can be used directly from the sqlite3 window prompt or SQLiteStudio. More informartion how to query from the two options, please read our description [#how-to-access-and-use-the-db](https://github.com/ShareTraitProject/ShareTraitDatabase/edit/main/sharatrait-database-v1/db-export/README.md#how-to-access-and-use-the-db)

```sql
Select measurement.trait_type, measurement.trait_value, measurement.trait_unit, individual.individual_pk, trait.life_stage_general_initial, trait.life_stage_general_final, population.species_reported, ref_taxonomy.scientific_name
FROM measurement
LEFT JOIN individual ON individual.individual_pk = measurement.individual_pk
LEFT JOIN contains ON contains.individual_pk = individual.individual_pk
LEFT JOIN population ON population.population_pk = contains.population_pk
LEFT JOIN taxonomic_label ON taxonomic_label.population_pk = population.population_pk
LEFT JOIN ref_taxonomy ON ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk
LEFT JOIN trait ON trait.trait_pk = measurement.trait_pk
WHERE measurement.trait_type = "development" AND ref_taxonomy.genus_name = "Aphidius"
```


## View the Query output

 1. Open the terminal and use the sqlite3 command to run the query file in sql format against the sharetrait database you have stored locally. Make sure you have the paths for where the database is stored and the info path where the query is stored.

```
sqlite3 /path/to/ST_all.db < /path/to/Aphidius.sql
```

  2. you can also save the sql query view in the same folder where the database is saved. In this case:

```
sqlite3 ST_all.db < Aphidius.sql
```

  3. you can verify by the view by connecting to sharetrait database and check if the query view exists

```
sqlite3 .schema Aphidius
```

  4. Now you can run the query by using a SELECT command on the view master-query. For example to view the first row of the Aphidius table view: 

```sql
SELECT * FROM Aphidius LIMIT 1;
```

You can also of course view this data select directly in the SQLStudio by selecting the table "Aphidius".

  5. you can save by using the .output command else Tools -> Export -> Query Result in SQLiteStudio [^1].

 ```
      sqlite> .headers on
      sqlite> .mode csv
      sqlite> .output /path/to/Aphidius-output.csv
      sqlite> 
 ```

A version of the query output is found here: [Aphidius-output.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/Aphidius-output.csv)
  
## Comments

---

[^1]: Export SQLite database to a CSV file using SQliteStudio: https://www.sqlitetutorial.net/sqlite-export-csv/
