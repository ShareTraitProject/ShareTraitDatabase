<!---
This README.md was generated for the Zenodo publication version 1.2.0 DOI: https://doi.org/10.5281/zenodo.14826294
--->

# ShareTrait Organisation - ShareTrait DataBase SQL 

- repository title: **ShareTrait: a data portal for making trait data interoperable and reusable**
- version: 1.2.0
- publish date: 2025-02-07
- description: DataBase SQL version of `ShareTrait_DataBase_v1.0.0.csv`, Published in Zenodo July 12, 2023 | version 1.0.0, [DOI](https://doi.org/10.5281/zenodo.8138904).

## List of file names and description provided in the repository

This repository contains 5 files (including this README.md file):

- `ShareTrait-database-v1.2.0.db`: ShareTrait DB database version 1.2.0
- `master-query-all.sql`: SQL query for generating the master query, see [Master Query SQL file description section
](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-queries/master-query.md) for running the query.
- `master-query-output.csv`: output file by running the SQL query `master-query-all.sql`.
- `ShareTrait-dataset-database-mapping.csv`: contains the ShareTrait dataset attribute mapping to the ShareTrait database v1.2.0 attributes that are provided in the master-query.csv output file.  

## Master query files and description

- The SQL file `master-query-all.sql` is a query that generates the complete Sharetrait dataset version 1.0.0, csv version, under the name ShareTrait_DataBase_v1.0.0.csv, Published in Zenodo July 12, 2023 | Version 1.0.0, [DOI](https://doi.org/10.5281/zenodo.8138904).
- the `master-query-all.sql` selects all the mapping attributes items found in [Shatrait DB attribute mapping to sharetrait_dataset_col_name](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-dataset-database-mapping.csv), thus replicates the complete record list of the dataset `ShareTrait_DataBase_v1.0.0.csv`, Published in Zenodo July 12, 2023 | Version 1.0.0, [DOI](https://doi.org/10.5281/zenodo.8138904)
- the query `master-query-all.sql` can be used directly from the Sqlite3 window prompt or SQLiteStudio.
- In order to run the SQL query and obtain the identical file to `ShareTrait_DataBase_v1.0.0.csv`, Published in Zenodo July 12, 2023 | Version 1.0.0, [DOI](https://doi.org/10.5281/zenodo.8138904), you can run the query file in SQL format against the Sharetrait database (file db name `ShareTrait-database-v1.2.0.db`) that you have downloaded via this repository.
- The only difference between the two versions will be found in the header.  `master-query-output.csv` contains as header the attributes selected from the database that correspond to the original sharetrait dataset v1.0.0. The mapping file `ShareTrait-dataset-database-mapping.csv` found in this repository provides the corresponding mapping to the headers uses in `ShareTrait_MetaData_v1.0.0.csv`, accessible via [Zenodo ShareTrait]()
- In terms of values, in particular to measurements and trait characteristics, this query reproduces all information with complete association as found in the original dataset of version 1.0.0.


## Query view of file master-query-all.sql 


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



## how to access and use the files

- The simple way to use these files is that you download all the files of this repository in one folder in your local environment.
- You can access the database (.db) by using SQLiteStudio or SQLite [^1].
- You can save the run the query against the database by using this command line in the terminal. If you have downloaded the files in the same folder, then the command is simply run this command from the terminal:
  
```
sqlite3 ShareTrait-database-v1.2.0.db < master-query-all.sql
```

Please note that you have to have sqlite3 downloaded in your system. 

You can also place the complete files paths (database and sql query) of the files for running the query. 


## support

For any questions about ShareTrait DataBase SQL version 1.2.0, you can contact the following developers:

- Irene Martorelli: i.martorelli@vu.nl
- Brett Olivier: b.g.olivier@vu.nl

> [!NOTE] 
For more information and documentation, please go and refer to ShareTrait development repositories [^2].

---

[^1]: Export SQLite database to a CSV file using SQliteStudio: https://www.sqlitetutorial.net/sqlite-export-csv/
[^2]: ShareTraitProject: https://github.com/ShareTraitProject





