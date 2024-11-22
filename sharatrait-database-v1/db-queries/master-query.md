# question-query for master-query-all view

## Question

**master-query-all**:

### *Generate a query to provide as output the complete sharetrait version 1.0.0 published in a csv version*


## Query Reference

Name : [master-query.sql](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/master-query.sql)

Description: selects all the mapping items found in [shatrait db attribute mapping to sharetrait_dataset_col_name](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-dataset-database-mapping.csv) and connects all the tables listed in [db table overview](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-tables-overview.csv)

## Query template

This query template can be used directly from the sqlite3 window prompt or SQLiteStudio. MOre informartion how to query from the two options, please read our description [#how-to-access-and-use-the-db](https://github.com/ShareTraitProject/ShareTraitDatabase/edit/main/sharatrait-database-v1/db-export/README.md#how-to-access-and-use-the-db)

```sql
Select dataset.sharetrait_datasetid, dataset.date_contribution, dataset.reference_type, dataset.doi_dataset, manuscript.doi_manuscript, dataset.comments_reference, population.species_reported, ref_taxonomy.phylum_name, ref_taxonomy.class_name, ref_taxonomy.order_name, ref_taxonomy.family_name, ref_taxonomy.genus_name, ref_taxonomy.species_name, ref_taxonomy.taxonomy_db_name, ref_taxonomy.rank_level, ref_taxonomy.comment_taxonomy, site.site_realm_general, site.site_realm_specific, site.elevation_value, site.depth_value, occurrence.origin, located_in.location_description, place.location_name, located_in.latitude, located_in.longitude, occurrence.year_collection_initial, occurrence.year_collection_final, occurrence.observation_date_initial, occurrence.observation_date_final, occurrence.comment_location, measurement.experiment_location, 
MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.method_check END) AS "maintained", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.duration END) AS "condition-maintenance.duration", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.duration_generations END) AS "condition-maintenance.duration_generations", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.temperature END) AS "condition-maintenance.temperature", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.photoperiod END) AS "condition-maintenance.photoperiod", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.humidity END) AS "condition-maintenance.humidity", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.oxygen END) AS "condition-maintenancen.oxygen", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.carbon_dioxide END) AS "condition-maintenance.carbon_dioxide", trait.sharetrait_type, MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.salinity END) AS "condition-maintenance.salinity", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.ph END) AS "condition-maintenance.ph", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.oxygen_units END) AS "condition-maintenance.oxygen_units", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.carbon_dioxide_units END) AS "condition-maintenance.carbon_dioxide_units", MAX(CASE WHEN experiment_setup.condition_label = "maintenance" THEN m.food_type END) AS "condition-maintenance.food_type", 
MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.method_check END) AS "acclimated", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.duration END) AS "condition-acclimation.duration", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.temperature END) AS "condition-acclimation.temperature", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.salinity END) AS "condition-acclimation.salinity", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.ph END) AS "condition-acclimation.ph", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.oxygen END) AS "condition-acclimation.oxygen", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.carbon_dioxide END) AS "condition-acclimation.carbon_dioxide", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.photoperiod END) AS "condition-acclimation.photoperiod", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.humidity END) AS "condition-acclimation.humidity", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.oxygen_units END) AS "condition-acclimation.oxygen_units", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.carbon_dioxide_units END) AS "condition-acclimation.carbon_dioxide_units", MAX(CASE WHEN experiment_setup.condition_label = "acclimation" THEN a.food_type END) AS "condition-acclimation.food_type", 
MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.temperature END) AS "condition-test.temperature", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.oxygen END) AS "condition-test.oxygen", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.carbon_dioxide END) AS "condition-test.carbon_dioxide", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.oxygen_units END) AS "condition-test.oxygen_units", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.carbon_dioxide_units END) AS "condition-test.carbon_dioxide_units", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.photoperiod END) AS "condition-test.photoperiod", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.humidity END) AS "condition-test.humidity", measurement.comments_experimental_conditions, MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.food_type END) AS "condition-test.food_type", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.salinity END) AS "condition-test.salinity", MAX(CASE WHEN experiment_setup.condition_label = "test" THEN t.ph END) AS "condition-test.ph", individual.strategy_of_protection, individual.sex, trait.life_stage_general_initial, trait.life_stage_general_final, measurement.lifestage_specific_initial, measurement.lifestage_specific_final, measurement.life_stage_general, measurement.life_stage_specific, measurement.size_type, measurement.size_units, measurement.size_value_initial, measurement.size_value_final, measurement.size_value, individual.parent_size_type, individual.parent_size_units,individual.parental_size_value, individual.parent_age, individual.parent_age_units, individual.mating_method, individual.method_type, measurement.fecundity_temporal_unit, measurement.reproductive_stage,
individual.offspring_developmental_stage, individual.offspring_size_type, individual.offspring_size_units,individual.offspring_size_value, respiratory_chamber.metabolic_rate_type, acclimation_specification.acclimation_chamber, acclimation_specification.fasting_time, respiratory_chamber.sensor_type,respiratory_chamber.respiration_volume, respiratory_chamber.delay_time, respiratory_chamber.respiratory_chamber_material, respiratory_chamber.incubation_time, respiratory_chamber.respirometry_type, respiratory_chamber.breathing_mode, measurement.trait_value, measurement.trait_unit, measurement.comment_trait, measurement.trait_error_estimate, measurement.trait_error_type, measurement.sample_size, measurement.trait_converted, measurement.fresh_mass
FROM measurement
LEFT JOIN individual ON individual.individual_pk = measurement.individual_pk
LEFT JOIN contains ON contains.individual_pk = individual.individual_pk
LEFT JOIN population ON population.population_pk = contains.population_pk
LEFT JOIN taxonomic_label ON taxonomic_label.population_pk = population.population_pk
LEFT JOIN ref_taxonomy ON ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk
LEFT JOIN occurrence ON occurrence.population_pk = population.population_pk
LEFT JOIN site ON site.site_pk = occurrence.site_pk
LEFT JOIN located_in ON located_in.site_pk = site.site_pk
LEFT JOIN place ON place.place_pk = located_in.place_pk
LEFT JOIN describe ON population.population_pk = describe.population_pk
LEFT JOIN dataset ON describe.dataset_pk = dataset.dataset_pk
LEFT JOIN publication ON dataset.dataset_pk = publication.dataset_pk
LEFT JOIN manuscript ON publication.manuscript_pk = manuscript.manuscript_pk
LEFT JOIN trait ON trait.trait_pk = measurement.trait_pk
LEFT JOIN chamber_describe ON chamber_describe.measurement_pk = measurement.measurement_pk
LEFT JOIN respiratory_chamber ON respiratory_chamber.technique_pk = chamber_describe.technique_pk
LEFT JOIN acclimation_describe ON acclimation_describe.measurement_pk = measurement.measurement_pk
LEFT JOIN acclimation_specification ON acclimation_specification.acclimation_pk = acclimation_describe.acclimation_pk
LEFT JOIN experiment_setup ON experiment_setup.measurement_pk = measurement.measurement_pk
LEFT JOIN condition t ON experiment_setup.condition_pk = t.condition_pk AND t.method_check = "test"
LEFT JOIN condition m ON experiment_setup.condition_pk = m.condition_pk AND m.method_check = "maintenance"
LEFT JOIN condition a ON experiment_setup.condition_pk = a.condition_pk AND a.method_check = "acclimation"
GROUP BY measurement.measurement_pk
```


## View the Query output

 1. Open the terminal and use the sqlite3 command to run the query file in sql format against the sharetrait database you have stored locally. Make sure you have the paths for where the database is stored and the info path where the query is stored.

```
sqlite3 /path/to/ST_all.db < /path/to/master-query.sql
```

  2. you can also save the sql query view in the same folder where the database is saved. In this case:

```
sqlite3 ST_all.db < master-query.sql
```

  3. you can verify by the view by connecting to sharetrait database and check if the query view exists

```
sqlite3 ST_all.db < master-query.sql
```

  4. Now you can run the query by using a SELECT command on the view master-query. For example to view the first row of the master-table. Note that the view for this query is called master-query-all. We will keep this term to access data: 

```sql
SELECT * FROM master-query-all LIMIT 1;
```

You can also of course view this data select directly in the SQLStudio by selecting the table "master-query-all".

  5. you can save by using the .output command else Tools -> Export -> Query Result in SQLiteStudio [^1].

 ```
      sqlite> .headers on
      sqlite> .mode csv
      sqlite> .output /path/to/master-query-output.csv
      sqlite> 
 ```

A version of the query output is found here: [master-query-output.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/master-query-output.csv)
  
## Comments

> [!NOTE]
> - In terms of values, in particular to measurements and trait characteristics, this query completes all information with complete association as found in the original dataset.
> - However, there is some extensions of information and this is based on testing the database. For example, sharetrait dataset does not contain taxonomy information. Or better, the only information that it contains deals with the attribute "species_reported".
> - However, as we designed and implemented the Taxonomy category, taking into account the existence of reference names, indipendendly of the source (tree of life, catalogue of life, ncbi..), we have included some parameters to test the functions. Such as adding a genus name for testing aggregations based on group of species. Ideally, someone will need to make sure that the reference namings and hierarchies are included.
> - Another difference which is not making the output incorrect but just using a different term is for the Method category in which there is metadata dealing with the condition and circumstances the measurement was collected/obtained.
> - In this case, because different situations do contain the same type of metadata (e.g. temperature, humidity for instance), we designed the condition to contain a type field (such as experiment, maintenance...). For this reason, the attribute of sharetrait dataset for "maintained" and "acclimed" that contains a "yes" and "no" features, but not for "tested" which for some reason it does not exist in sharetrait dataset, even though metadata fields are present. We then decided to have those labelled referred for the type instead of yes and no. Thus, if metadata of maintenance exists, then the value of condition is "maintained", meaning that the metadata exists, else all those values are empty. For the master query this is not actually seen as it returns the correct replication of a csv file, by providing empty values for those conditions. 

---

[^1]: Export SQLite database to a CSV file using SQliteStudio: https://www.sqlitetutorial.net/sqlite-export-csv/
