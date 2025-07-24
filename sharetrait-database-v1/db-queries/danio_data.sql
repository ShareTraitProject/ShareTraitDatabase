--
-- File generated with SQLiteStudio v3.4.4 on Fri Nov 22 15:45:41 2024
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- View: danio_data
CREATE VIEW IF NOT EXISTS danio_data AS
    SELECT DISTINCT dataset.dataset_pk,
                    dataset.title_dataset,
                    dataset.dataset_publisher,
                    dataset.doi_dataset,
                    dataset.year_publication,
                    population.species_reported,
                    measurement.trait_type
      FROM dataset,
           describe,
           population,
           taxonomic_label,
           ref_taxonomy,
           contains,
           individual,
           measurement
     WHERE ref_taxonomy.genus_name = "Danio" AND 
           ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk AND 
           taxonomic_label.population_pk = population.population_pk AND 
           population.population_pk = describe.population_pk AND 
           describe.dataset_pk = dataset.dataset_pk AND 
           population.population_pk = contains.population_pk AND 
           contains.individual_pk = individual.individual_pk AND 
           individual.individual_pk = measurement.individual_pk;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
