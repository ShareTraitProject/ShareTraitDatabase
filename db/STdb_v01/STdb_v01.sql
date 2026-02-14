--
-- File generated with SQLiteStudio v3.4.4 on Wed Jun 12 02:37:21 2024
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: acclimation_describe
DROP TABLE IF EXISTS acclimation_describe;

CREATE TABLE IF NOT EXISTS acclimation_describe (
    condition_pk   VARCHAR (30),
    acclimation_pk VARCHAR (30),
    PRIMARY KEY (
        condition_pk,
        acclimation_pk
    ),
    FOREIGN KEY (
        condition_pk
    )
    REFERENCES condition (condition_pk),
    FOREIGN KEY (
        acclimation_pk
    )
    REFERENCES acclimation_specification (acclimation_pk) 
);


-- Table: acclimation_specification
DROP TABLE IF EXISTS acclimation_specification;

CREATE TABLE IF NOT EXISTS acclimation_specification (
    acclimation_pk      VARCHAR (30) PRIMARY KEY
                                     NOT NULL,
    acclimation_name    TEXT,
    acclimation_mating  TEXT,
    acclimation_chamber TEXT,
    fasting_time        TEXT,
    fasting_unit        VARCHAR (30) 
);


-- Table: chamber_describe
DROP TABLE IF EXISTS chamber_describe;

CREATE TABLE IF NOT EXISTS chamber_describe (
    measurement_pk VARCHAR (30),
    technique_pk   VARCHAR (30),
    PRIMARY KEY (
        measurement_pk,
        technique_pk
    ),
    FOREIGN KEY (
        measurement_pk
    )
    REFERENCES measure (measurement_pk),
    FOREIGN KEY (
        technique_pk
    )
    REFERENCES respiratory_chamber (technique_pk) 
);


-- Table: condition
DROP TABLE IF EXISTS condition;

CREATE TABLE IF NOT EXISTS condition (
    condition_pk         VARCHAR (30)   PRIMARY KEY
                                        NOT NULL,
    temperature_value    DECIMAL (8, 2),
    temperature_unit     VARCHAR (30),
    oxygen_value         DECIMAL (8, 2),
    oxygen_unit          VARCHAR (30),
    carbondioxide_value  DECIMAL (8, 2),
    carbondioxide_unit   VARCHAR (30),
    photoperiod          TEXT,
    salinity_value       DECIMAL (8, 2),
    salinity_unit        VARCHAR (30),
    pH_value             DECIMAL (8, 2),
    food_type            TEXT,
    duration_days        INT,
    duration_unit        VARCHAR (30),
    duration_generations TEXT,
    comments_experiment  TEXT,
    humidity_value       DECIMAL (4, 2),
    humidity_unit        VARCHAR (30) 
);


-- Table: dataset
DROP TABLE IF EXISTS dataset;

CREATE TABLE IF NOT EXISTS dataset (
    dataset_pk           VARCHAR (30)  PRIMARY KEY
                                       NOT NULL,
    title_dataset        TEXT,
    doi_dataset          VARCHAR (256),
    sharetrait_datasetid TEXT,
    reference_type       VARCHAR (64),
    dataset_type         VARCHAR (64),
    dataset_publisher    VARCHAR (64),
    dataset_license      VARCHAR (64),
    dataset_version      VARCHAR (64),
    dataset_citation     TEXT,
    date_publication     TEXT,
    year_publication     INT,
    date_contribution    VARCHAR (64),
    dataset_trait        VARCHAR (64),
    dataset_comment      TEXT
);


-- Table: describe
DROP TABLE IF EXISTS describe;

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


-- Table: experiment_setup
DROP TABLE IF EXISTS experiment_setup;

CREATE TABLE IF NOT EXISTS experiment_setup (
    measurement_pk      VARCHAR (30),
    condition_pk        VARCHAR (30),
    condition_type      VARCHAR (30),
    setup_date          TEXT,
    experiment_location TEXT,
    PRIMARY KEY (
        measurement_pk,
        condition_pk
    ),
    FOREIGN KEY (
        measurement_pk
    )
    REFERENCES measure (measurement_pk),
    FOREIGN KEY (
        condition_pk
    )
    REFERENCES condition (condition_pk) 
);


-- Table: individual
DROP TABLE IF EXISTS individual;

CREATE TABLE IF NOT EXISTS individual (
    individual_pk           VARCHAR (30)   PRIMARY KEY
                                           NOT NULL,
    individual_id           VARCHAR (30),
    representative_stage    VARCHAR (30),
    individual_sex          VARCHAR (30),
    individual_type         VARCHAR (30),
    individual_parentpk     VARCHAR (30),
    parent_id               VARCHAR (30),
    parent_size_value       DECIMAL (8, 2),
    parent_size_unit        VARCHAR (30),
    parent_size_type        VARCHAR (30),
    parent_age              INT,
    parent_age_unit         VARCHAR (30),
    parent_sex              VARCHAR (30),
    mating_method           VARCHAR (256),
    method_type             VARCHAR (256),
    fecundity_temporal_unit VARCHAR (256),
    reproductive_stage      VARCHAR (256),
    strategy_of_protection  TEXT,
    description_individual  TEXT,
    comment                 TEXT
);


-- Table: located_in
DROP TABLE IF EXISTS located_in;

CREATE TABLE IF NOT EXISTS located_in (
    site_pk              VARCHAR (30),
    place_pk             VARCHAR (30),
    latitude_decimal     DECIMAL (8, 4),
    longitude_decimal    DECIMAL (8, 4),
    location_description TEXT,
    location_reference   TEXT,
    PRIMARY KEY (
        site_pk,
        place_pk
    ),
    FOREIGN KEY (
        site_pk
    )
    REFERENCES site (site_pk),
    FOREIGN KEY (
        place_pk
    )
    REFERENCES place (place_pk) 
);


-- Table: manuscript
DROP TABLE IF EXISTS manuscript;

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


-- Table: measure
DROP TABLE IF EXISTS measure;

CREATE TABLE IF NOT EXISTS measure (
    measurement_pk                 VARCHAR (30)   PRIMARY KEY
                                                  NOT NULL,
    individual_pk                  VARCHAR (30),
    trait_pk                       VARCHAR (30),
    trait_type                     VARCHAR (30),
    trait_value                    DECIMAL (8, 4),
    trait_unit                     VARCHAR (30),
    trait_error_estimate           VARCHAR (30),
    trait_error_type               VARCHAR (30),
    trait_converted                TEXT,
    individual_developmental_stage VARCHAR (30),
    fresh_mass                     DECIMAL (8, 2),
    fresh_mass_unit                VARCHAR (30),
    sample_size                    VARCHAR (30),
    size_condition                 VARCHAR (30),
    size_value                     DECIMAL (8, 2),
    size_value_initial             DECIMAL (8, 2),
    size_value_final               DECIMAL (8, 2),
    size_unit                      VARCHAR (30),
    size_type                      VARCHAR (30),
    life_stage_general             VARCHAR (256),
    life_stage_specific            VARCHAR (256),
    lifestage_specific_initial     VARCHAR (256),
    lifestage_specific_final       VARCHAR (256),
    comment_trait                  TEXT,
    measure_date                   TEXT,
    FOREIGN KEY (
        individual_pk
    )
    REFERENCES individual (individual_pk),
    FOREIGN KEY (
        trait_pk
    )
    REFERENCES trait (trait_pk) 
);


-- Table: occurrence
DROP TABLE IF EXISTS occurrence;

CREATE TABLE IF NOT EXISTS occurrence (
    population_pk           VARCHAR (30),
    site_pk                 VARCHAR (30),
    observation_date        VARCHAR (30),
    date_iso_initial        VARCHAR (30),
    date_iso_final          VARCHAR (30),
    year_collection_initial INT,
    year_collection_final   INT,
    comments_time           TEXT,
    origin                  VARCHAR (256),
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


-- Table: place
DROP TABLE IF EXISTS place;

CREATE TABLE IF NOT EXISTS place (
    place_pk       VARCHAR (30)  PRIMARY KEY
                                 NOT NULL,
    place_name     TEXT,
    country_name   VARCHAR (256),
    continent_name VARCHAR (256) 
);


-- Table: population
DROP TABLE IF EXISTS population;

CREATE TABLE IF NOT EXISTS population (
    population_pk       VARCHAR (30)  PRIMARY KEY
                                      NOT NULL,
    population_id       TEXT,
    population_label    VARCHAR (256),
    population_describe TEXT,
    species_reported    TEXT,
    authority           TEXT,
    population_facts    TEXT,
    pop_comments        TEXT
);


-- Table: publication
DROP TABLE IF EXISTS publication;

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


-- Table: ref_taxonomy
DROP TABLE IF EXISTS ref_taxonomy;

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


-- Table: respiratory_chamber
DROP TABLE IF EXISTS respiratory_chamber;

CREATE TABLE IF NOT EXISTS respiratory_chamber (
    technique_pk        VARCHAR (30)   PRIMARY KEY
                                       NOT NULL,
    sensory_type        TEXT,
    respiration_volume  INT,
    delay_time          VARCHAR (256),
    respiratory_chamber VARCHAR (256),
    metabolic_rate_type VARCHAR (256),
    incubation_time     DECIMAL (8, 2),
    respirometry_type   VARCHAR (256),
    breathing_mode      VARCHAR (256) 
);


-- Table: site
DROP TABLE IF EXISTS site;

CREATE TABLE IF NOT EXISTS site (
    site_pk             VARCHAR (30)   PRIMARY KEY
                                       NOT NULL,
    site_name           TEXT,
    site_realm_specific VARCHAR (256),
    site_realm_general  VARCHAR (256),
    elevation_value     DECIMAL (6, 2),
    elevation_unit      VARCHAR (30),
    temperature_value   DECIMAL (4, 2),
    temperature_unit    VARCHAR (30),
    depth_value         DECIMAL (4, 2),
    depth_unit          VARCHAR (30) 
);


-- Table: taxonomic_label
DROP TABLE IF EXISTS taxonomic_label;

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
    REFERENCES taxonomy (taxonomy_pk),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk) 
);


-- Table: trait
DROP TABLE IF EXISTS trait;

CREATE TABLE IF NOT EXISTS trait (
    trait_pk                VARCHAR (30)  PRIMARY KEY
                                          NOT NULL,
    trait_name              VARCHAR (256),
    trait_id                VARCHAR (30),
    trait_type              VARCHAR (256),
    trait_condition         TEXT,
    trait_parentid          VARCHAR (30),
    life_stage_initial      VARCHAR (256),
    life_stage_final        VARCHAR (256),
    trait_definition        TEXT,
    trait_definition_source TEXT,
    trait_unit              VARCHAR (30) 
);

-- Table: contains
DROP TABLE IF EXISTS contains;

CREATE TABLE IF NOT EXISTS contains (
    population_pk VARCHAR (30) NOT NULL,
    individual_pk VARCHAR (30) NOT NULL,
    PRIMARY KEY (
        population_pk,
        individual_pk
    ),
    FOREIGN KEY (
        population_pk
    )
    REFERENCES population (population_pk),
    FOREIGN KEY (
        individual_pk
    )
    REFERENCES individual (individual_pk) 
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
