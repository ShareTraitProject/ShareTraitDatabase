"""
ShareTraitDatabase - sharetrait-database-v1 

Irene Martorelli (@imartorelli)
Vrije Amsterdam Universiteit (VU)

Permission to use, modify, and distribute this software is given under the
terms of the STDB (BSD style) license. See LICENSE that came with
this distribution for specifics.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
Irene Martorelli
"""
import sqlite3
import pandas as pd
import os

# Connect to SQLite database 
db_name = "sharetrait-db-test.db"
table_folder = "table-folder"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Recreate tables (first drop if exist)
cursor.executescript("""
DROP TABLE IF EXISTS trait;
DROP TABLE IF EXISTS individual;
DROP TABLE IF EXISTS measurement;
DROP TABLE IF EXISTS acclimation_describe;
DROP TABLE IF EXISTS acclimation_specification;
DROP TABLE IF EXISTS chamber_describe;
DROP TABLE IF EXISTS condition;
DROP TABLE IF EXISTS contains;
DROP TABLE IF EXISTS dataset;
DROP TABLE IF EXISTS describe;
DROP TABLE IF EXISTS experiment_setup;
DROP TABLE IF EXISTS located_in;
DROP TABLE IF EXISTS manuscript;
DROP TABLE IF EXISTS occurrence;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS population; 
DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS ref_taxonomy; 
DROP TABLE IF EXISTS respiratory_chamber;
DROP TABLE IF EXISTS site;
DROP TABLE IF EXISTS taxonomic_label;                                                                                                                                                                                                                                                                                                                                                                 

CREATE TABLE IF NOT EXISTS trait (
    trait_pk                   VARCHAR(30) PRIMARY KEY NOT NULL,
    trait_name                 VARCHAR(256),
    trait_id                   VARCHAR(30),
    sharetrait_type            VARCHAR(256),
    trait_type                 VARCHAR(256),
    trait_condition            TEXT,
    trait_parentid             VARCHAR(30),
    life_stage_general_initial VARCHAR(256),
    life_stage_general_final   VARCHAR(256),
    trait_definition           TEXT,
    trait_definition_source    TEXT,
    trait_unit                 VARCHAR(30),
    trait_comment              TEXT
);

CREATE TABLE IF NOT EXISTS individual (
    individual_pk                 VARCHAR(30) PRIMARY KEY NOT NULL,
    individual_id                 VARCHAR(30),
    representative_stage          VARCHAR(30),
    sex                           VARCHAR(30),
    individual_type               VARCHAR(30),
    individual_parentpk           VARCHAR(30),
    parent_id                     VARCHAR(30),
    parental_size_value           DECIMAL(8,2),
    parent_size_units             VARCHAR(30),
    parent_size_type              VARCHAR(30),
    parent_age                    INT,
    parent_age_units              VARCHAR(30),
    mating_method                 VARCHAR(256),
    method_type                   VARCHAR(256),
    offspring_developmental_stage VARCHAR(256),
    offspring_size_type           VARCHAR(256),
    offspring_size_units          VARCHAR(256),
    offspring_size_value          DECIMAL(8,2),
    strategy_of_protection        TEXT,
    description_individual        TEXT,
    comment                       TEXT
);

CREATE TABLE IF NOT EXISTS measurement (
    measurement_pk                   VARCHAR (30)   PRIMARY KEY
                                                    NOT NULL,
    individual_pk                    VARCHAR (30),
    trait_pk                         VARCHAR (30),
    trait_type                       VARCHAR (30),
    trait_value                      DECIMAL (8, 4),
    trait_unit                       VARCHAR (30),
    trait_error_estimate             VARCHAR (30),
    trait_error_type                 VARCHAR (30),
    trait_converted                  TEXT,
    individual_developmental_stage   VARCHAR (30),
    fresh_mass                       DECIMAL (8, 2),
    fresh_mass_unit                  VARCHAR (30),
    sample_size                      VARCHAR (30),
    size_condition                   VARCHAR (30),
    size_value_initial               DECIMAL (8, 2),
    size_value_final                 DECIMAL (8, 2),
    size_value                       DECIMAL (8, 2),
    size_units                       VARCHAR (30),
    size_type                        VARCHAR (30),
    life_stage_general               VARCHAR (256),
    life_stage_specific              VARCHAR (256),
    lifestage_specific_initial       VARCHAR (256),
    lifestage_specific_final         VARCHAR (256),
    comment_trait                    TEXT,
    measure_date                     TEXT,
    fecundity_temporal_unit          TEXT,
    reproductive_stage               TEXT,
    experiment_location              TEXT,
    comments_experimental_conditions TEXT,
    FOREIGN KEY (
        individual_pk
    )
    REFERENCES individual (individual_pk),
    FOREIGN KEY (
        trait_pk
    )
    REFERENCES trait (trait_pk) 
);

CREATE TABLE IF NOT EXISTS acclimation_describe (
    measurement_pk     VARCHAR (30) NOT NULL,
    acclimation_pk     VARCHAR (30) NOT NULL,
    specification_date VARCHAR (30),
    PRIMARY KEY (
        measurement_pk,
        acclimation_pk
    ),
    FOREIGN KEY (
        measurement_pk
    )
    REFERENCES measurement (measurement_pk),
    FOREIGN KEY (
        acclimation_pk
    )
    REFERENCES acclimation_specification (acclimation_pk) 
);

CREATE TABLE IF NOT EXISTS acclimation_specification (
    acclimation_pk      VARCHAR (30)  PRIMARY KEY
                                      NOT NULL,
    acclimation_mating  VARCHAR (256),
    acclimation_chamber TEXT,
    fasting_time        VARCHAR (30),
    fasting_unit        VARCHAR (30) 
);

CREATE TABLE IF NOT EXISTS chamber_describe (
    measurement_pk     VARCHAR (30),
    technique_pk       VARCHAR (30),
    specification_date TEXT,
    PRIMARY KEY (
        measurement_pk,
        technique_pk
    ),
    FOREIGN KEY (
        measurement_pk
    )
    REFERENCES measurement (measurement_pk),
    FOREIGN KEY (
        technique_pk
    )
    REFERENCES respiratory_chamber (technique_pk) 
);

CREATE TABLE IF NOT EXISTS condition (
    condition_pk         VARCHAR (30)   PRIMARY KEY
                                        NOT NULL,
    temperature          DECIMAL (8, 2),
    photoperiod          TEXT,
    humidity             DECIMAL (4, 2),
    oxygen               DECIMAL (8, 2),
    carbon_dioxide       DECIMAL (8, 2),
    salinity             DECIMAL (8, 2),
    pH                   DECIMAL (8, 2),
    oxygen_units         VARCHAR (30),
    carbon_dioxide_units VARCHAR (30),
    food_type            TEXT,
    duration             INT,
    duration_generations TEXT,
    method_check         TEXT
);
                     
CREATE TABLE IF NOT EXISTS contains (
    individual_pk VARCHAR (30),
    population_pk VARCHAR (30),
    PRIMARY KEY (
        individual_pk,
        population_pk
    ),
    FOREIGN KEY (
        individual_pk
    )
    REFERENCES individual (individual_pk),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk) 
);
                     
CREATE TABLE IF NOT EXISTS dataset (
    dataset_pk           VARCHAR (30)  PRIMARY KEY
                                       NOT NULL,
    title_dataset        TEXT,
    doi_dataset          VARCHAR (256),
    sharetrait_datasetid TEXT,
    reference_type       VARCHAR (64),
    dataset_type         VARCHAR (64),
    dataset_publisher    VARCHAR (64),
    dataset_licence      VARCHAR (64),
    dataset_version      VARCHAR (64),
    dataset_citation     TEXT,
    date_publication     TEXT,
    year_publication     INT,
    date_contribution    VARCHAR (64),
    dataset_trait        VARCHAR (64),
    dataset_comment      TEXT,
    comments_reference   TEXT
);
                     
CREATE TABLE IF NOT EXISTS describe (
    dataset_pk    VARCHAR (30),
    population_pk VARCHAR (30),
    date_describe TEXT,
    date_iso      TEXT,
    year          INT,
    PRIMARY KEY (
        dataset_pk,
        population_pk
    ),
    FOREIGN KEY (
        dataset_pk
    )
    REFERENCES dataset (dataset_pk),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk) 
);
                     
CREATE TABLE IF NOT EXISTS experiment_setup (
    measurement_pk      VARCHAR (30),
    condition_pk        VARCHAR (30),
    condition_label     VARCHAR (30),
    setup_date          TEXT,
    experiment_location TEXT,
    PRIMARY KEY (
        measurement_pk,
        condition_pk
    ),
    FOREIGN KEY (
        measurement_pk
    )
    REFERENCES measurement (measurement_pk),
    FOREIGN KEY (
        condition_pk
    )
    REFERENCES condition (condition_pk) 
);
                     
CREATE TABLE IF NOT EXISTS located_in (
    place_pk             VARCHAR (30),
    site_pk              VARCHAR (30),
    latitude             DECIMAL (8, 4),
    longitude            DECIMAL (8, 4),
    location_description TEXT,
    location_check       TEXT,
    PRIMARY KEY (
        place_pk,
        site_pk
    ),
    FOREIGN KEY (
        place_pk
    )
    REFERENCES place (place_pk),
    FOREIGN KEY (
        site_pk
    )
    REFERENCES site (site_pk) 
);
                     
CREATE TABLE IF NOT EXISTS manuscript (
    manuscript_pk        VARCHAR (30)  PRIMARY KEY
                                       NOT NULL,
    title_manuscript     TEXT,
    doi_manuscript       VARCHAR (256),
    type_manuscript      VARCHAR (64),
    manuscript_publisher VARCHAR (64),
    manuscript_citation  TEXT,
    date_publication     TEXT,
    year_publication     INT,
    manuscript_comment   TEXT
);
                     
CREATE TABLE IF NOT EXISTS occurrence (
    population_pk            VARCHAR (30),
    site_pk                  VARCHAR (30),
    observation_date_initial VARCHAR (30),
    observation_date_final   VARCHAR (30),
    year_collection_initial  INT,
    year_collection_final    INT,
    comment_location         TEXT,
    origin                   VARCHAR (256),
    PRIMARY KEY (
        population_pk,
        site_pk
    ),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk),
    FOREIGN KEY (
        site_pk
    )
    REFERENCES site (site_pk) 
);
                     
CREATE TABLE IF NOT EXISTS place (
    place_pk          VARCHAR (30)   PRIMARY KEY
                                     NOT NULL,
    place_name        TEXT,
    location_name     TEXT,
    location_label    VARCHAR (2560),
    country_name      VARCHAR (256),
    continent_name    VARCHAR (256),
    geoname_countryid VARCHAR (256) 
);
                     
CREATE TABLE IF NOT EXISTS population (
    population_pk          VARCHAR (30)  PRIMARY KEY
                                         NOT NULL,
    population_name        TEXT,
    population_label       VARCHAR (256),
    population_description TEXT,
    species_reported       TEXT,
    authority              TEXT,
    population_facts       TEXT,
    comments               TEXT
);

CREATE TABLE IF NOT EXISTS publication (
    dataset_pk    VARCHAR (30),
    manuscript_pk VARCHAR (30),
    PRIMARY KEY (
        dataset_pk,
        manuscript_pk
    ),
    FOREIGN KEY (
        dataset_pk
    )
    REFERENCES dataset (dataset_pk),
    FOREIGN KEY (
        manuscript_pk
    )
    REFERENCES manuscript (manuscript_pk) 
);
                     
CREATE TABLE IF NOT EXISTS ref_taxonomy (
    taxonomy_pk         VARCHAR (30)  PRIMARY KEY
                                      NOT NULL,
    scientific_name     TEXT,
    taxonomy_id_ref     VARCHAR (30),
    taxonomy_db_name    VARCHAR (256),
    taxonomy_db_url     TEXT,
    taxonomy_db_version VARCHAR (64),
    parent_id           VARCHAR (30),
    parent_name         VARCHAR (256),
    rank_level          VARCHAR (256),
    phylum_name         TEXT,
    class_name          TEXT,
    order_name          TEXT,
    family_name         TEXT,
    genus_name          TEXT,
    species_name        TEXT,
    common_names        TEXT,
    comment_taxonomy    TEXT
);
                     
CREATE TABLE IF NOT EXISTS respiratory_chamber (
    technique_pk                 VARCHAR (30)   PRIMARY KEY
                                                NOT NULL,
    sensor_type                  TEXT,
    respiration_volume           DECIMAL (8, 2),
    delay_time                   VARCHAR (256),
    respiratory_chamber_material VARCHAR (256),
    incubation_time              DECIMAL (8, 2),
    respirometry_type            VARCHAR (256),
    breathing_mode               VARCHAR (256),
    metabolic_rate_type          VARCHAR (256) 
);

CREATE TABLE IF NOT EXISTS site (
    site_pk             VARCHAR (30)   PRIMARY KEY
                                       NOT NULL,
    site_name           TEXT,
    site_realm_general  VARCHAR (256),
    site_realm_specific VARCHAR (256),
    elevation_value     DECIMAL (6, 2),
    elevation_unit      VARCHAR (30),
    depth_value         DECIMAL (4, 2),
    depth_unit          VARCHAR (30) 
);

CREATE TABLE IF NOT EXISTS taxonomic_label (
    taxonomy_pk      VARCHAR (30),
    population_pk    VARCHAR (30),
    name_date        TEXT,
    reference_source TEXT,
    version_taxa     TEXT,
    PRIMARY KEY (
        taxonomy_pk,
        population_pk
    ),
    FOREIGN KEY (
        taxonomy_pk
    )
    REFERENCES ref_taxonomy (taxonomy_pk),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk) 
);
""")

# Insert csv content in table template
cursor.execute("PRAGMA foreign_keys = OFF;")

# Loop through all CSV files in the folder
for file in os.listdir(table_folder):
    if file.endswith(".csv"):
        table_name = file[:-4]  # Strip '.csv' to get the table name
        csv_path = os.path.join(table_folder, file)

        try:
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="append", index=False)
            print(f"Imported {file} into table '{table_name}'")
        except Exception as e:
            print(f"Error importing {file} into '{table_name}': {e}")

# Re-enable foreign key enforcement if desired
cursor.execute("PRAGMA foreign_keys = ON;")

# commit and close the db version
conn.commit()
conn.close()

print("Database v1.0 created and populated with Sharetrait data.")

print("Now we test the database with a query")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# ... your table creation and CSV import code ...

# --- TEST QUERY EXAMPLE ---
print("\n--- TEST QUERY: Measurements with Trait Info ---")
try:
    query = """
    SELECT i.individual_pk, t.trait_name, m.trait_value, m.trait_unit, m.measure_date
    FROM measurement m
    JOIN individual i ON m.individual_pk = i.individual_pk
    JOIN trait t ON m.trait_pk = t.trait_pk
    LIMIT 10;
    """
    results = cursor.execute(query).fetchall()
    for row in results:
        print(row)
except Exception as e:
    print("Query failed:", e)

conn.commit()
conn.close()

print("test completed")
